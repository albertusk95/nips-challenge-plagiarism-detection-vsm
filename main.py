
from __future__ import division
from math import log10, sqrt
from string import punctuation
import os
import nltk

# Variables
MODEL = 'unigram'
NUM_DOCS = 0
MASTER_DOC = 'combined_docs'
STOPWORDS = 'nltk_en_stopwords'
DATASET = 'docs'

# Return unigram unique words from a text
def extract_unique_words(text):
	#return text.translate(None, punctuation).split()
	return set(text.translate(None, punctuation).lower().split())


# Return bigram unique words from a text
def extract_bigram_unique_words(text):
	# Remove punctuations
	text_no_punctuations = text.translate(None, punctuation).lower().split()

	# Create bigrams from the input text
	bigrms = list(nltk.bigrams(text_no_punctuations))

	# Create unique bigrams
	unique_bigrms = set(bigrms)

	# Convert the set of unique bigrams back into list
	list_of_unique_bigrms = list(unique_bigrms)

	# Create list of unique bigrams represented as string
	list_of_unique_bigrams_str = [ "%s %s" % x for x in list_of_unique_bigrms ]

	return list_of_unique_bigrams_str


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

			
			# Convert the whole text into lower case
			all_text = all_text.lower()

			# Replace single quote (" ' ") into single white space
			all_text_no_quote = all_text.replace("'", " ")


			if unique_word in all_text_no_quote:
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

	# Convert the whole text into lower case
	all_text = all_text.lower()

	# Replace single quote (" ' ") into single white space
	all_text_no_quote = all_text.replace("'", " ")

	return all_text_no_quote.count(unique_word) / computeNumOfWordsInText(all_text_no_quote)


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


# Return the list of unique words without stopwords
def eliminateStopwords(unique_words):
	stopwords = nltk.corpus.stopwords.words('english')

	no_stopwords_list = []

	for unique_word in unique_words:
		words = unique_word.split()

		no_stopwords_list.append(unique_word)

		for word in words:
			if word in stopwords:
				no_stopwords_list.pop()
				break

	return no_stopwords_list


# Return the number of unigram words in a string
def computeNumOfWordsInText(text):
	numOfWords = len(text.split())

	if MODEL == 'bigram':
		if numOfWords == 1:
			numOfWords = 0
		else:
			numOfWords = numOfWords - 1
	elif MODEL == 'trigram':
		if numOfWords == 1 or numOfWords == 2:
			numOfWords = 0
		else:
			numOfWords = numOfWords - 2

	return numOfWords


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


# Convert the whole text into lower case
all_text = all_text.lower()

# Replace single quote (" ' ") into single white space
all_text_no_quote = all_text.replace("'", " ")

# Create unique words (vocabulary) based on the applied model
# Default is unigram
unique_words = extract_unique_words(all_text_no_quote)

#if MODEL == 'bigram':
# Unique words for bigram vector
#unique_words = extract_bigram_unique_words(all_text_no_quote)


# [TODO] Unique words for trigram vector







# DATASET PREPROCESSING

# Eliminate stopwords
'''
with open(STOPWORDS, 'r') as f:
	stopwords = f.readlines()

stopwords = [x.strip() for x in stopwords]

unique_words_no_stopwords = [x for x in unique_words if x not in stopwords]
'''

unique_words_no_stopwords = eliminateStopwords(unique_words)

print 'Unique words without stopwords'
print unique_words_no_stopwords



# VECTOR SPACE MODEL WITH COSINE SIMILARITY MEASURE

NUM_DOCS = len(assignment_files)

# Computer Document Frequency (DF) for each term t
DFs = computeDFs(unique_words_no_stopwords, assignment_files)

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
	TFIDF_weightvectors.append(computeTFIDFweightvector(assignment_file, unique_words_no_stopwords, IDFs))

print 'TFIDF weight vectors'
print TFIDF_weightvectors
print '\n'

# Compare each pair of assignment using Cosine Similarity
for idx_1 in range(0, NUM_DOCS):
	for idx_2 in range(0, NUM_DOCS):
		if idx_1 != idx_2:
			cosineSim = compareDocument(TFIDF_weightvectors[idx_1], TFIDF_weightvectors[idx_2])
			print 'Cosine similarity measure between document {0} and {1} gives {2} as the result'.format(idx_1, idx_2, cosineSim)


