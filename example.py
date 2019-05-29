import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
import pandas as pd

#model = pickle.load(open('model_LR.sav', 'rb'))
dataset = pd.read_csv('dataset - enlarged.csv', skiprows=1, header=None)

vectorizer = CountVectorizer()
train_bow_set = vectorizer.fit_transform(dataset[0])
tfidf_transformer = TfidfTransformer().fit(train_bow_set)
messages_tfidf = tfidf_transformer.transform(train_bow_set)
detect_model = LogisticRegression().fit(messages_tfidf,dataset[1])

result = 'There was a chargeoff reversal which generated an interest amount. There was also a payment on the same day which generated T'
bow = vectorizer.transform([result])
print(bow)
tfidf4 = tfidf_transformer.transform(bow)
resolution = detect_model.predict(tfidf4)
print(resolution)		