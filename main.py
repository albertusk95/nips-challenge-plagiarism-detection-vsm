
from string import punctuation
import os

MASTER_DOC = 'combined_docs'

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

# Extract unique words from the MASTER DOCUMENT
with open(MASTER_DOC, 'r') as f:
	all_text = f.read().replace('\n', ' ')

unique_words = extract_unique_words(all_text)



	