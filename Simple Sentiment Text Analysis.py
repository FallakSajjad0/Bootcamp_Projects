from textblob import TextBlob
# from newspaper import Article

# url = ""

# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

with open('negative.txt', 'r') as n:
    text = n.read()

with open('positive.txt', 'r') as p:
    text2 = p.read()


blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(f"\nSentiment 1 : {sentiment}")

blob = TextBlob(text2)
sentiment2 = blob.sentiment.polarity 
print(f"\nSentiment 2  : {sentiment2}\n")