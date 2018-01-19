
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
def computeDF(unique_words, list_of_assignment_files):
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
# DF for each term t (dfT) was calculated by counting the number of
# documents which had the term t
dfT = computeDF(unigram_unique_words_no_stopwords, assignment_files)

# Compute Inverse Document Frequency (IDF) for each term t
# Formula: idf(t) = 1 + log N / df(t)
# df(t) = document frequency for term t
# idf(t) = inverse document frequency for term t
# N = total number of documents


