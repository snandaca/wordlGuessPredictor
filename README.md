# wordlGuessPredictor
 Predict the percentage of guesses for words
 Loads data for about 20 words and trains it using MultiOutputClassifier
 (Thanks to scikit and Chris from engaging-data - What is the distribution of guesses for the daily Wordle?
 Current days word is manually added and it predicts the guess percentage
 1 guess  0% (always)
 2 guesses thru 6 guesses - predicted
 Fail - Not predicted

 For 4/1, word FROND, percentages are
 | #Guess | Predicted | Actual |
 |--------|-----------|--------|
 | 2      |    2      |    2   |
 | 3      |   14      |   21   |
 | 4      |   37      |   36   |
 | 5      |   29      |   28   |
 | 6      |    7      |    2   |

 Frequency of words is used for predicting, vowels are added in again to skew it a little bit more towards words having more vowels

 Feel free to download and play around with it, if you have any improvements, email me at snandaca@yahoo.com
