## kNN 

1. Pros: High accuracy, insensitive to outliers, no assumptions about data

2. Cons: Computationally expensive, requires a lot of memory

3. Works with: Numeric values, nominal values

4. general approach to kNN
   1. collect data
   2. prepare data, numeric values are needed for distance calculation
   3. analyse
   4. train
   5. test

5. core:

   1. distance algorithms: usually use Euclidian distance, or some weighted distance calculation, it's just like a similarity calculation.
   2. data preparation: when dealing with values that lie in different ranges, it's common to normalize them.

6. summary

   ```
   kNN is a simple and effective way to classify data. it's an example of instance-based learning, where you need to have instances of data close at hand to perform the algorithm. and it has to carry around the full dataset, for large datasets, it may imply a large amount of storage, and in addition, you need to calculate the distance measurement for every piece of data in the database.

   and additional drawback is that kNN doesn't give you any idea of the underlying structure of the data, you have no idea of what an "average" or "exemplar" instance from each class looks like. In the next chapter, we'll address this issue by exploring ways in which probability measurements can help you do classification.
   ```

   ​

## Decision trees

1. pros: computational cheap to use, easy for humans to understand, missing values ok, can deal with irrelevant features
2. cons: prone to overfitting
3. works with: Numeric values, nominal values
4. how to split a dataset will use something mathematic theory: ***information theory***
5. some decision trees make a binary split of the data, but if we split on an attribute and it has 4 possible values, then we'll split the data 4 ways and create 4 separate branches.
6. we'll follow the ***ID3 algorithm*** to tell us how to split the data and when to stop splitting.
7. the change in information before and after the split is known as the ***information gain***, when you know how the calculate the information gain, you can split your data across every feature to see which split gives you the highest information gain. the split with the highest information gain is your best option. before you can measure the best split and start splitting our data, you need to know how to calculate the information gain, the measure of information of a set is known as the ***shannon entropy**, or just ***entropy*** for short.
8. ***entropy*** is defined as the expected value of the information, and we need first to define information. if we're classifying something that can take on multiple values, the information for symbol $x_i^{}$ is defined as : $l(x_i^{}) = log_2^{} P(x_i^{})$ , where $P(x_i^{})$ is the probability of choosing this class. to calculate entropy, you need the expected value of all the information of all possible values of our class, this is given by: $$ H = - \sum_{i=1}^{n} P(x_i^{}) * log_2^{} P(x_i^{}) $$ , where n is the number of class. and the higher the entropy, the more mixed up the data is. So entropy is kind of a thing to measure the amount of disorder in a dataset. for decision tree, we need to measure the entropy, split the dataset, measure the entropy on the split sets, and see if splitting it was the right thing to do. and we'll do this for all our features to determine the best feature to split on.
9. summary


```
A decision tree classifier is just like a work-flow diagram with the terminating blocks representing classification decisions. Start with a dataset, you can measure the inconsistency of a set or the entropy to find a way to split the set until all the data belongs to the same class. The ID3 algorithm can split nominal-valued datasets. recursion is used in tree-building algorithms to turn a dataset into a decision tree. And there are other decision tree-generating algorithms. the most popular are C4.5 and CART, CART will be addressed later when we talk aboug regression.
```



## Naive Bayes

1. pros: works with a small amount of data, handles multiple classes
2. cons: sensitive to how the input data is prepared
3. works with: nominal values, it's a popular algorithm for the document-classification problem.
4. Bayesian decision theory in a nutshell: choosing the decision with the highest probability.
5. conditional probability and bayes' rule: $$P(c | x) = \frac {P(x | c) P(c)} {P(x)}$$
6. ***not understand deeply enough, need read cn-version and do a practice, and the key point is do the modeling, and optimize the probability calculation***
7. summary:


```
using probabilities can sometimes be more effective than using hard rules for classification, bayes probability and bayes rule gives us a way to estimate unknown probabilities from known values.
you can reduce the need for a lot of data by assuming conditional independence among the features in your data. the assumption we make is that the probability of one word doesn't depend on any other words in the document. we know this assumption is a little simple, so that's why it's known as naive bayes.
There are a number of practical considerations when implementing naive bayes in a modern programming language. underflow is one problem that can be addressed by using the logarithm of probabilities in your calculations. the bag-of-words model is an improvement on the set-of-words model when approaching document classification. and other improvements such as removing stop words, and you can spend a long time on optimizing a tokenizer.
```

8. code sample:

```python
# encoding=utf-8

from numpy import *
 
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
                  
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)
 
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec
 
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)              ### 训练集中数据条数
    numWords = len(trainMatrix[0])               ### 每一条训练数据中的特征数
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0
    p1Denom = 2.0                        #change to 2.0
    
    # import pdb; pdb.set_trace()
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()

    return p0Vect, p1Vect, pAbusive
 
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
     
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
 
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
 
def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 
     
def spamTest():
    docList = []
    classList = []
    fullText =[]
    
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    vocabList = createVocabList(docList)#create vocabulary

    trainingSet = range(50)
    testSet = []           #create test set
    
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  

    trainMat = []
    trainClasses = []
    
    for docIndex in trainingSet:    #train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])

    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    #return vocabList,fullText
 
def calcMostFreq(vocabList,fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]       
 
def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    top30Words = calcMostFreq(vocabList,fullText)   #remove top 30 words
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet=[]           #create test set
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V
 
def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]


if __name__ == '__main__':
    spamTest()
```
















## resources

- kaggle algorithms test
- ​




















