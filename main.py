
from math import log10
from string import punctuation
import os

# Variables
NUM_DOCS = 0
MASTER_DOC = 'combined_docs'
STOPWORDS = 'nltk_en_stopwords'
DATASET = 'docs'

# Return unique words from a sentence
def extract_unique_words(sentence):
	return sentence.translate(None, punctuation).lower().split()

# Return the document frequency for each term in the input list
def computeDFs(unique_words, list_of_assignment_files):
	# DF for each term t (dfT) was calculated by counting the number of
	# documents which had the term t
	list_of_df = []

	for unique_word in unique_words:
		counter = 0
		for assignment_file in list_of_assignment_files:
			with open(assignment_file, 'r') as f:
				all_text = f.read().replace('\n', ' ')

			if unique_word in all_text:
				counter = counter + 1

		list_of_df.append(counter)

	return list_of_df

# Return the inverse document frequency for each term in the input list
def computeIDFs(NUM_DOCS, DFs):
	# Formula: idf(t) = 1 + log N / df(t)
	# df(t) = document frequency for term t
	# idf(t) = inverse document frequency for term t
	# N = total number of documents
	list_of_idf = []

	for df in DFs:
		idf = 1 + (log10(NUM_DOCS / df))
		list_of_idf.append(idf)

	return list_of_idf


# Return the term frequency of a term in a document
def computeTF(assignment_file, unique_word):
	with open(assignment_file, 'r') as f:
		all_text = f.read().replace('\n', ' ')

	return all_text.count(unique_word) / computeNumOfWordsInText(all_text)


# Return the TF-IDF weight vector for a document
def computeTFIDFweightvector(assignment_file, unique_words, IDFs):
	# Wtd = TFtd x IDFt
	# Wtd = TF-IDF weight vector
	# TFtd = frequency of a term in a document
	# IDFt = inverse document frequency for term t
	list_of_TFIDFweightvector = []

	for idx in range(0, len(unique_words)):
		TF = computeTF(assignment_file, unique_words[idx])
		weightVector = TF * IDFs[idx]
		list_of_TFIDFweightvector.append(weightVector)

	return list_of_TFIDFweightvector


# Return the number of words in a string
def computeNumOfWordsInText(text):
	return len(text.split())


# Combine all documents into one file called MASTER DOCUMENT
assignment_files = []

for filename in os.listdir(DATASET):
	assignment_files.append(DATASET + '/' + filename)

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

# Computer Document Frequency (DF) for each term t
DFs = computeDFs(unigram_unique_words_no_stopwords, assignment_files)

# Compute Inverse Document Frequency (IDF) for each term t
IDFs = computeIDFs(NUM_DOCS, DFs)

# Compute TF-IDF weight vector for each document
TFIDF_weightvectors = []

for assignment_file in assignment_files:
	TFIDF_weightvectors.append(computeTFIDFweightvector(assignment_file, unigram_unique_words_no_stopwords, IDFs))
