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


def stop_word_2(term):
    return term not in set(stopwords.words('english'))


#### END OF STOPWORD #####

def stemming_by_porter_2(term):
    return stem(term)


class tfidf:
    def __init__(self):
        self.document = []
        self.corpus_dic = {}
        self.terms_documents = []

    def addDocument(self, doc_name, raw):
        doc_dict = {}
        terms = remove_punctuation(raw)
        list_of_word = terms.lower().split(None)
        for w in list_of_word:
            if (stop_word_2(w)):
                self.terms_documents.append(w.lower())
                doc_dict[w] = doc_dict.get(w, 0.0) + 1.0
                self.corpus_dic[w] = self.corpus_dic.get(w, 0.0) + 1.0

        length = float(len(list_of_word))
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length

        self.document.append([doc_name, doc_dict])
        print "log"
