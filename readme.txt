ORACLE - Language Identification Predictor 

Purpose:
Language identification is the problem of determining the language origin of a given document.  
Automating this identification plays an important role in Natural Language Processing, since a human manual 
processes would consume a lot of time. 

Scope
The ORACLE system will be responsible for analyzing inputted text and determining its linguistic origin.  
The system will allow the user to input text and it will output a “best guess” or “unknown” if it's not confident 
in guessing.

Background:
There are several research area to solve the problem of language identification, the two broad approaches are 
feature-based supervised learning and unsupervised evolutionary computation.

APPROACH I - Feature-based Supervised Text Classification 
One approach, is to identify and classify certain features that appear in each language, for example, 
common word elements that occur frequently to a particular language and store it in a database or on disk 
and use a hash table or database to store pre-processed statistical analysis of the frequency of common words. 
So that when assessing the input text, the system would take the word intersection of the training set and a set 
of input text and count the common elements. And which ever language has the most common elements would be the most 
likely candidate for identifying the unknown language. 

Feature Vectors and Classifiers: 
Typically two phases are involved, a feature construction and feature section phase followed by a learning phase. 
The classifier is responsible for assigning a category or categories to a given document. In order to accomplish this,
the classifier needs a set of data as input for each assessment. It builds a feature vector of the most frequently 
used words and assigns a weight associated with the word. After the system trains the classifier using the obtained 
feature vectors from a training data set. 
There are several types of classifiers, following are a few classifiers that were considered.[5]
 Distance Vectors are the simplest classifiers, where for every category and document, there are representative 
 vectors produced. And some measure of the distance must be defined. We can count all the distances between vectors 
 of categories and a document's vector and the category closest to the document is chosen. Often the dot product 
 cosine value of vectors is used instead of distance.  Decision Trees can be used to select certain words based on 
 an information gain criterion and predict categories based on the occurrences of word combination.

Naive Bayes are probabilistic classifiers which use joint probabilities of words and categories to calculate the 
category of document. It uses Bayes Theorem with a strong (naive) independence assumptions between the features. 
This is a very efficient approach, training naive Bayes can be done in linear time if an approximation algorithm is 
used, as opposed to the expensive iterative approach. This is the most popular approach do to its simpler 
implementation. [5][6][7] 

K-nearest neighbours (kNN) classifiers ranks the k-nearest documents from the training set and categorizes documents 
for prediction.

Rocchio algorithm uses vector-space model to categorize documents, summing vectors of documents and categories with 
either positive or negative weights to assess which group the document belongs to. 

RIPPER classifier is a nonlinear rule learning algorithm which uses statistical data to create simple rules for 
categories then uses the conjunctions of the set of rules to assign a category.

Sleeping experts use a combination of several classifiers to create a master algorithm which combines results of 
these classifiers. Multiplicative updates of weights of classifiers can be efficient. [5][6]

Neural Networks: a computational model inspired by biology and the central nervous systems in brains. This systems 
use interconnected “neurons” which an compute values from inputs.Support Vector Machines (SVM) introduced by Vapnik 
is a learning methods based on the Structural Risk Maximization principle and mapping of input vectors in a high 
dimensional feature space. [5]

Caveats:
An issue that arises with the supervised learning approach is that it depends on the quality of the training data. 
Solely relying on common words might not be as a robust model to confidently identify the unknown language, specially 
if the input text is from the web and use different phonetic spelling of common words or merely have misspelled words. Another consequence is that the training set needs to be known beforehand which makes language identification a “classification” problem. [2]
As well, statistical classifiers can suffer from over-fitting, which can occur if a model is too complex or has too 
many parameters which brings a lot of noise and can cause poor predictive performance.[7]

N-gram  Another approach, is to use more a sophisticated supervised probabilistic model is to assess the probably 
per letter as opposed to a whole word. Cavnar and Trenkle (1994) present a probabilistic model of an N-gram Text 
Classification which is a contiguous sequence of n items from a given sequence of text or speech. The N-gram model 
attempts to predict the next item in a sequence in the form of a (n-1)-order Markov model. N-gram models are now 
commonly used in computational linguistics. One advantage of the N-gram is its simplicity and ability to scale up 
by increasing "n" (unigram: n=1, bigram: n=2, tri-gram: n=3 etc). [1][5]
For example, the N-gram model would compose the word “TEXT” as:

bi-grams: _T, TE, EX, XT, T_
tri-grams: _TE, TEX, EXT, XT_, T__
quad-grams: _TEX, TEXT, EXT_, XT__, T___
 N-gram frequency strategy: According to Zipf's Law, each word occurs in the hum language with a different frequency. 
 The n'th most common word in a human language text occurs with a frequency inversely proportional to n.
First, Cavnar and Trenkle create profiles with training set data for each of the different categories, then another 
profile is computed for the target document that is to be classified. Finally, a distance measure between the target 
document and the training set for each of the categories is calculated. The one with the closest distance is selected.[1]

Further, Cavnar and Trenkle keep the top 300 ngrams, they observed that this range as proper for language 
identification and saved a text category profile of them. Then calculated the “Out-Of-Place” measure against the 
training profiles. [1]

Advantages: N-grams are efficient at approximating matches.
Disadvantages: does not work well with short snippets of text.
[1][5][6]

Unstructured Text Classification
A more recent approach introduced by Řehůřek and Kolkus (2009) can detect multiple languages in an unstructured 
document and has successful results with short texts. Their approach  constructs language models based on word 
relevance to generate a decision function. The benefit of using words instead of n-gram characters is that the 
system is more open to human introspection. Instead of looking for common words in a given language (stopwords 
like “the”, “and”) they look for wards which are specific for a language or assess “how specific” they are to the 
language. Their algorithm depends on a relevance mapping: 
rel(word, language): W x L --> R
where:
W: set of all words present in the training data
L: set of considered languages
real-valued score of word w  |--> W in a language l |--> L its relevance. 
Hence, creates a soft grading of words as opposed a “common words” approach.
[2]
 APPROACH II - Unsupervised Evolutionary Algorithms Bungum and Gamback (2010) discuss the fluidity of change 
 inherent to a language. Language is ever-changing and hence a moving target since it is continuously evolving in 
 various directions just as it occurs in nature, this conceptual works well with genetic algorithms. The advances 
 in computational techniques both inspired by biology and machine learning in general has increased interest for 
 computational experiments in historical linguistics. 

They refer to Adriaans and van Zaanen who suggest the three main research avenues:  
recursive-theoretic approach where a learner asks questions that are truthfully answered by an oracle, which will 
result in a description of the grammar by the learner.
algorithms for the unsupervised identification of a grammar from a text corpus, that try to establish context-free 
grammar rules using clustering (grouping chunks of words). The use of genetic algorithms in grammar induction is 
part of this second research tradition.
probabilistic methods, that are supervised methods learning a formal grammar from annotated data. Probabilistic 
parsers by Charniak (1996) and Collins, (2003)
[3]

Computational Etymology
One interesting strategy discussed is the use of language phylogenies to automatically identify “cognate words” 
from unaligned word list given a family tree of languages by Hall and Klein (2010). Cognates are descendant words 
of an ancestor language, for example, the English word “night” and the Norwegian word “natt” or Slovak word “noc” 
have a similar origin. This strategy aims to model how languages develop over time and the model is based on the 
survival, evolution, and alignment of a language. The evolution is defined by how the words changes as they drift 
down the language family tree which models the etymology of the word and keeping track of their positions in the 
word lists, creating a dependency grammar. This will allow the model to associate the child language with it's 
ancestor language. Moreover, this strategy is more adaptive then the supervised approach which relies on static 
training set which can suffer from being out of date. [3]

Caveats
Currently evolutionary computation can help to optimize current techniques but it is still a ways away from 
outperforming or matching the performance of feature-based classification. But is worth mentioning as it offers a 
conceptual good fit to the evolution of language as it aims to adapt and handle the speciation of a language, until 
feature-based approaches which can suffer from stagnation since it needs to pre-processed and accounted for. [3] 

Summary
In summary, based on the gathered research, the proposed system employ strategies from  APPROACH I and will attempt 
to use APPROACH II for optimization to identify the language origin of a given input.  

System Specifications
ORACLE is a command line tool where the user inputs text in a certain language and ORACLE will attempt to identify 
the linguistic origin. Currently the system is trained to recognize "English", "French" and "German", however, 
the code based can be extended to teach the system to recognize more languages.

Strategies:
ORACLE has adopted the following strategies to identify the language, the system can easily be extended to adopt 
more strategies:
(1) Simple Simon Classification: a naive distance vector approach
(2) Naive Bayes Classification: a probabilistic classifier using joint probabilities of words and categories
(3) N-grams Text Classification: Cavnar and Trenkle contiguous sequence of n items
(4) Unstructured Text Classification: Rehurek and Kolkus algorithm 
(4) Sleeper Expert: employ all strategies to develop a master algorithm

*****Refer to Appendix I for template details


