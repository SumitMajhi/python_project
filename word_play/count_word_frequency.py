def count_word_frequency(text):
    text = text.lower()
    
    import string
    text = text.translate(str.maketrans('','', string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word} : {count}")

sample_text = "Hello world! Learning python by making projects , we will cross paths eventually on my python learning journey. Meet you soon hello world."
count_word_frequency(sample_text)
