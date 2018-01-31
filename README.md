# Plagiarism Detection on Electronic Text Based Assignments Using Vector Space Model (iciafs14)

## Global NIPS Paper Implementation Challenge 2017

I implemented the paper based on the research methodology

## Original Paper

https://arxiv.org/pdf/1412.7782.pdf

## Programming Tools

<ul>
  <li>Python 2.7</li>
  <li>scikit-learn</li>
  <li>NLTK</li>
</ul>

## Main Goal

Develope an effective plagiarism detection tool for text based assignments by comparing unigram, bigram, and trigram of vector space model with cosine and jaccard similarity measure

## Methodology

<ul>
  <li>Combining students answer into one single answer file (MASTER DOCUMENT)
    <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_1.png?raw=true"/>
    </p>
  </li>
  <li>Extract unique words (unigram, bigram, trigram) from the MASTER DOCUMENT
    <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_2.png?raw=true"/>
    </p>
    <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_3.png?raw=true"/>
    </p>
  </li>
  <li>Eliminate stopwords
    <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_4.png?raw=true"/>
    </p>
  </li>
  <li>Compute Document Frequency (DF) and Inverse Document Frequency (IDF) for each term
    <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_5.png?raw=true"/>
    </p>
  </li>
  <li>Compute TF-IDF Weight Vector for each document
   <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_6.png?raw=true"/>
   </p>
  </li>
  <li>Compare each pair of assignment using Cosine Similarity
   <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_7.png?raw=true"/>
   </p>
  </li>
  <li>Compare each pair of assignment using Jaccard Similarity
   <p>
      <img src="https://github.com/albertusk95/nips-challenge-plagiarism-detection-vsm/blob/master/assets/img/step_8.png?raw=true"/>
   </p>
  </li>
</ul>

---

**Albertus Kelvin**
**January 20th, 2018**
