from nltk.corpus import stopwords
from nltk import PorterStemmer
from stemming.porter2 import stem
import math
import codecs, sys, glob, os, unicodedata

tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                    if unicodedata.category(unichr(i)).startswith('P'))


# Remove Punctuation
def remove_punctuation(unicode_text):
    return unicode_text.translate(tbl)


### STOP WORD #####
def concanated_terms_of_documents(document_tokens_list):
    terms = []
    for document_token in document_tokens_list:
        for term in document_token[:]:
            if term not in terms:
                terms.append(term)
    return terms


# Remove useless word
def stop_word():
    terms_with_stop_word = []
    terms = concanated_terms_of_documents(document_tokens_list)
    for term in terms:
        if term not in set(stopwords.words('english')):
            terms_with_stop_word.append(term)
    return terms_with_stop_word
#### END OF STOPWORD #####

def stemming_by_porter_2(term):
    return stem(term)

class rtfidf:
    def __init__(self):
        self.weight = False
        self.document = []
        self.corpus_dic = {}

    def addDocument(self, doc_name, list_of_word):
        doc_dict = {}
        for i in list_of_word:
