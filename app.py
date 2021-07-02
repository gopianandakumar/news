from flask import Flask,render_template 
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c005c347b5fc41b79760188b38aa5812')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')


data = top_headlines['articles']
#news =[]

# for i in data:
# 	news.append(i['title'])



app=Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html",news =data )


if __name__=="__main__":
	app.run(debug=True)



