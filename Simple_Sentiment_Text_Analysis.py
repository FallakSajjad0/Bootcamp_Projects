from textblob import TextBlob
from newspaper import Article

url = "https://en.wikipedia.org/wiki/Matthew_Muller"
article = Article(url)

article.download()
article.parse()
article.nlp()

text0 = article.summary
print(text0)

print("\n__Through URL__")

blob = TextBlob(text0)
sentiment0 = blob.sentiment.polarity 
print(f"\nSentiment : {sentiment0}")

with open('negative.txt', 'r') as n:
    text = n.read()

with open('positive.txt', 'r') as p:
    text2 = p.read()

print("\n__Through Texts__")

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(f"\nSentiment 1 : {sentiment}")

blob = TextBlob(text2)
sentiment2 = blob.sentiment.polarity 
print(f"\nSentiment 2  : {sentiment2}\n")