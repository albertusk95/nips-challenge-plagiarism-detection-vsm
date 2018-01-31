# Plagiarism Detection on Electronic Text Based Assignments Using Vector Space Model (iciafs14)

## Global NIPS Paper Implementation Challenge

I implemented the paper based on the research methodology

## Original Paper

https://arxiv.org/pdf/1412.7782.pdf

## Main Goal

Develope an effective plagiarism detection tool for text based assignments by comparing unigram, bigram, and trigram of vector space model with cosine and jaccard similarity measure

## Programming Tools

<ul>
  <li>Python 2.7</li>
  <li>scikit-learn</li>
  <li>NLTK</li>
</ul>

## Files

Several important files / directories:
<ul>
  <li><b>main.py</b>
    <p>
      Main file containing the whole source code
    </p>
  </li>
  <li><b>docs</b>
    <p>
      A directory containing students answer. Each answer is stored in a document having specified file name, namely <b>assignment_index</b>. The word <b>assignment</b> is fixed and word <b>index</b> is an integer that will be incremented each time a new student is added
    </p>
  </li>
  <li><b>combined_docs</b>
    <p>
      Each student answer will be combined into one document called MASTER Document. The detection processes will be done using this combined document
    </p>
  </li>
</ul>

## To Run

To run the program, execute the following command:

_python main.py_

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

**Albertus Kelvin**<br/>
**Bandung Institute of Technology**<br/><br/>
**Code was developed on January 20th, 2018**<br/>
**Code was made publicly available on January 31st, 2018**
