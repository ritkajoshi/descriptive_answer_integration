import re
import networkx.algorithms.isomorphism as iso
import pandas as pd
import bs4
import requests
import spacy
import scipy as sp
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher 
from spacy.tokens import Span 

import networkx as nx

import matplotlib.pyplot as plt
from tqdm import tqdm

pd.set_option('display.max_colwidth', 200)
# %matplotlib inline
candidate_sentences = pd.read_csv("wiki_sentences_v2.csv")
candidate_sentences.shape

# doc = nlp("the drawdown process is governed by astm standard d823")

# for tok in doc:
#   print(tok.text, "...", tok.dep_)

def get_entities(sent):
  ## chunk 1
  ent1 = ""
  ent2 = ""

  prv_tok_dep = ""    # dependency tag of previous token in the sentence
  prv_tok_text = ""   # previous token in the sentence

  prefix = ""
  modifier = ""

  #############################################################
  
  for tok in nlp(sent):
    ## chunk 2
    # if token is a punctuation mark then move on to the next token
    if tok.dep_ != "punct":
      # check: token is a compound word or not
      if tok.dep_ == "compound":
        prefix = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          prefix = prv_tok_text + " "+ tok.text
      
      # check: token is a modifier or not
      if tok.dep_.endswith("mod") == True:
        modifier = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          modifier = prv_tok_text + " "+ tok.text
      
      ## chunk 3
      if tok.dep_.find("subj") == True:
        ent1 = modifier +" "+ prefix + " "+ tok.text
        prefix = ""
        modifier = ""
        prv_tok_dep = ""
        prv_tok_text = ""      

      ## chunk 4
      if tok.dep_.find("obj") == True:
        ent2 = modifier +" "+ prefix +" "+ tok.text
        
      ## chunk 5  
      # update variables
      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text
  #############################################################

  return [ent1.strip(), ent2.strip()]

print(get_entities("the film had 200 patents"))
entity_pairs = []

for i in tqdm(candidate_sentences["sentence"]):
  entity_pairs.append(get_entities(i))

 print(entity_pairs)
  
def get_relation(sent):

  doc = nlp(sent)

  # Matcher class object 
  matcher = Matcher(nlp.vocab)

  #define the pattern 
  pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 

  matcher.add("matching_1", None, pattern) 
  #  from website while below is from stackoverflow
  # matcher.add('Relation_name', [pattern], on_match=None)
  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]] 

  return(span.text)

# # print(get_relation("John completed the task"))  


relations = [print(get_relation(i) for i in tqdm(candidate_sentences['sentence']))]
pd.Series(relations).value_counts()[:15]
print(get_relation(i) for i in tqdm(candidate_sentences['sentence']))
# # extract subject

# source = [i[0] for i in entity_pairs]

# # extract object
# target = [i[1] for i in entity_pairs]
# a = {'source':source, 'target':target, 'edge':relations}
# kg_df = pd.DataFrame.from_dict(a, orient='index')
# kg_df = kg_df.transpose()
# kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})

# #  create a directed-graph from a dataframe
# G1=nx.from_pandas_edgelist(kg_df, "source", "target", 
                          # edge_attr=True, create_using=nx.MultiDiGraph())
# G2=nx.from_pandas_edgelist(kg_df, "source", "target", 
                          # edge_attr=True, create_using=nx.MultiDiGraph())

# plt.figure(figsize=(12,12))

# pos = nx.spring_layout(G)
# nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
# plt.show()

# G=nx.from_pandas_edgelist(kg_df[kg_df['edge']=="composed by"], "source", "target", 
#                           edge_attr=True, create_using=nx.MultiDiGraph())

# plt.figure(figsize=(12,12))
# pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes
# nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)
# plt.show()

 
# G1 = nx.DiGraph()
# G2 = nx.DiGraph()
# G1.add_path([1,2,3,4])
# G2.add_path([10,20,30,40])
# em = iso.numerical_edge_match('weight', 1)
# nx.is_isomorphic(G1, G2) 

# G1 = nx.cycle_graph(6)
# G2 = nx.wheel_graph(7)

# print(nx.graph_edit_distance(G1, G2))