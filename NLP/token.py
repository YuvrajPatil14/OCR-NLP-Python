# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3  2020

@author: Yuvraj
finding date in a text using python Natural language processing and 
regular expressions
ref: https://nbviewer.jupyter.org/github/lukewrites/NP_chunking_with_nltk/blob/master/NP_chunking_with_the_NLTK.ipynb
usage: python token.py
"""
import nltk
import re
import pprint
from nltk import Tree

patterns = """
    NP: {<JJ>*<NN>+}
    {<JJ>*<NN><CC>*<NN>+}
    """
    
NPChunker = nltk.RegexpParser(patterns)

sample_text = """
GOPAL SWEETS

1-�, MALHAR ROAD, gaRABHA NAGAR, LUDHIANA

RESTAURANT
sT-No -AAICS2076FSD 004

1N:03921067905
Date:26/05/2017

Bill No.20137 Time: 13:17:10

KOTs:20137

Particular Qty Rate VAT% Amount

AMRITSARI KULCHA & 2 125.00 13.0 250.00

CHHANA

SPECIAL THALI NAAN
PARANTHA
bread steak
BUTTER NAAN 45.00 13.0 90,00
quick bread
Total 800,00

2 230,00 13.0 460.00

Inclusive of yAT: 86.45
Incl. Of Surcharge:8.65
Incl. of Serv, Tax:39.90@ � 000%
@6, hy

GrandTate| "800.00

HAVE A NICE TIME

Your Order No. 137
"""



# =============================================================================
# def prepare_text(input):
#     tokenized_sentence = nltk.sent_tokenize(input)  # Tokenize the text into sentences.
#     tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]  # Tokenize words in sentences.
#     tagged_words = [nltk.pos_tag(word) for word in tokenized_words]  # Tag words for POS in each sentence.
#     word_tree = [NPChunker.parse(word) for word in tagged_words]  # Identify NP chunks
#     return word_tree 
# =============================================================================

new_patterns = """
    NP:    {<DT><WP><VBP>*<RB>*<VBN><IN><NN>}
           {<NN|NNS|NNP|NNPS><IN>*<NN|NNS|NNP|NNPS>+}
           {<JJ>*<NN|NNS|NNP|NNPS><CC>*<NN|NNS|NNP|NNPS>+}
           {<JJ>*<NN|NNS|NNP|NNPS>+}
           
    """

new_NPChunker = nltk.RegexpParser(new_patterns)

def prepare_text(input):
    tokenized_sentence = nltk.sent_tokenize(input)  # Tokenize the text into sentences.
    tokenized_words = [nltk.word_tokenize(sentence) for sentence in tokenized_sentence]  # Tokenize words in sentences.
    tagged_words = [nltk.pos_tag(word) for word in tokenized_words]  # Tag words for POS in each sentence.
    word_tree = [new_NPChunker.parse(word) for word in tagged_words]  # Identify NP chunks
    return word_tree 
#print(prepare_text(sample_text))
sentences = prepare_text(sample_text)

def return_a_list_of_NPs(sentences):
    nps = []  # an empty list in which to NPs will be stored.
    for sent in sentences:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                t = subtree
                t = ' '.join(word for word, tag in t.leaves())
                nps.append(t)
    return nps

print(return_a_list_of_NPs(sentences))