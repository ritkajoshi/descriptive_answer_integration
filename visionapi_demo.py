import os,io
import numpy as np
from nltk import tokenize
from nltk.tokenize import word_tokenize
# import nltk
import yake 
import nltk
from google.cloud import vision
from google.cloud.vision_v1 import types
from jaccardsimi import * 
from keywordextract import *
from sentencesplitting import *

# OCR 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'ServiceAccountToken.json'

client=vision.ImageAnnotatorClient()
FOLDER_PATH=r'C:\Users\Ritika joshi\OneDrive\Documents\Python venv\VisionAPIDemo\Images'
IMAGE_FILE='test4.jpg'
FILE_PATH=os.path.join(FOLDER_PATH,IMAGE_FILE)

with io.open(FILE_PATH,'rb') as image_file:
    content= image_file.read()


image=vision.Image(content=content)
response = client.document_text_detection(image=image)

# doctext1=response.full_text_annotation.text
# doctext1="Photosynthesis, the process by which green plants and certain other organisms transform light energy into chemical energy"
doctext1=response.full_text_annotation.text
print(doctext1)
doctext2="Photosynthesis is the process used by plants, algae and certain bacteria to turn sunlight, carbon dioxide (CO2) andwater into food (sugars) and oxygen.Here's a look at the general principles of photosynthesis and related research to help develop clean fuels and sources of renewable energy."
 

#sentence splitting
a=sensplit(doctext1)
b=sensplit(doctext2)


#find Jaccard Similarity between the two sets 
c=jaccard(a, b)
print(c)

# keyword extraction in text
list5=keywordextract(doctext1,doctext2)
print(list5)

# #concept graph 

# #language check

# #bert


