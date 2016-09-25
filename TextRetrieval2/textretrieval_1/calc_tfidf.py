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


text_dirs = ["articles/sample"]

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


# Remove Empty from array
def remove_empty(terms):
    return filter(None, terms)


# Returns integer with total number of tokens in a document
# toc = count number of tokens in a document
def token_count(document_tokens):
    return len(document_tokens)


# Returns float term frequency (TF),
# normalized for document size
# tf = term count / token count
def term_frequency(term, document_tokens):
    return term_count(term, document_tokens)  # / float(token_count(document_tokens))


# Returns integer Term Count for a document
# tc = count number of term occurence in document
def term_count(term, document_tokens):
    return document_tokens.count(term.lower())


# Returns the float Inverse Document Frequency  (IDF)
def inverse_document_frequency(term, document_tokens_list):
    docslen = len(document_tokens_list)
    docscontainterm = document_frequency(term, document_tokens_list)
    return math.log10(docslen / float(docscontainterm))


def term_frequency_document(term, documents):
    term_frequency(term, documents)


# Returns the float Term Frequency - Inverse Document Frequency or tf-idf
def tf_idf(term, document_tokens, document_tokens_list):
    return term_frequency(term, document_tokens) * inverse_document_frequency(term, document_tokens_list)


# Returns the number of documents containing the term
# from a list of document tokens
def document_frequency(term, document_tokens_list):
    nr = 0
    for document_tokens in document_tokens_list:
        if term_count(term, document_tokens) > 0:
            nr += 1
    return nr


term = "december"
load_document()

print "Terms:", remove_empty(terms)
print "\n"
print "Document Count:", size_doc
print "Terms Count:\t", len(terms)
print "Term:\t\t\t", term
print "TF:\t\t\t\t", term_frequency(term, documents[2])
print "IDF:\t\t\t", inverse_document_frequency(term, terms)
print "TF--IDF:\t\t", tf_idf(term, documents, terms)

