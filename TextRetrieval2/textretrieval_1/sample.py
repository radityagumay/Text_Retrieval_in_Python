from nltk.corpus import stopwords
from nltk import PorterStemmer
from stemming.porter2 import stem
import math
import json
import codecs, sys, glob, os, unicodedata


# Concated [x]terms in [n]documents
# And pick unique terms
def concanated_terms_of_documents(document_tokens_list):
    terms = []
    for document_token in document_tokens_list:
        for term in document_token[:]:
            if term not in terms:
                terms.append(term)
    return terms


# Define stopword
# the, a, of, etc
def stop_word():
    terms_with_stop_word = []
    terms = concanated_terms_of_documents(document_tokens_list)
    for term in terms:
        if term not in set(stopwords.words('english')):
            terms_with_stop_word.append(term)
    return terms_with_stop_word


# Load Punctuation
# . ? % $ [etc]
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                    if unicodedata.category(unichr(i)).startswith('P'))


# Remove Punctuation
def remove_punctuation(unicode_text):
    return unicode_text.translate(tbl)


text_dirs = ["sample"]

# Create array to put clean document
# We will use to calc tf-idf
clean_document = []

# Collection of Terms
terms = []


# StopWord
def stop_word_2(term):
    return term not in set(stopwords.words('english'))


# Punctuation
def remove_punctuation_2(term):
    return term.translate(tbl)


# Stemming by Porter Algo
def stemming_by_porter_2(term):
    return stem(term)


# Stemming by Old Porter
def stemming_by_portter_1(term):
    return PorterStemmer().stem(term)


# Create Folder
if not os.path.exists("terms"):
    os.mkdir("terms")


def load_document():
    for i in text_dirs:
        global documents
        global size_doc
        documents = glob.glob(i + "/*.txt")
        size_doc = len(documents)
        for j in documents:
            response = {"documents": {j: []}}
            with codecs.open(j, "r", "utf-8") as raw_file:
                clean = remove_punctuation(raw_file.read().replace("\r", "").replace("\n", " "))
                term_metadata = clean.lower().split(None)
                for term in term_metadata:
                    if stop_word_2(term):
                        if term not in terms:
                            lower_term = term.lower()
                            terms.append(lower_term)
                            response["document"][j].append(lower_term)
        print "response:", response


data = {'list': []}
data['list'].append({'a': '1'})
data['list'].append({'b': '2'})
# print "data", data

load_document()

#
# for row in range(0, 10):
#    response.append({'author': "raditya " + str(row), 'short_title': "shortdesc " + str(row)})

# print "res", response
# print json.dumps(response)
