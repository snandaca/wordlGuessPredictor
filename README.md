# wordlGuessPredictor
 Predict the percentage of guesses for words
 Loads data for about 20 words and trains it using MultiOutputClassifier
 (Thanks to scikit and Chris from engaging-data - What is the distribution of guesses for the daily Wordle?
 Current days word is manually added and it predicts the guess percentage
 1 guess  0% (always)
 2 guesses thru 6 guesses - predicted
 Fail - Not predicted

 For 4/1, word FROND, predicted values are (predicted vs actual)
 2 guesses -  2 vs 2
 3 guesses - 14 vs 21
 4 guesses - 37 vs 36
 5 guesses - 29 vs 28
 6 guesses -  7 vs 2

 Frequency of words is used for predicting, vowels are added in again to skew it a little bit more towards words having more vowels

 Feel free to download and play around with it, if you have any improvements, email me at snandaca@yahoo.com
