from textblob import TextBlob
from newspaper import Article

url = "https://en.wikipedia.org/wiki/Muhammad_Ali"
article = Article(url)

# Loading Data

article.download()
article.parse()
article.nlp()

text0 = article.summary
print(text0)

print("\n__Through URL__")

# Cheaking and showing polarity -1 to 1, Sentiment for data from url
blob = TextBlob(text0)
sentiment0 = blob.sentiment.polarity 
print(f"\nSentiment : {sentiment0}")

# loading self made txt data
with open('negative.txt', 'r') as n:
    text = n.read()

with open('positive.txt', 'r') as p:
    text2 = p.read()

print("\n__Through Texts__")

# Cheaking and showing polarity -1 to 1, Sentiment for data from txt files

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(f"\nSentiment 1 : {sentiment}")

blob = TextBlob(text2)
sentiment2 = blob.sentiment.polarity 
print(f"\nSentiment 2  : {sentiment2}\n")