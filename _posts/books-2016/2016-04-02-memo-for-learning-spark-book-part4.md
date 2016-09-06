---
category: books
published: false
layout: post
title: 『 读书笔记 』Learning Spark [part 4]
description: 好书，应该从不嫌旧
---


## 写在前面

这本书是在 2015.02 就出版的，那个时候 spark 应该还只是 1.1 左右，最近准备看一两本讲 spark 的高质量的书，算是梳理一下自己的思维。期间因为觉得这本书出版得太早，可能会缺少 spark 现在的很多 feature，所以选了另外一本在 gitbook 上开源的书。可是看了这本 learning spark 后，发现两本书还是有很大的差别。虽然必须承认这本书出版得较早，里面缺少了一些 spark 的新 feature，但是这完全不影响你学习 spark，掌握 spark 的里里外外。我比较推荐这本书作为 spark 初学者的入门书，而且这本书还是 spark 的作者 Matei 合著的，在很多问题的解释上会比其他人解释得更浅显易懂。

spark 的知识点很多，也很细碎，初学者需要通读几遍再加上亲身实践，才能把这些细小的知识点串起来，慢慢开始深入了解 spark，inside out。这篇读书笔记是我在读 learning spark 时候记录的书中的一些知识点，供以后 review 用，当然大家也可以参考参考。

书籍简介：

- 第一本介绍 spark 的书
- 由 spark 开发者写
- 完全 free，在 safaribook 上可以直接在线看：[learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- 本书代码: [code of learning spark on github](https://github.com/databricks/learning-spark)


## 11. Machine Learning with MLlib

### 11.1 Overview

MLlib’s design and philosophy are simple: *it lets you invoke various algorithms on distributed datasets, representing all data as RDDs*. MLlib introduces a few data types (e.g., labeled points and vectors), but at the end of the day, it is simply a set of functions to call on RDDs. For example, to use MLlib for a text classification task (e.g., identifying spammy emails), you might do the following:

- Start with an RDD of strings representing your messages.
- Run one of MLlib’s feature extraction algorithms to convert text into numerical features (suitable for learning algorithms); this will give back an RDD of vectors.
- Call a classification algorithm (e.g., logistic regression) on the RDD of vectors; this will give back a model object that can be used to classify new points.
- Evaluate the model on a test dataset using one of MLlib’s evaluation functions.

One important thing to note about MLlib is that it contains only parallel algorithms that run well on clusters. Some classic ML algorithms are not included because *they were not designed for parallel platforms*, but in contrast MLlib contains several recent research algorithms for clusters, such as distributed random forests, K-means, and alternating least squares. *This choice means that MLlib is best suited for running each algorithm on a large dataset*. If you instead have many small datasets on which you want to train different learning models, it would be better to use a single-node learning library (e.g., Weka or SciKit-Learn) on each node, perhaps calling it in parallel across nodes using a Spark *map()*. Likewise, it is common for machine learning pipelines to require training the same algorithm on a small dataset with many configurations of parameters, in order to choose the best one. You can achieve this in Spark by using *parallelize()* over your list of parameters to train different ones on different nodes, again using a single-node learning library on each node. But MLlib itself shines when you have a large, distributed dataset that you need to train a model on.

### 11.2 System Requirements

### 11.3 Machine Learning Basics

To put the functions in MLlib in context, we’ll start with a brief review of machine learning concepts.

Machine learning algorithms attempt to make predictions or decisions based on training data, often maximizing a mathematical objective about how the algorithm should behave. There are multiple types of learning problems, including classification, regression, or clustering, which have different objectives. 

All learning algorithms require defining a set of features for each item, which will be fed into the learning function. 

Most algorithms are defined only for numerical features (specifically, a vector of numbers representing the value for each feature), so often *an important step is feature extraction and transformation to produce these feature vectors*. 

Once data is represented as feature vectors, most machine learning algorithms optimize a well-defined mathematical function based on these vectors. 

![learning-spark-1-16.png](../images/learning-spark-1-16.png)

Finally, most learning algorithms have multiple parameters that can affect results, so real-world pipelines will train multiple versions of a model and evaluate each one. To do this, it is common to separate the input data into “training” and “test” sets, and train only on the former, so that the test set can be used to see whether the model overfit the training data. MLlib provides several algorithms for model evaluation.


#### 11.3.1 Example: Spam Classification

A spam classification in python.

{% highlight python %}

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import LogisticRegressionWithSGD

spam = sc.textFile("spam.txt")
normal = sc.textFile("normal.txt")

# Create a HashingTF instance to map email text to vectors of 10,000 features.
tf = HashingTF(numFeatures = 10000)
# Each email is split into words, and each word is mapped to one feature.
spamFeatures = spam.map(lambda email: tf.transform(email.split(" ")))
normalFeatures = normal.map(lambda email: tf.transform(email.split(" ")))

# Create LabeledPoint datasets for positive (spam) and negative (normal) examples.
positiveExamples = spamFeatures.map(lambda features: LabeledPoint(1, features))
negativeExamples = normalFeatures.map(lambda features: LabeledPoint(0, features))
trainingData = positiveExamples.union(negativeExamples)
trainingData.cache() # Cache since Logistic Regression is an iterative algorithm.

# Run Logistic Regression using the SGD algorithm.
model = LogisticRegressionWithSGD.train(trainingData)

# Test on a positive example (spam) and a negative one (normal). We first apply
# the same HashingTF feature transformation to get vectors, then apply the model.
posTest = tf.transform("O M G GET cheap stuff by sending money to ...".split(" "))
negTest = tf.transform("Hi Dad, I started studying Spark the other ...".split(" "))
print "Prediction for positive test example: %g" % model.predict(posTest)
print "Prediction for negative test example: %g" % model.predict(negTest)

{% endhighlight %}


### 11.4 Data Types

MLlib contains a few specific data types, located in the *org.apache.spark.mllib package (Java/Scala) or pyspark.mllib (Python)*. The main ones are:

*Vector*

>>
A mathematical vector. MLlib supports both dense vectors, where every entry is stored, and sparse vectors, where only the nonzero entries are stored to save space. We will discuss the different types of vectors shortly. Vectors can be constructed with the *mllib.linalg.Vectors* class.

*LabeledPoint*

>>
A labeled data point for supervised learning algorithms such as classification and regression. Includes a feature vector and a label (which is a floating-point value). Located in the *mllib.regression* package.

*Rating*

>>
A rating of a product by a user, used in the *mllib.recommendation* package for product recommendation.

*Various Model classes*

>>
Each Model is the result of a training algorithm, and typically has a *predict()* method for applying the model to a new data point or to an RDD of new data points.

Most algorithms work directly on RDDs of Vectors, LabeledPoints, or Ratings. You can construct these objects however you want, but typically you will build an RDD through transformations on external data—for example, by loading a text file or running a Spark SQL command—and then apply a *map()* to turn your data objects into MLlib types.

### 11.5 Working with Vectors

There are a few points to note for the Vector class in MLlib, which will be the most commonly used one.

First, vectors come in two flavors: dense and sparse. Dense vectors store all their entries in an array of floating-point numbers. For example, a vector of size 100 will contain 100 double values. In contrast, sparse vectors store only the nonzero values and their indices. Sparse vectors are usually preferable (both in terms of memory use and speed) if at most 10% of elements are nonzero. Many featurization techniques yield very sparse vectors, so using this representation is often a key optimization.

Second, the ways to construct vectors vary a bit by language. In Python, you can simply pass a NumPy array anywhere in MLlib to represent a dense vector, or use the *mllib.linalg.Vectors* class to build vectors of other types. In Java and Scala, use the *mllib.linalg.Vectors* class.


### 11.6 Algorithms

In this section, we’ll cover the key algorithms available in MLlib, as well as their input and output types. We do not have space to explain each algorithm mathematically, but focus instead on how to call and configure these algorithms.

#### 11.6.1 Feature Extraction

The *mllib.feature* package contains several classes for common feature transformations. These include algorithms to construct feature vectors from text (or from other tokens), and ways to normalize and scale features.

#### 11.6.2 TF-IDF

*Term Frequency–Inverse Document Frequency*, or TF-IDF, is a simple way to generate feature vectors from text documents. It computes two statistics for each term in each document: 

- the term frequency (TF), which is the number of times the term occurs in that document
- the inverse document frequency (IDF), which measures how (in)frequently a term occurs across the whole document corpus. 

The product of these values, *TF * IDF*, shows how relevant a term is to a specific document (i.e., if it is common in that document but rare in the whole corpus).

MLlib has two algorithms that compute TF-IDF: *HashingTF and IDF*, both in the *mllib.feature* package. HashingTF computes a term frequency vector of a given size from a document. In order to map terms to vector indices, it uses a technique known as the hashing trick. Within a language like English, there are hundreds of thousands of words, so tracking a distinct mapping from each word to an index in the vector would be expensive. Instead, HashingTF takes the hash code of each word modulo a desired vector size, S, and thus maps each word to a number between 0 and S–1. This always yields an S-dimensional vector, and in practice is quite robust even if multiple words map to the same hash code. The MLlib developers recommend setting S between 2^18 and 2^20.

HashingTF can run either on one document at a time or on a whole RDD. It requires each “document” to be represented as an iterable sequence of objects, for instance, a list in Python or a Collection in Java. 

{% highlight python %}

>>> from pyspark.mllib.feature import HashingTF

>>> sentence = "hello hello world"
>>> words = sentence.split()  # Split sentence into a list of terms
>>> tf = HashingTF(10000)  # Create vectors of size S = 10,000
>>> tf.transform(words)
SparseVector(10000, {3065: 1.0, 6861: 2.0})

>>> rdd = sc.wholeTextFiles("data").map(lambda (name, text): text.split())
>>> tfVectors = tf.transform(rdd)   # Transforms an entire RDD

{% endhighlight %}

tips: 

>>
In a real pipeline, you will likely need to preprocess and stem words in a document before passing them to TF. For example, you might convert all words to lowercase, drop punctuation characters, and drop suffixes like ing. For best results you can call a single-node natural language library like NLTK in a map().

Once you have built term frequency vectors, you can use IDF to compute the inverse document frequencies, and multiply them with the term frequencies to compute the TF-IDF. You first call *fit()* on an IDF object to obtain an IDFModel representing the inverse document frequencies in the corpus, then call *transform()* on the model to transform TF vectors into IDF vectors. 

{% highlight python %}

from pyspark.mllib.feature import HashingTF, IDF

# Read a set of text files as TF vectors
rdd = sc.wholeTextFiles("data").map(lambda (name, text): text.split())
tf = HashingTF()
tfVectors = tf.transform(rdd).cache()

# Compute the IDF, then the TF-IDF vectors
idf = IDF()
idfModel = idf.fit(tfVectors)
tfIdfVectors = idfModel.transform(tfVectors)

{% endhighlight %}


#### 11.6.3 SCALING

Most machine learning algorithms consider the magnitude of each element in the feature vector, and thus work best when the features are scaled so they weigh equally (e.g., all features have a mean of 0 and standard deviation of 1). Once you have built feature vectors, you can use the *StandardScaler* class in MLlib to do this scaling, both for the mean and the standard deviation. You create a *StandardScaler*, call *fit()* on a dataset to obtain a StandardScalerModel (i.e., compute the mean and variance of each column), and then call *transform()* on the model to scale a dataset.

{% highlight python %}

from pyspark.mllib.feature import StandardScaler

vectors = [Vectors.dense([-2.0, 5.0, 1.0]), Vectors.dense([2.0, 0.0, 1.0])]
dataset = sc.parallelize(vectors)
scaler = StandardScaler(withMean=True, withStd=True)
model = scaler.fit(dataset)
result = model.transform(dataset)

# Result: {[-0.7071, 0.7071, 0.0], [0.7071, -0.7071, 0.0]}

{% endhighlight %}

#### 11.6.4 NORMALIZATION

In some situations, normalizing vectors to length 1 is also useful to prepare input data. The Normalizer class allows this. Simply use *Normalizer().transform(rdd)*. By default Normalizer uses the L^2 norm (i.e, Euclidean length), but you can also pass a power p to Normalizer to use the L^p norm.

#### 11.6.5 WORD2VEC

*Word2Vec* is a featurization algorithm for text based on neural networks that can be used to feed data into many downstream algorithms. Spark includes an implementation of it in the *mllib.feature.Word2Vec* class.

To train Word2Vec, you need to pass it a corpus of documents, represented as Iterables of Strings (one per word). Much like in “TF-IDF”, it is recommended to normalize your words (e.g., mapping them to lowercase and removing punctuation and numbers). Once you have trained the model (with *Word2Vec.fit(rdd)*), you will receive a Word2VecModel that can be used to *transform()* each word into a vector. Note that the size of the models in Word2Vec will be equal to the number of words in your vocabulary times the size of a vector (by default, 100). You may wish to filter out words that are not in a standard dictionary to limit the size. In general, a good size for the vocabulary is 100,000 words.

#### 11.6.6 Statistics

Basic statistics are an important part of data analysis, both in ad hoc exploration and understanding data for machine learning. MLlib offers several widely used statistic functions that work directly on RDDs, through methods in the *mllib.stat.Statistics* class. Some commonly used ones include:

*Statistics.colStats(rdd)*

>>
Computes a statistical summary of an RDD of vectors, which stores the min, max, mean, and variance for each column in the set of vectors. This can be used to obtain a wide variety of statistics in one pass.

*Statistics.corr(rdd, method)*

>>
Computes the correlation matrix between columns in an RDD of vectors, using either the Pearson or Spearman correlation (method must be one of pearson and spearman).

*Statistics.corr(rdd1, rdd2, method)*

>>
Computes the correlation between two RDDs of floating-point values, using either the Pearson or Spearman correlation (method must be one of pearson and spearman).

*Statistics.chiSqTest(rdd)*

>>
Computes Pearson’s independence test for every feature with the label on an RDD of LabeledPoint objects. Returns an array of ChiSqTestResult objects that capture the p-value, test statistic, and degrees of freedom for each feature. Label and feature values must be categorical (i.e., discrete values).

Apart from these methods, RDDs containing numeric data offer several basic statistics such as *mean(), stdev(), and sum()*, as described in “Numeric RDD Operations”. In addition, RDDs support sample() and sampleByKey() to build simple and stratified samples of data.

#### 11.6.7 Classification and Regression

Classification and regression are two common forms of supervised learning, where algorithms attempt to predict a variable from features of objects using labeled training data. The difference between them is the type of variable predicted: in classification, the variable is discrete; In regression, the variable predicted is continuous.

Both classification and regression use the *LabeledPoint* class in MLlib, described in “Data Types”, which resides in the *mllib.regression* package. A LabeledPoint consists simply of a label and a features vector.

#### 11.6.8 Linear Regression

Linear regression is one of the most common methods for regression, predicting the output variable as a linear combination of the features. MLlib also supports Lasso and ridge regression.

The linear regression algorithms are available through the *mllib.regression.LinearRegressionWithSGD, LassoWithSGD, and RidgeRegressionWithSGD* classes. These follow a common naming pattern throughout MLlib, where problems involving multiple algorithms have a “With” part in the class name to specify the algorithm used. Here, SGD is Stochastic Gradient Descent.

These classes all have several parameters to tune the algorithm:

- numIterations

>>
Number of iterations to run (default: 100).

- stepSize

>>
Step size for gradient descent (default: 1.0).

- intercept

>>
Whether to add an intercept or bias feature to the data—that is, another feature whose value is always 1 (default: false).

- regParam

>>
Regularization parameter for Lasso and ridge (default: 1.0).

{% highlight python %}

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import LinearRegressionWithSGD

points = # (create RDD of LabeledPoint)
model = LinearRegressionWithSGD.train(points, iterations=200, intercept=True)
print "weights: %s, intercept: %s" % (model.weights, model.intercept)

{% endhighlight %}

Once trained, the *LinearRegressionModel* returned in all languages includes a *predict()* function that can be used to predict a value on a single vector. The *RidgeRegressionWithSGD and LassoWithSGD* classes behave similarly and return a similar model class. Indeed, this pattern of an algorithm with parameters adjusted through setters, which returns a Model object with a *predict()* method, is common in all of MLlib.


#### 11.6.9 Logistic Regression

Logistic regression is a *binary classification* method that identifies a linear separating plane between positive and negative examples. In MLlib, it takes *LabeledPoints* with label 0 or 1 and returns a *LogisticRegressionModel* that can predict new points.

The logistic regression algorithm has a very similar API to linear regression, covered in the previous section. One difference is that there are two algorithms available for solving it: *SGD and LBFGS.20 LBFGS* is generally the best choice, but is not available in some earlier versions of MLlib (before Spark 1.2). These algorithms are available in the *mllib.classification.LogisticRegressionWithLBFGS and WithSGD* classes, which have interfaces similar to LinearRegressionWithSGD. They take all the same parameters as linear regression (see the previous section).

The *LogisticRegressionModel* from these algorithms computes a score between 0 and 1 for each point, as returned by the logistic function. It then returns either 0 or 1 based on a threshold that can be set by the user: by default, if the score is at least 0.5, it will return 1. You can change this threshold via *setThreshold()*. You can also disable it altogether via *clearThreshold()*, in which case *predict()* will return the raw scores. For balanced datasets with about the same number of positive and negative examples, we recommend leaving the threshold at 0.5. For imbalanced datasets, you can increase the threshold to drive down the number of false positives (i.e., increase precision but decrease recall), or you can decrease the threshold to drive down the number of false negatives.

#### 11.6.10 Support Vector Machines

Support Vector Machines, or SVMs, are another binary classification method with linear separating planes, again expecting labels of 0 or 1. They are available through the *SVMWithSGD* class, with similar parameters to linear and logisitic regression. The returned SVMModel uses a threshold for prediction like *LogisticRegressionModel*.

#### 11.6.11 Naive Bayes

Naive Bayes is a multiclass classification algorithm that scores how well each point belongs in each class based on a linear function of the features. It is commonly used in text classification with TF-IDF features, among other applications. MLlib implements Multinomial Naive Bayes, which expects nonnegative frequencies (e.g., word frequencies) as input features.

In MLlib, you can use Naive Bayes through the *mllib.classification.NaiveBayes* class. It supports one parameter, lambda (or lambda_ in Python), used for smoothing. You can call it on an RDD of LabeledPoints, where the labels are between 0 and C–1 for C classes.

The returned NaiveBayesModel lets you *predict()* the class in which a point best belongs, as well as access the two parameters of the trained model: theta, the matrix of class probabilities for each feature (of size C*D for C classes and D features), and pi, the C-dimensional vector of class priors.

#### 11.6.12 Decision Trees and Random Forests

Decision trees are a flexible model that can be used for both classification and regression. They represent a tree of nodes, each of which makes a binary decision based on a feature of the data, and where the leaf nodes in the tree contain a prediction. Decision trees are attractive because the models are easy to inspect and because they support both categorical and continuous features.

In MLlib, you can train trees using the *mllib.tree.DecisionTree* class, through the static methods *trainClassifier() and trainRegressor()*. Unlike in some of the other algorithms, the Java and Scala APIs also use static methods instead of a DecisionTree object with setters. The training methods take the following parameters:

- data

>>
RDD of LabeledPoint.

- numClasses (classification only)

>>
Number of classes to use.

- impurity

>>
Node impurity measure; can be gini or entropy for classification, and must be variance for regression.

- maxDepth

>>
Maximum depth of tree (default: 5).

- maxBins

>>
Number of bins to split data into when building each node (suggested value: 32).

- categoricalFeaturesInfo

>>
A map specifying which features are categorical, and how many categories they each have. For example, if feature 1 is a binary feature with labels 0 and 1, and feature 2 is a three-valued feature with values 0, 1, and 2, you would pass {1: 2, 2: 3}. Use an empty map if no features are categorical.

The online MLlib documentation contains a detailed explanation of the algorithm used. The cost of the algorithm scales linearly with the number of training examples, number of features, and maxBins. For large datasets, you may wish to lower maxBins to train a model faster, though this will also decrease quality.

The *train()* methods return a *DecisionTreeModel*. You can use it to predict values for a new feature vector or an RDD of vectors via *predict()*, or print the tree using *toDebugString()*. This object is serializable, so you can save it using Java Serialization and load it in another program.

Finally, in Spark 1.2, MLlib adds an experimental RandomForest class in Java and Scala to build ensembles of trees, also known as random forests. It is available through *RandomForest.trainClassifier and trainRegressor*. Apart from the per-tree parameters just listed, RandomForest takes the following parameters:

- numTrees

>>
How many trees to build. Increasing numTrees decreases the likelihood of overfitting on training data.

- featureSubsetStrategy

>>
Number of features to consider for splits at each node; can be auto (let the library select it), all, sqrt, log2, or onethird; larger values are more expensive.

- seed

>>
Random-number seed to use.

Random forests return a *WeightedEnsembleModel* that contains several trees (in the weakHypotheses field, weighted by weakHypothesisWeights) and can *predict()* an RDD or Vector. It also includes a toDebugString to print all the trees.


#### 11.6.13 Clustering

Clustering is the unsupervised learning task that involves grouping objects into clusters of high similarity. Unlike the supervised tasks seen before, where data is labeled, clustering can be used to make sense of unlabeled data. It is commonly used in data exploration (to find what a new dataset looks like) and in anomaly detection (to identify points that are far from any cluster).

#### 11.6.14 K-MEANS

MLlib includes the popular K-means algorithm for clustering, as well as a variant called K-means, that provides better initialization in parallel environments. K-means is similar to the K-means++ initialization procedure often used in single-node settings.

The most important parameter in K-means is a target number of clusters to generate, K. In practice, you rarely know the “true” number of clusters in advance, so the best practice is to try several values of K, until the average intracluster distance stops decreasing dramatically. However, the algorithm takes only one K at a time. Apart from K, K-means in MLlib takes the following parameters:

- initializationMode

>>
The method to initialize cluster centers, which can be either “k-means||” or “random”; k-means|| (the default) generally leads to better results but is slightly more expensive.

- maxIterations

>>
Maximum number of iterations to run (default: 100).

- runs

>>
Number of concurrent runs of the algorithm to execute. MLlib’s K-means supports running from multiple starting positions concurrently and picking the best result, which is a good way to get a better overall model (as K-means runs can stop in local minima).

Like other algorithms, you invoke K-means by creating a *mllib.clustering.KMeans* object (in Java/Scala) or calling *KMeans.train* (in Python). It takes an RDD of Vectors. K-means returns a KMeansModel that lets you access the clusterCenters (as an array of vectors) or call *predict()* on a new vector to return its cluster. Note that *predict()* always returns the closest center to a point, even if the point is far from all clusters.


#### 11.6.15 Collaborative Filtering and Recommendation

Collaborative filtering is a technique for recommender systems wherein users’ ratings and interactions with various products are used to recommend new ones. Collaborative filtering is attractive because it only needs to take in a list of user/product interactions: either “explicit” interactions (i.e., ratings on a shopping site) or “implicit” ones (e.g., a user browsed a product page but did not rate the product). Based solely on these interactions, collaborative filtering algorithms learn which products are similar to each other (because the same users interact with them) and which users are similar to each other, and can make new recommendations.

While the MLlib API talks about “users” and “products,” you can also use collaborative filtering for other applications, such as recommending users to follow on a social network, tags to add to an article, or songs to add to a radio station.

#### 11.6.16 Alternating Least Squares

MLlib includes an implementation of Alternating Least Squares (ALS), a popular algorithm for collaborative filtering that scales well on clusters. It is located in the *mllib.recommendation.ALS* class.

ALS works by determining a feature vector for each user and product, such that the dot product of a user’s vector and a product’s is close to their score. It takes the following parameters:

- rank

>>
Size of feature vectors to use; larger ranks can lead to better models but are more expensive to compute (default: 10).

- iterations

>>
Number of iterations to run (default: 10).

- lambda

>>
Regularization parameter (default: 0.01).

- alpha

>>
A constant used for computing confidence in implicit ALS (default: 1.0).

- numUserBlocks, numProductBlocks

>>
Number of blocks to divide user and product data in, to control parallelism; you can pass –1 to let MLlib automatically determine this (the default behavior).

To use ALS, you need to give it an RDD of *mllib.recommendation.Rating* objects, each of which contains a user ID, a product ID, and a rating (either an explicit rating or implicit feedback; see upcoming discussion). One challenge with the implementation is that each ID needs to be a 32-bit integer. If your IDs are strings or larger numbers, it is recommended to just use the hash code of each ID in ALS; even if two users or products map to the same ID, overall results can still be good. Alternatively, you can *broadcast()* a table of product-ID-to-integer mappings to give them unique IDs.

ALS returns a *MatrixFactorizationModel* representing its results, which can be used to *predict()* ratings for an RDD of (userID, productID) pairs. Alternatively, you can use *model.recommendProducts(userId, numProducts)* to find the top *numProducts()* products recommended for a given user. Note that unlike other models in MLlib, the *MatrixFactorizationModel* is large, holding one vector for each user and product. This means that it cannot be saved to disk and then loaded back in another run of your program. Instead, you can save the RDDs of feature vectors produced in it, *model.userFeatures and model.productFeatures*, to a distributed filesystem.

Finally, there are two variants of ALS: for explicit ratings (the default) and for implicit ratings (which you enable by calling *ALS.trainImplicit() instead of ALS.train()*). With explicit ratings, each user’s rating for a product needs to be a score (e.g., 1 to 5 stars), and the predicted ratings will be scores. With implicit feedback, each rating represents a confidence that users will interact with a given item (e.g., the rating might go up the more times a user visits a web page), and the predicted items will be confidence values. Further details about ALS with implicit ratings are described in Hu et al., “Collaborative Filtering for Implicit Feedback Datasets,” ICDM 2008.

#### 11.6.17 Principal Component Analysis

Given a dataset of points in a high-dimensional space, we are often interested in reducing the dimensionality of the points so that they can be analyzed with simpler tools. 

The main technique for dimensionality reduction used by the machine learning community is *principal component analysis (PCA)*. In this technique, the mapping to the lower-dimensional space is done such that the variance of the data in the low-dimensional representation is maximized, thus ignoring noninformative dimensions. To compute the mapping, the normalized correlation matrix of the data is constructed and the singular vectors and values of this matrix are used. The singular vectors that correspond to the largest singular values are used to reconstruct a large fraction of the variance of the original data.

PCA is currently available only in Java and Scala (as of MLlib 1.2). To invoke it, you must first represent your matrix using the *mllib.linalg.distributed.RowMatrix* class, which stores an RDD of Vectors, one per row.24 You can then call PCA as shown bellow:

{% highlight scala %}

import org.apache.spark.mllib.linalg.Matrix
import org.apache.spark.mllib.linalg.distributed.RowMatrix

val points: RDD[Vector] = // ...
val mat: RowMatrix = new RowMatrix(points)
val pc: Matrix = mat.computePrincipalComponents(2)

// Project points to low-dimensional space
val projected = mat.multiply(pc).rows

// Train a k-means model on the projected 2-dimensional data
val model = KMeans.train(projected, 10)

{% endhighlight %}

#### 11.6.18 Model Evaluation

No matter what algorithm is used for a machine learning task, model evaluation is an important part of end-to-end machine learning pipelines. Many learning tasks can be tackled with different models, and even for the same algorithm, parameter settings can lead to different results. Moreover, there is always a risk of overfitting a model to the training data, which you can best evaluate by testing the model on a different dataset than the training data.

At the time of writing (for Spark 1.2), MLlib contains an experimental set of model evaluation functions, though only in Java and Scala. These are available in the *mllib.evaluation* package, in classes such as *BinaryClassificationMetrics and MulticlassMetrics*, depending on the problem. For these classes, you can create a Metrics object from an RDD of (prediction, ground truth) pairs, and then compute metrics such as precision, recall, and area under the receiver operating characteristic (ROC) curve. These methods should be run on a test dataset not used for training (e.g., by leaving out 20% of the data before training). You can apply your model to the test dataset in a map() function to build the RDD of (prediction, ground truth) pairs.

### 11.7 Tips and Performance Considerations

#### 11.7.1 Preparing Features

While machine learning presentations often put significant emphasis on the algorithms used, it is important to remember that in practice, each algorithm is only as good as the features you put into it! Many large-scale learning practitioners agree that feature preparation is the most important step to large-scale learning. Both adding more informative features (e.g., joining with other datasets to bring in more information) and converting the available features to suitable vector representations (e.g., scaling the vectors) can yield major improvements in results.

A full discussion of feature preparation is beyond the scope of this book, but we encourage you to refer to other texts on machine learning for more information. However, with MLlib in particular, some common tips to follow are:

- Scale your input features. Run features through StandardScaler as described in “Scaling” to weigh features equally.
- Featurize text correctly. Use an external library like NLTK to stem words, and use IDF across a representative corpus for TF-IDF.
- Label classes correctly. MLlib requires class labels to be 0 to C–1, where C is the total number of classes.


#### 11.7.2 Configuring Algorithms

Most algorithms in MLlib perform better (in terms of prediction accuracy) with regularization when that option is available. Also, most of the SGD-based algorithms require around 100 iterations to get good results. MLlib attempts to provide useful default values, but you should try increasing the number of iterations past the default to see whether it improves accuracy. 

#### 11.7.3 Caching RDDs to Reuse

Most algorithms in MLlib are iterative, going over the data multiple times. Thus, it is important to *cache()* your input datasets before passing them to MLlib. Even if your data does not fit in memory, try *persist(StorageLevel.DISK_ONLY)*.

*In Python, MLlib automatically caches RDDs on the Java side when you pass them from Python*, so there is no need to cache your Python RDDs unless you reuse them within your program. In Scala and Java, however, it is up to you to cache them.

#### 11.7.3 Recognizing Sparsity

When your feature vectors contain mostly zeros, storing them in sparse format can result in huge time and space savings for big datasets. In terms of space, MLlib’s sparse representation is smaller than its dense one if at most two-thirds of the entries are nonzero. In terms of processing cost, sparse vectors are generally cheaper to compute on if at most 10% of the entries are nonzero. (This is because their representation requires more instructions per vector element than dense vectors.) But if going to a sparse representation is the difference between being able to cache your vectors in memory and not, you should consider a sparse representation even for denser data.

#### 11.7.4 Level of Parallelism

For most algorithms, you should have at least as many partitions in your input RDD as the number of cores on your cluster to achieve full parallelism. Recall that Spark creates a partition for each “block” of a file by default, where a block is typically 64 MB. You can pass a minimum number of partitions to methods like *SparkContext.textFile()* to change this—for example, *sc.textFile("data.txt", 10)*. Alternatively, you can call *repartition(numPartitions)* on your RDD to partition it equally into numPartitions pieces. You can always see the number of partitions in each RDD on Spark’s web UI. At the same time, be careful with adding too many partitions, because this will increase the communication cost.


### 11.8 Pipeline API

Starting in Spark 1.2, MLlib is adding a new, higher-level API for machine learning, based on the concept of pipelines. This API is similar to the pipeline API in SciKit-Learn. In short, a pipeline is a series of algorithms (either feature transformation or model fitting) that transform a dataset. Each stage of the pipeline may have parameters (e.g., the number of iterations in LogisticRegression). The pipeline API can automatically search for the best set of parameters using a grid search, evaluating each set using an evaluation metric of choice.










## 参考文章

- [learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- [code of learning spark on github](https://github.com/databricks/learning-spark)
- [spark-summit](https://spark-summit.org/)
- [TF-IDF与余弦相似性的应用（一）：自动提取关键词](http://www.ruanyifeng.com/blog/2013/03/tf-idf.html)



