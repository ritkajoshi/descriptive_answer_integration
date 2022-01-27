import re 
import string 
import nltk 
import spacy 
import pandas as pd 
import numpy as np 
import math 
from tqdm import tqdm 

from spacy.matcher import Matcher 
from spacy.tokens import Span 
from spacy import displacy 

pd.set_option('display.max_colwidth', 200)
# load spaCy model
nlp = spacy.load("en_core_web_sm")
# sample text 
text = "GDP in developing countries such as Vietnam will continue growing at a high rate." 

# create a spaCy object 
doc = nlp(text)
# print token, dependency, POS tag 
for tok in doc: 
  print(tok.text, "-->",tok.dep_,"-->", tok.pos_)
  