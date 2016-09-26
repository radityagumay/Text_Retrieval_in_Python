from nltk.corpus import stopwords
from nltk import PorterStemmer
from stemming.porter2 import stem
import math
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


text_dirs = ["articles/business"]

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
            with codecs.open(j, "r", "utf-8") as raw_file:
                clean = remove_punctuation(raw_file.read().replace("\r", "").replace("\n", " "))
                term_metadata = clean.lower().split(None)
                for term in term_metadata:
                    if stop_word_2(term):
                        if term not in terms:
                            terms.append(term.lower())


def write_terms():
    with codecs.open("terms/terms.txt", "w", "utf-8") as temp:
        for term in terms:
            temp.write(stemming_by_porter_2(term) + " ")


def write_original_terms():
    with codecs.open("terms/origin_terms.txt", "w", "utf-8") as temp:
        for term in terms:
            temp.write(term + " ")


load_document()
write_terms()
write_original_terms()
print "Terms: ", terms
