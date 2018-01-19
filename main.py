
from string import punctuation
import os

# Variables
NUM_DOCS = 0
MASTER_DOC = 'combined_docs'
STOPWORDS = 'nltk_en_stopwords'

# Return unique words from a sentence
def extract_unique_words(sentence):
	return sentence.translate(None, punctuation).lower().split()

# Combine all documents into one file called MASTER DOCUMENT
dataset = 'docs'
assignment_files = []

for filename in os.listdir(dataset):
	assignment_files.append(dataset + '/' + filename)

with open(MASTER_DOC, 'w') as outfile:
	for fname in assignment_files:
		with open(fname) as infile:
			for line in infile:
				outfile.write(line)

# Extract unique words (unigram, bigram, trigram) from the MASTER DOCUMENT
with open(MASTER_DOC, 'r') as f:
	all_text = f.read().replace('\n', ' ')

# Unique words for unigram vector
unigram_unique_words = extract_unique_words(all_text)


# DATASET PREPROCESSING

# Eliminate stopwords
with open(STOPWORDS, 'r') as f:
	stopwords = f.readlines()

stopwords = [x.strip() for x in stopwords]

unigram_unique_words_no_stopwords = [x for x in unigram_unique_words if x not in stopwords]

# VECTOR SPACE MODEL WITH COSINE SIMILARITY MEASURE

NUM_DOCS = len(assignment_files)

# Compute Inverse Document Frequency (IDF) for each term t


