## Basic Concepts

- 机器学习 开发流程

  ```
  * 收集数据: 收集样本数据
  * 准备数据: 注意数据的格式
  * 分析数据: 为了确保数据集中没有垃圾数据；
      如果是算法可以处理的数据格式或可信任的数据源，则可以跳过该步骤；
      另外该步骤需要人工干预，会降低自动化系统的价值。
  * 训练算法: [机器学习算法核心]如果使用无监督学习算法，由于不存在目标变量值，则可以跳过该步骤
  * 测试算法: [机器学习算法核心]评估算法效果
  * 使用算法: 将机器学习算法转为应用程序
  ```




# Supurvised Learning






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



## Logistic Regression

- pros: computationally inexpensive, easy to implement, knowledge representation easy to interpret
- cons: prone to underfitting, may have low accuracy
- works with: numeric values, nominal values
- we'd like to have an equation we can give all of our features and it will predict the class. in the two-class case, the function will spit out a 0 or a 1, it's called ***Heaviside step function*** or just ***step function***, another function is much easier to deal with mathematically, is call ***sigmoid*** function, is given by: $$\sigma(z) = \frac{1}{1 + e_{}^{-z}}$$
- for the logistic regression classifier, we'll take our features and multiply each one by a weight and then add them up, then put the result into the sigmoid and we'll get a number between 0, and 1, anything above 0.5 will be classified as 1, and anything below 0.5 will be classified as 0. you can think of logistic regression as a probability estimate.
- ***gradient ascent***: the first optimization algorithm we're going to look at is gradient ascent. it's based on the idea that if we want to find the maximum point on a function, then the best way to move is in the direction of the gradient. we write the gradient with the symbol $ \triangledown $ and the gradient of a function $ f(x, y) $ is given as below:
  - $$ \triangledown f(x, y) = \left(\begin{array}{c} \frac{\partial f(x, y)} {\partial x}\\ \frac{\partial f(x, y)} {\partial y} \end{array}\right) $$
  - means we'll move in the x direction by amount of $ \frac {\partial f(x, y)} {\partial x} $ , and y in the direction of another. this is the direction to which we should move, and for the magnitude or step size, we have a parameter $ \alpha $ to represent. so the gradient ascent algorithm is given as: $ w := w + \alpha * \triangledown_{w}^{} * f(w) $. this step is repeated until we reach a stopping condition: either a specified number of steps or the algorithm is within a certain tolerance margin.
- ***gradient descent***  is the same to the gradient ascent, except that we're trying to minimize some function rather than maximize it. 
- ***stochastic gradient ascent***: gradient ascent is computational expensive, an alternative way to this method is to update the weights using only one instance at a time, which is stochastic gradient, and its an online learning algorithm, because we can incrementally update the classifier as new data comes in rather than all at once. the all-at-once method is known as batch processing.
- one way to look at how well the optimization algorithm is doing is to see if it's converging, that is, are the parameters reaching a steady value or are they constantly changing.
- example:


```python
#!/usr/bin/python
# coding: utf8

'''
Created on Oct 27, 2010
Update  on 2017-05-18
Logistic Regression Working Module
@author: Peter Harrington/羊三/小瑶
《机器学习实战》更新地址：https://github.com/apachecn/MachineLearning
'''
from numpy import *
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 使用 Logistic 回归在简单数据集上的分类

# 解析数据
def loadDataSet(file_name):
    # dataMat为原始数据， labelMat为原始数据的标签
    dataMat = []; labelMat = []
    fr = open(file_name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        # 为了方便计算，我们将 X0 的值设为 1.0 ，也就是在每一行的开头添加一个 1.0 作为 X0
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

# sigmoid跳跃函数
def sigmoid(inX):
    return 1.0/(1+exp(-inX))


# 正常的处理方案
# 两个参数：第一个参数==> dataMatIn 是一个2维NumPy数组，每列分别代表每个不同的特征，每行则代表每个训练样本。
# 第二个参数==> classLabels 是类别标签，它是一个 1*100 的行向量。为了便于矩阵计算，需要将该行向量转换为列向量，做法是将原向量转置，再将它赋值给labelMat。
def gradAscent(dataMatIn, classLabels):
    # 转化为矩阵[[1,1,2],[1,1,2]....]
    dataMatrix = mat(dataMatIn)             # 转换为 NumPy 矩阵
    # 转化为矩阵[[0,1,0,1,0,1.....]]，并转制[[0],[1],[0].....]
    # transpose() 行列转置函数
    # 将行向量转化为列向量   =>  矩阵的转置
    labelMat = mat(classLabels).transpose() # 首先将数组转换为 NumPy 矩阵，然后再将行向量转置为列向量
    # m->数据量，样本数 n->特征数
    m,n = shape(dataMatrix)
    # print m, n, '__'*10, shape(dataMatrix.transpose()), '__'*100
    # alpha代表向目标移动的步长
    alpha = 0.001
    # 迭代次数
    maxCycles = 500
    # 生成一个长度和特征数相同的矩阵，此处n为3 -> [[1],[1],[1]]
    # weights 代表回归系数， 此处的 ones((n,1)) 创建一个长度和特征数相同的矩阵，其中的数全部都是 1
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        # m*3 的矩阵 * 3*1 的单位矩阵 ＝ m*1的矩阵
        # 那么乘上单位矩阵的意义，就代表：通过公式得到的理论值
        # 参考地址： 矩阵乘法的本质是什么？ https://www.zhihu.com/question/21351965/answer/31050145
        # print 'dataMatrix====', dataMatrix 
        # print 'weights====', weights
        # n*3   *  3*1  = n*1
        h = sigmoid(dataMatrix*weights)     # 矩阵乘法
        # print 'hhhhhhh====', h
        # labelMat是实际值
        error = (labelMat - h)              # 向量相减
        # 0.001* (3*m)*(m*1) 表示在每一个列上的一个误差情况，最后得出 x1,x2,xn的系数的偏移量
        weights = weights + alpha * dataMatrix.transpose() * error # 矩阵乘法，最后得到回归系数
    return array(weights)


# 随机梯度上升
# 梯度上升优化算法在每次更新数据集时都需要遍历整个数据集，计算复杂都较高
# 随机梯度上升一次只用一个样本点来更新回归系数
def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    # n*1的矩阵
    # 函数ones创建一个全1的数组
    weights = ones(n)   # 初始化长度为n的数组，元素全部为 1
    for i in range(m):
        # sum(dataMatrix[i]*weights)为了求 f(x)的值， f(x)=a1*x1+b2*x2+..+nn*xn,此处求出的 h 是一个具体的数值，而不是一个矩阵
        h = sigmoid(sum(dataMatrix[i]*weights))
        # print 'dataMatrix[i]===', dataMatrix[i]
        # 计算真实类别与预测类别之间的差值，然后按照该差值调整回归系数
        error = classLabels[i] - h
        # 0.01*(1*1)*(1*n)
        print weights, "*"*10 , dataMatrix[i], "*"*10 , error
        weights = weights + alpha * error * dataMatrix[i]
    return weights


# 随机梯度上升算法（随机化）
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   # 创建与列数相同的矩阵的系数矩阵，所有的元素都是1
    # 随机梯度, 循环150,观察是否收敛
    for j in range(numIter):
        # [0, 1, 2 .. m-1]
        dataIndex = range(m)
        for i in range(m):
            # i和j的不断增大，导致alpha的值不断减少，但是不为0
            alpha = 4/(1.0+j+i)+0.0001    # alpha 会随着迭代不断减小，但永远不会减小到0，因为后边还有一个常数项0.0001
            # 随机产生一个 0～len()之间的一个值
            # random.uniform(x, y) 方法将随机生成下一个实数，它在[x,y]范围内,x是这个范围内的最小值，y是这个范围内的最大值。
            randIndex = int(random.uniform(0,len(dataIndex)))
            # sum(dataMatrix[i]*weights)为了求 f(x)的值， f(x)=a1*x1+b2*x2+..+nn*xn
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            # print weights, '__h=%s' % h, '__'*20, alpha, '__'*20, error, '__'*20, dataMatrix[randIndex]
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights


# 可视化展示
def plotBestFit(dataArr, labelMat, weights):
    '''
        Desc:
            将我们得到的数据可视化展示出来
        Args:
            dataArr:样本数据的特征
            labelMat:样本数据的类别标签，即目标变量
            weights:回归系数
        Returns:
            None
    '''
    
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    """
    y的由来，卧槽，是不是没看懂？
    首先理论上是这个样子的。
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    w0*x0+w1*x1+w2*x2=f(x)
    x0最开始就设置为1叻， x2就是我们画图的y值，而f(x)被我们磨合误差给算到w0,w1,w2身上去了
    所以： w0+w1*x+w2*y=0 => y = (-w0-w1*x)/w2   
    """
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X'); plt.ylabel('Y')
    plt.show()


def simpleTest():
    # 1.收集并准备数据
    dataMat, labelMat = loadDataSet("input/5.Logistic/TestSet.txt")

    # print dataMat, '---\n', labelMat
    # 2.训练模型，  f(x)=a1*x1+b2*x2+..+nn*xn中 (a1,b2, .., nn).T的矩阵值
    # 因为数组没有是复制n份， array的乘法就是乘法
    dataArr = array(dataMat)
    # print dataArr
    weights = gradAscent(dataArr, labelMat)
    # weights = stocGradAscent0(dataArr, labelMat)
    # weights = stocGradAscent1(dataArr, labelMat)
    # print '*'*30, weights

    # 数据可视化
    plotBestFit(dataArr, labelMat, weights)


#--------------------------------------------------------------------------------
# 从疝气病症预测病马的死亡率

# 分类函数，根据回归系数和特征向量来计算 Sigmoid的值
def classifyVector(inX, weights):
    '''
    Desc: 
        最终的分类函数，根据回归系数和特征向量来计算 Sigmoid 的值，大于0.5函数返回1，否则返回0
    Args:
        inX -- 特征向量，features
        weights -- 根据梯度下降/随机梯度下降 计算得到的回归系数
    Returns:
        如果 prob 计算大于 0.5 函数返回 1
        否则返回 0
    '''
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

# 打开测试集和训练集,并对数据进行格式化处理
def colicTest():
    '''
    Desc:
        打开测试集和训练集，并对数据进行格式化处理
    Args:
        None
    Returns:
        errorRate -- 分类错误率
    '''
    frTrain = open('input/5.Logistic/horseColicTraining.txt')
    frTest = open('input/5.Logistic/horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    # 解析训练数据集中的数据特征和Labels
    # trainingSet 中存储训练数据集的特征，trainingLabels 存储训练数据集的样本对应的分类标签
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    # 使用 改进后的 随机梯度下降算法 求得在此数据集上的最佳回归系数 trainWeights
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    # 读取 测试数据集 进行测试，计算分类错误的样本条数和最终的错误率
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate


# 调用 colicTest() 10次并求结果的平均值
def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests)) 


if __name__ == "__main__":
    simpleTest()
    # multiTest()
```



- summary: logistic regression is finding best-fit parameters to a nonlinear function called the sigmoid. methods of optimization can be used to find the best-fit parameters, among the optimization algorithms, one of the most common algorithm is gradient ascent, which can be simplified with stochastic gradient ascent.




## SVM

- pros: low generalization error, computationally inexpensive, eay to interpret results;
- cons: sensitive to tuning parameters and kernel choice; natively only handles binary classification;
- works with: numeric values, nominal values
- If data points are separated enough that we can draw a straight line with all the points of one class on one side of the side and all the points of the other class on the other side of the line, if such a situation exists, we say the data is ***linearly separable***. and the line used to sparate the dataset is called a ***separating hyperplane***, in 2D plots, is's just a line. but if we have N dimensions data points, we need something N-1 dimensions to separate them. and the N-1 dimension is called a ***hyperplane***, it's the decision boundary. 
- We'd like to make our classifier in such a way that the farther a data point is from the decision boundary, the more confident we are about the prediction we've made. And we shouldn't use the minimizing the average distance to the separating hyperplane, cause it can not deal with situation bellow, which means B and C are better than D.
- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/3860076c-99da-11e7-95fa-0242ac140002)



- We'd like to find the point closest to the separating hyperplane and make sure this is as far away from the separating line as possible. this is known as ***margin***, we want to have the greatest possible margin, and the points closest to the separating hyperplane are known as ***support vectors [support: make the separating hyperplane confident, vectors: A N dimensions point, (x, y) in 2D plots]***. So now we know that we're trying to maximize the distance from the separating line the support vectors, we need to find a way to optimize this problem.
- if we want to find the distance from A to the separating plane, we must measure normal or perpendicular to the line, this is given by $\frac {|w_{}^{T} x + b|} {|w|} $, [frankly, I don't get this formula, google 点到直线的距离即可].
- [点到直线距离公式的几种推导](https://zhuanlan.zhihu.com/p/26307123)
- ​
- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/db3d1bde-99dd-11e7-9497-0242ac140002)
- For svm, the principles are a little hard to understand, I think we can start from ***learning to use to*** then to slowly find ***how it works***. we can learn from code: https://github.com/litaotao/MachineLearning , a very awesome repo.
- ***kernels***: is kind of a way for mapping data to higher dimensions. matchematicians like to call this ***mapping from one feature space to another feature space***, and this mapping goes from a lower-dimensional feature space to a higher-dimensions space, usually. if feature space sounds confusing, you can think of it as another distance metric.
- ***summary***: SVM are a type of classifier, they're called machines because they generate a binary decision, they're decision machines. ther're considered by some to be the best ***stock*** algorithm in unsupervised learning. svm try to maximize margin by solving a quadratic optimization problem. kernel methods or the kernel trick, map data from a low-dimensional space to a high-dimensional space, in a higher dimension, you can solve a linear problem that's nonlinear in lower-dimensional space.




## Adaboost

- concept: meta-algorithms, boosting, adaboost [ adaptive boosting].
- pros: low generalization error, easy to code, works with most classifiers, no parameters to adjust
- cons: sensitvie to outliers
- works with: numeric values, nominal values
- ​




## Predicting Numeric Values: Regression

- The difference between regression and classification is that in regression our target variable is numeric and continuous.
- Our goal when using regression is to predict a numeric target value, one way to do this is to write out an equation for the target vaue with respect to the inputs, that's known as ***regression equation***. and for the quation, there are two kinds: ***linear regression and non-linear regression***.
- our input data is in the matrix $X$, and regression weights in the vector $w$, for a given piece of data $X1$, our predicted value is given by $y1 = X_1^{T} * w$, we have the $Xs$ and $Ys$, but how can we find the $Ws$, one way is to find the $Ws$ which can minimize the error. and we define the error as the difference between predicted $y$ and the actual $Y$. using just the error will allow positive and negative values to cancel out, so we use the squared error, then write this as $\sum_{i=1}^m (y_i^{} - x_i^{T}w)_{}^{2}$ , and we can also wirte this in matrix notation as $(y-xw)_{}^{T} * (y-xw)$, if we take the derivative of this with respect to $w$, we'll get $X_{}^{T} * (y - Xw)$, and we can set this to zero and solve for $w$ to get the following equation: $\hat w = (X_{}^{T} * X)_{}^{-1} * X_{}^{T} * y$. 
- One way we can calculate how well the predicted data matches our actual data is with the correlation between the two series.
- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/a3a16466-9e7c-11e7-95fa-0242ac140002)


- Bellow the best-fit line does a great job of modeling the data as if it were a straight line. but it looks like the data has some patterns we may want to take advantage of. and one way we can do is called ***locally adjust forecast: 局部加权线性回归*** based on the data.

- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/1700c10c-9e8e-11e7-9497-0242ac140002)

- Linear regression tends to underfoot the data, and there are a number of ways to reduce the mean-squared error by adding some bias into our estimator. in LWLR we give a weight to data points near our data point of interest, then we compute a least-squares regression similar to above. This type of regression uses the dataset each time a calculation is needed, similar to kNN, the solution is now given by: $\hat w = (X_{}^{T} * X)_{}^{-1} * X_{}^{T} * W * y$, where $W$ is a matrix that's used to weight the data points.

- LWLR uses a kernel something like the kernels demonstrated in SVM to weight nearby points more heavily than other points. the most common kernel to use is a ***Gaussian***, the kernel assigns a weight given by: $w(i, i) = exp(\frac {\mid x_{}^{i} - x \mid} {-2k_{}^{2}})$, this builds the matrix $w$, which has only diagonal elements, the closer the data point x is to the other points, the larger w(i, i) will be, the $k$ will determine how much to weight nearby points.

- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/586c36c6-9e93-11e7-9497-0242ac140002)

- the core code of lwlr and the effection is bellow:

- ```python
  def lwlr(testPoint, xArr, yArr, k=1.0):
      xMat = mat(xArr)
      yMat = mat(yArr).T
      m = shape(xMat)[0]
      weights = mat(eye(m))
      
      for j in range(m):
          diffMat = testPoint - xMat[j, :]
          weights[j, j] = exp(diffMat * diffMat.T) / (-2.0 * k ** 2)
          
      xTx = xMat.T * (weights * xMat)
      ws = xTx.I * (xMat.T * (weights * yMat))
      
      return testPoint * ws

  def lwlr_test(testArr, xArr, yArr, k=1.0):
      m = shape(testArr)[0]
      yHat = zeros(m)
      for i in range(m):
          yHat[i] = lwlr(testArr[i], xArr, yArr, k)
      
      return yHat
  ```

- ![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/801f8cca-9e95-11e7-9497-0242ac140002)

- one problem with lwlr is that it involves lots of computations. you have to use the entire dataset to make one estimate.

- what if we have more features than data points? we'll get an error wen compute $X_{}^{T} * X$, and if we have more features than data points (n > m), we day that our data matrix $X$ isn't full rank. to solve this problem, we can use the ***shrinkage methods***. ridge regression and lasso regression.

- ***ridge regreesion*** add an matrix $\lambda I$ to the data matrix, so that it's non-singular and can compute the inverse.  then the solution will look like: $\hat w = (X_{}^{T} * X + \lambda I)_{}^{-1} * X_{}^{T} * y$, we can use the $\lambda$ to impose a maximum value on the sum of all our $ws$, by imposing this penalty, we can decrease unimportant parameters, this decreasing is known as ***shrinkage*** in statistics.

- we choose $\lambda$ to minimize prediction error, we take some of our data, set it aside for testing, and the use the remaining data to determine the $ws$, then test this model against our test data and measure its performance, this is repeated with different $\lambda$ values until we find a $\lambda$ that minimizes prediction error.

- There are other shrinkage methods such as the lasso, LAR, PCA regression and subset selection.

- ***lasso regression*** imposes a different constraint on the weights: $\sum_{k=1}^{n} |w_k \leq \lambda$, if $\lambda$ is small enough, some of the weights are forced to be exactly 0, which makes it easier to understand our data. to solve this we need a quadratic programming, which is too complex, we can use ***forward stagewide regression*** algorithm to get a similar solution.

- ***forward statewide regression*** is a greedy algorithm. it makes the decision that will reduce the error the most at that step, initally the weights are all set to 0, the decision that's made at each step is increasing or decreasing a weight by some small amount.

- summary:

  - regression is the process of predicting a target value similar to classification. the difference between regression and classification is that the variable forecasted in regression is ***continuous***, whereas it's ***discrete*** in classification.
  - regression is one of the most useful tools in statistics. minimizing the ***sum-of-squares*** error is used to find the best weights for the input features in a regression equation.
  - regression can be done on any set of data provided that for an input matrix $X$, you can compute the inverse of $X_{}^{T}X$. Just because you can compute a regression equation for a set of data doesn't mean that the results are very good, one test of how good or significant the results are is the ***correlation*** between the predicted values yHat and the original data y.
  - when you have more features that data points, you can't compute the inverse of $X_{}^{t}X$, if you have more data points that features, you still may not be able to compute $X_{}^{T}X$, if the features are highly correlated. ***ridge regression*** is a regression method that allows you to ocmpute regression coefficients despite being unable to compute the inverse of $X_{}^{T}X$.
  - ridge is an example of ***shrinkage method***, another method is the ***lasso***, the lasso is difficult to compute, but ***stagewise linear regression*** is easy to compute and gives results close to lasso.




## Tree-based Regression





# Unsupurvised Learning



## Grouping Unlabeled Items Using K-means Clustering

- ​




































## resources

- kaggle algorithms test
- http://mindhacks.cn/2008/09/21/the-magical-bayesian-method/
- [点到直线距离公式的几种推导](https://zhuanlan.zhihu.com/p/26307123)
- [支持向量机(SVM)是什么意思？](https://www.zhihu.com/question/21094489)
- [如何通俗易懂地解释「协方差」与「相关系数」的概念？](https://www.zhihu.com/question/20852004)
- [https://github.com/litaotao/MachineLearning](https://github.com/litaotao/MachineLearning)
- [ 加权最小二乘法与局部加权线性回归 ](https://uqer.io/community/share/57887c7e228e5b8a03932c66)
- []()
- []()
- []()






















