from flask import Flask,render_template, request,json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import re


app = Flask(__name__)

dataset = pd.read_csv('dataset - enlarged.csv', skiprows=1, header=None)
f=open("Apache_2k.log.txt", "r")
opt_file= open("opt_file.csv","w+")
vectorizer = CountVectorizer()
train_bow_set = vectorizer.fit_transform(dataset[0])
tfidf_transformer = TfidfTransformer().fit(train_bow_set)
messages_tfidf = tfidf_transformer.transform(train_bow_set)
detect_model = LogisticRegression().fit(messages_tfidf,dataset[1])


@app.route('/')
def home():
	for line in f:
		new_line = line
		searchObj = re.search("\[error\]",new_line)
		if searchObj:
			problem_summary = re.split('\[error\]',new_line)[-1]
			bow = vectorizer.transform([problem_summary])
			tfidf4 = tfidf_transformer.transform(bow)
			resolution = detect_model.predict(tfidf4)
			opt_file.write("%s , %s \n" %(problem_summary,resolution))
	return render_template('SelfManagementSystem.html')

@app.route('/data')
def data():
	for line in f:
		new_line = line
		searchObj = re.search("\[error\]",new_line)
		if searchObj:
			problem_summary = re.split('\[error\]',new_line)[-1]
			bow = vectorizer.transform([problem_summary])
			tfidf4 = tfidf_transformer.transform(bow)
			resolution = detect_model.predict(tfidf4)
			opt_file.write("%s , %s \n" %(problem_summary,resolution))
	return render_template('homePage.html')
		
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form['Resolution']
		bow = vectorizer.transform([result])
		tfidf4 = tfidf_transformer.transform(bow)
		resolution = detect_model.predict(tfidf4)
		return render_template("result.html",resolution = resolution)
	  
if __name__=="__main__":
    app.run()