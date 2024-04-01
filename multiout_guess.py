# Thanks to python developers, scikit, How Hard is Today’s Wordle?
# imports
import numpy as np
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import re
import pandas as pd

# Read datafile and define arrays based on max number of lines
datafile = pd.read_csv('data.csv')
totLines=len(datafile)
totChars=5

# global variables for word manipulation
lineNum=0
stringIs=[ [None] * totChars] * totLines
XVal=[0] * totLines

# distribution of letters frequency
letterFrequency = { 
'E' : 12.0, 'T' : 9.10, 'A' : 8.12, 'O' : 7.68, 'I' : 7.31,
'N' : 6.95, 'S' : 6.28, 'R' : 6.02, 'H' : 5.92, 'D' : 4.32,
'L' : 3.98, 'U' : 2.88, 'C' : 2.71, 'M' : 2.61, 'F' : 2.30,
'Y' : 2.11, 'W' : 2.09, 'G' : 2.03, 'P' : 1.82, 'B' : 1.49,
'V' : 1.11, 'K' : 0.69, 'X' : 0.17, 'Q' : 0.11, 'J' : 0.10,
'Z' : 0.07 
}

vowels="AEIOU"

# Parsing string and storing word
wordsAre=[]
y_train=[ ] * totLines
for row in datafile.itertuples():
	#Build up list of words
	wordsAre.append(row.word)
	curArray=[]
	#Build up array of output (multiple)
	curArray.append(row.two)
	curArray.append(row.three)
	curArray.append(row.four)
	curArray.append(row.five)
	curArray.append(row.six)
	y_train.append(curArray)

#Convert word to numerical values
for word in wordsAre:
	# Give slightly higher value to vowels
	for vowel in vowels:
		XVal[lineNum]=XVal[lineNum]+(word.count(vowel) * letterFrequency[vowel])
	# Add in value for each character
	for charIs in word:
		XVal[lineNum]=XVal[lineNum]+(word.count(charIs) * letterFrequency[charIs])

	lineNum=lineNum+1

X_train_data = np.array(XVal)
X_train = X_train_data.reshape(-1, 1)
min_max_scaler = MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)

# Current day word
testData = ["04/01/2024,FROND,98,4.3,0,2,21,36,28,11,2"]
testWordIs = re.split(",", testData[0])
testVal=0.0

#Normalize the data
X_test_data = np.array([testVal])
X_test = X_test_data.reshape(-1, 1)

#Train and Predict
clf = MultiOutputClassifier(LogisticRegression()).fit(X_train_minmax, y_train)
print (clf.predict(X_test[-2:]))
#print (clf.predict_proba(X_test[-2:]))
