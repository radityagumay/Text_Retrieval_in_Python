from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StandardAnalyzer
from string import maketrans, punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import codecs, sys, glob, os, unicodedata

# Define stopwords
stopset = set(stopwords.words('english'))

# Load unicode punctuation
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))

# Create function to strip punctuation
def remove_punctuation(unicode_text):
	return unicode_text.translate(tbl)

# Make index folder
if not os.path.exists("simple_test/index_for_sample_files"):
	os.makedirs("simple_test/index_for_sample_files")

