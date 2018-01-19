
from __future__ import division
from math import log10, sqrt
from string import punctuation
import os

# Variables
NUM_DOCS = 0
MASTER_DOC = 'combined_docs'
STOPWORDS = 'nltk_en_stopwords'
DATASET = 'docs'

# Return unique words from a sentence
def extract_unique_words(sentence):
	return sentence.translate(None, punctuation).split()

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

		print 'TF'
		print TF
		print '\n'

		weightVector = TF * IDFs[idx]

		print 'Weight Vector'
		print weightVector
		print '\n'
		
		list_of_TFIDFweightvector.append(weightVector)

	return list_of_TFIDFweightvector


# Return the value of cosine between two document vectors
def compareDocument(TFIDF_weightvector_1, TFIDF_weightvector_2):
	# Compute the dot products
	dotProducts = 0
	
	for idx in range(0, len(TFIDF_weightvector_1)):
		dotProducts = dotProducts + (TFIDF_weightvector_1[idx] * TFIDF_weightvector_2[idx])

	# Compute the magnitude of the 1st TFIDF weight vector
	magnitude_1 = 0
	for idx in range(0, len(TFIDF_weightvector_1)):
		magnitude_1 = magnitude_1 + (TFIDF_weightvector_1[idx] * TFIDF_weightvector_1[idx])

	# Compute the magnitude of the 2nd TFIDF weight vector
	magnitude_2 = 0
	for idx in range(0, len(TFIDF_weightvector_2)):
		magnitude_2 = magnitude_2 + (TFIDF_weightvector_2[idx] * TFIDF_weightvector_2[idx])

	# Compute the cosine
	cosine = dotProducts / (sqrt(magnitude_1) * sqrt(magnitude_2))

	return cosine


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

print 'Unique words without stopwords'
print unigram_unique_words_no_stopwords

# VECTOR SPACE MODEL WITH COSINE SIMILARITY MEASURE

NUM_DOCS = len(assignment_files)

# Computer Document Frequency (DF) for each term t
DFs = computeDFs(unigram_unique_words_no_stopwords, assignment_files)

print 'DFs'
print DFs
print '\n'

# Compute Inverse Document Frequency (IDF) for each term t
IDFs = computeIDFs(NUM_DOCS, DFs)

print 'IDFs'
print IDFs
print '\n'

# Compute TF-IDF weight vector for each document
TFIDF_weightvectors = []

for assignment_file in assignment_files:
	TFIDF_weightvectors.append(computeTFIDFweightvector(assignment_file, unigram_unique_words_no_stopwords, IDFs))

print 'TFIDF weight vectors'
print TFIDF_weightvectors
print '\n'

# Compare each pair of assignment using Cosine Similarity
for idx_1 in range(0, NUM_DOCS):
	for idx_2 in range(0, NUM_DOCS):
		if idx_1 != idx_2:
			cosineSim = compareDocument(TFIDF_weightvectors[idx_1], TFIDF_weightvectors[idx_2])
			print 'Cosine similarity measure between document {0} and {1} gives {2} as the result'.format(idx_1, idx_2, cosineSim)


