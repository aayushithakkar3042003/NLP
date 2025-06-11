import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
text = "Running run runner ran easily"
stemmer = PorterStemmer()
tokens = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Stemmed Words",stemmed_words)