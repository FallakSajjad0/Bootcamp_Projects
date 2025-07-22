print(text0)

blob = TextBlob(text0)
sentiment0 = blob.sentiment.polarity 
print(f"Sentiment0 : {sentiment0}")