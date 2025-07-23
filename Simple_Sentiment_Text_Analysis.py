from textblob import TextBlob
from newspaper import Article
import pandas as pd
from matplotlib import pyplot as plt

# Loading Data
url = "https://en.wikipedia.org/wiki/Muhammad_Ali"
article = Article(url)

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

# loading self made txt files
with open('negative.txt', 'r') as n:
    text = n.read()

with open('positive.txt', 'r') as p:
    text2 = p.read()

print("\n__Through Texts__")

# Cheaking and showing polarity -1 to 1, Sentiment for data from txt files

blob = TextBlob(text)
sentiment1 = blob.sentiment.polarity # -1 to 1
print(f"\nSentiment 1 : {sentiment1}")

blob = TextBlob(text2)
sentiment2 = blob.sentiment.polarity 
print(f"\nSentiment 2  : {sentiment2}\n")

# taking the values in dic
Sentiments = {
    "Names" : ["sentiment0", "sentiment1", "sentiment2"],
    "values" : [sentiment0, sentiment1, sentiment2]
    }

# ploting the graph of the sentiments with values
df = pd.DataFrame(Sentiments)

df.plot(x= "Names", y= "values", kind= "line", color = 'black')

plt.title("Sentiments Text Analysis Graph")
plt.xlabel("Names")
plt.ylabel("values")
plt.show()