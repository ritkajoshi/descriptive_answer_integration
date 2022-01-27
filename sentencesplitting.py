from nltk import tokenize
from nltk.tokenize import word_tokenize
import nltk
# nltk.download('punkt')

def sensplit(doctext):
    return tokenize.word_tokenize(doctext)
