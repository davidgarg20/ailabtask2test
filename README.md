# AI Lab Task 3

## Code Structure

### Main Folder  
19075089-David-Garg

#### Sub-Folders under Main Folder

1. COGW
2. SG
3. GLOVE
4. CNN

#### COGW
Files

1. model.txt - Model file generated using COGW
2. cogw.ipynb - Python NoteNN book containing the COGW code

#### SG
Files

1. model.txt - Model file generated using Skip Gram
2. sg.ipynb - Python Notebook containing the Skip Gram code

#### GLOVE
Files

1. model.txt - Model file generated using GLOVE
2. glove.ipynb - Python Notebook containing the GLOVE code

#### CNN
Files

1. model.txt - Model file generated using CNN
2. cnn.iypnb - Python Notebook containing the CNN code

## Word2Vec 
Word2vec is a technique for natural language processing. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. As the name implies, word2vec represents each distinct word with a particular list of numbers called a vector. The vectors are chosen carefully such that a simple mathematical function (the cosine similarity between the vectors) indicates the level of semantic similarity between the words represented by those vectors. 

### CBOW (Continuous Bag of Words) :
CBOW model predicts the current word given context words within specific window. The input layer contains the context words and the output layer contains the current word. The hidden layer contains the number of dimensions in which we want to represent current word present at the output layer.

Advantages:
1. Being probabilistic is nature, it is supposed to perform superior to deterministic methods(generally).
2. It is low on memory. It does not need to have huge RAM requirements like that of co-occurrence matrix where it needs to store three huge matrices.

DisAdvantages:
1. CBOW takes the average of the context of a word (as seen above in calculation of hidden activation). For example, Apple can be both a fruit and a company but
CBOW takes an average of both the contexts and places it in between a cluster for fruits and companies.
2. Training a CBOW from scratch can take forever if not properly optimized.

### Skip Gram : 
Skip gram predicts the surrounding context words within specific window given current word. The input layer contains the current word and the output layer contains the context words. The hidden layer contains the number of dimensions in which we want to represent current word present at the input layer.

Advantages:
1. Skip-gram model can capture two semantics for a single word. i.e it will have two vector representations of Apple. One for the company and other for the fruit.
2. Skip-gram with negative sub-sampling outperforms every other method generally

DisAdvantages:
1. Both of the CBOW and skip-gram model fails to identify the combined word phrases. e.g “New York” is a single word and cannot be treated as New and York
two different words.
2. Unfortunately, CBOW and skip-gram cannot capture the polysemy, because they tend to represent a word as a single vector

Training
A Word2vec model can be trained with hierarchical softmax and/or negative sampling. To approximate the conditional log-likelihood a model seeks to maximize, the hierarchical softmax method uses a Huffman tree to reduce calculation. The negative sampling method, on the other hand, approaches the maximization problem by minimizing the log-likelihood of sampled negative instances. According to the authors, hierarchical softmax works better for infrequent words while negative sampling works better for frequent words and better with low dimensional vectors. As training epochs increase, hierarchical softmax stops being useful.



### GloVe : Global Vectors for Word Representation
GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space. 
 
1.   Nearest neighbors
The Euclidean distance (or cosine similarity) between two word vectors provides an effective method for measuring the linguistic or semantic similarity of the corresponding words. Sometimes, the nearest neighbors according to this metric reveal rare but relevant words that lie outside an average human's vocabulary. 

2.   Linear substructures
The similarity metrics used for nearest neighbor evaluations produce a single scalar that quantifies the relatedness of two words. This simplicity can be problematic since two given words almost always exhibit more intricate relationships than can be captured by a single number. For example, man may be regarded as similar to woman in that both words describe human beings; on the other hand, the two words are often considered opposites since they highlight a primary axis along which humans differ from one another.

Training
The GloVe model is trained on the non-zero entries of a global word-word co-occurrence matrix, which tabulates how frequently words co-occur with one another in a given corpus. Populating this matrix requires a single pass through the entire corpus to collect the statistics. For large corpora, this pass can be computationally expensive, but it is a one-time up-front cost. Subsequent training iterations are much faster because the number of non-zero matrix entries is typically much smaller than the total number of words in the corpus. 

Commands
1. git clone https://github.com/stanfordnlp/glove
2. cd glove && make
3. ./glove.sh
4. from gensim.scripts.glove2word2vec import glove2word2vec
5. from gensim.models.keyedvectors import KeyedVectors

## CNN
A convolutional neural network (CNN) is a specific type of artificial neural network that uses perceptrons, a machine learning unit algorithm, for supervised learning, to analyze data. CNNs apply to image processing, natural language processing and other kinds of cognitive tasks.A convolutional neural network is also known as a ConvNet.
It is an interaction of identification and of mistakenly spelled words in a content. In common language, it fundamentally examines the content and concentrates
contained in it. It at that point looks at each word to a rundown of effectively spelled words (a greater amount of like a word reference) and henceforth distinguishes
the incorrectly spelled words.
Usage - We have actualized a binary characterization model of CNN in which we have utilized a dataset which contains accurately spelled words alongside some
wrongly spelled words in the proportion of 10:1 (i.e., 10 right words for each wrongly spelled word).
In this I have used my CGOW embedding


  
