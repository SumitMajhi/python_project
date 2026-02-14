import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trial Salary Dashboard", layout="wide")
st.title("📊 Monthly Salary Dashboard")

paybill = pd.read_excel("PAYBILL.xlsx")
payrec = pd.read_excel("PAYREC.xlsx")

months = sorted(paybill["YYMM"].unique())
selected_month = st.selectbox("Select Month (YYMM)", months)

pb = paybill[paybill["YYMM"] == selected_month]
pr = payrec[payrec["YYMM"] == selected_month]

tab1, tab2 = st.tabs(["👤 Employee View", "🏢 Company Summary"])

# Tab - 1 : Employee View
with tab1:
    st.subheader("Employee Salary Details")

    emp_list = pb["NEW_PERNO"].unique()
    emp = st.selectbox("Select Employee (NEW_PERNO)", emp_list)

    emp_pb = pb[pb["NEW_PERNO"] == emp]
    emp_pr = pr[pr["NEW_PERNO"] == emp]

    col1, col2, col3 = st.columns(3)
    col1.metric("Gross Pay", f"₹ {emp_pb['GPAY'].iloc[0]:,.0f}")
    col2.metric("Total Deduction", f"₹ {emp_pb['DEDN'].iloc[0]:,.0f}")
    col3.metric("Net Pay", f"₹ {emp_pb['NPAY'].iloc[0]:,.0f}")

    st.divider()

    def draw_bar_streamlit(title, columns):
        data = emp_pb[columns].iloc[0].fillna(0)

        st.subheader(title)

        df = data.reset_index()
        df.columns = ["Component", "Amount"]

        st.bar_chart(
            df,
            x="Component",
            y="Amount"
        )

    draw_bar_streamlit(
        "Salary & Incentive Breakdown",
        [
            "BASIC", "PERS_PAY", "DA", "MINE_ALL",
            "NIGHT_ALL", "INC_PIS", "INC_MPPIS", "INC_FIXED"
        ]
    )

    st.divider()

    draw_bar_streamlit(
        "Statutory Deductions",
        ["CPF_PC", "EPS", "PTAX", "ITAX", "SURCH", "CESS"]
    )

    st.divider()

    draw_bar_streamlit(
        "Voluntary Deductions",
        ["VPF", "LIC", "SESBF", "SEWA", "COOP", "CLUB", "CAF_TAX", "CAF_NTAX"]
    )

    st.divider()

    draw_bar_streamlit(
        "Recoveries",
        ["HRENT", "ELEC", "CONS", "CPF_LNPR", "CPF_LNINT", "FEST_REC"]
    )

    st.divider()


# tab - 2 : Company Summary
with tab2:
    st.subheader("Company Salary Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Employees", pb["NEW_PERNO"].nunique())
    col2.metric("Total Net Payout", f"₹ {pb['NPAY'].sum():,.0f}")
    col3.metric("Average Net Pay", f"₹ {pb['NPAY'].mean():,.0f}")

    st.divider()

    earn_company = pr[pr["IND"] == 1]["AMOUNT"].sum()
    ded_company = pr[pr["IND"] == 2]["AMOUNT"].sum()

    st.subheader("Earnings vs Deductions")
    st.bar_chart({
        "Earnings": earn_company,
        "Deductions": ded_company
    })

    st.subheader("Top Salary Components")
    top_codes = (
        pr.groupby("CODE")["AMOUNT"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_codes)

    st.divider()

    bins = [10000, 50000, 100000, 150000, 200000, 250000]
    labels = ["10K–50K", "50K–100K", "100K–150K", "150K–200K", "200K–250K"]

    basic_salary = pb["BASIC"].dropna()

    salary_ranges = pd.cut(
        basic_salary,
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    range_counts = (
        salary_ranges
        .value_counts()
        .sort_index()
    )

    range_df = range_counts.reset_index()
    range_df.columns = ["BASIC Salary Range", "Number of Employees"]

    st.subheader("Employee Distribution by BASIC Salary Range")

    st.bar_chart(
        range_df,
        x="BASIC Salary Range",
        y="Number of Employees"
    )


    st.divider()
    st.subheader("Employee Benefit Utilization & Cost Summary")

    salary_cols = [
        'BASIC', 'PERS_PAY', 'DA',
        'MINE_ALL', 'NIGHT_ALL',
        'INC_PIS', 'INC_MPPIS', 'INC_FIXED'
    ]

    statutory = ['CPF_PC','EPS','PTAX','ITAX','SURCH','CESS']

    voluntary = ['VPF','LIC','SESBF','SEWA','COOP','CLUB','CAF_TAX','CAF_NTAX']

    recoveries = ['HRENT','ELEC','CONS','CPF_LNPR','CPF_LNINT','FEST_REC']


    def build_table(columns):
        rows = []
        for col in columns:
            if col in pb.columns:
                rows.append({
                    "Component": col,
                    "Employees Receiving": int((pb[col] > 0).sum()),
                    "Total Amount": pb[col].sum()
                })
        df = pd.DataFrame(rows)
        df["Total Amount"] = df["Total Amount"].apply(lambda x: f"₹ {x:,.0f}")
        return df
    

    st.markdown("###  Salary Components")
    st.dataframe(
        build_table(salary_cols),
        use_container_width=True
    )

    st.markdown("###  Statutory Deductions")
    st.dataframe(
        build_table(statutory),
        use_container_width=True
    )

    st.markdown("###  Voluntary Deductions")
    st.dataframe(
        build_table(voluntary),
        use_container_width=True
    )

    st.markdown("###  Recoveries")
    st.dataframe(
        build_table(recoveries),
        use_container_width=True
    )

    st.subheader("Total Cost by Category")

    category_totals = {
        "Salary": pb[salary_cols].sum().sum(),
        "Statutory": pb[statutory].sum().sum(),
        "Voluntary": pb[voluntary].sum().sum(),
        "Recoveries": pb[recoveries].sum().sum()
    }

    st.bar_chart(category_totals)

    st.subheader("Top 10 Costliest Components")

    all_components = salary_cols + statutory + voluntary + recoveries

    top_cost_df = (
        pb[all_components]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_cost_df)

    st.subheader("Employee Coverage by Component (%)")

    coverage_data = {}

    total_employees = pb["NEW_PERNO"].nunique()

    for col in salary_cols + statutory + voluntary + recoveries:
        if col in pb.columns:
            coverage_data[col] = (pb[col] > 0).sum() / total_employees * 100

    coverage_df = (
        pd.Series(coverage_data)
        .sort_values(ascending=False)
    )

    st.bar_chart(coverage_df)

    st.subheader("Salary vs Deductions Split")

    salary_total = pb[salary_cols].sum().sum()
    deduction_total = pb[statutory + voluntary + recoveries].sum().sum()

    st.bar_chart({
        "Salary": salary_total,
        "Deductions & Recoveries": deduction_total
    })

