from transformers import pipeline
import csv
from datetime import datetime

print("Loading AI model .....please wait\n")
sentiment_model=pipeline("sentiment-analysis")
print("Model ready!\n")

reviews=[
    "This product changed my life,absolutely love it!",
    "Terrible quality, broke after one day.",
    "It was okay, nothing special.",
    "Highly recommend, fantastic value for money!",
    "Worst customer service i have never experienced.",
    "Decent product, does the job.",
    "Amazing! Will definitely buy again.",
    "Very disappointing, not worth the price."
]

print(f"Analyzing {len(reviews)} reviews....\n")
results=[]

for review in reviews:
    result=sentiment_model(review)
    label=result[0]["label"]
    score=result[0]["score"]

    print(f"Review:{review}")
    print(f"Sentiment:{label}({round(score*100,2)}%)")
    print()
    
    results.append({
        "review":review,
        "sentiment":label,
        "confidence":f"{round(score*100,2)}%",
        "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
with open("ai_review.csv","w",newline="") as f:
    writer=csv.DictWriter(f, fieldnames=["review","sentiment","confidence","time"])
    writer.writeheader()
    writer.writerows(results)
positive=sum(1 for r in results if r["sentiment"]=="POSITIVE")
negative=sum(1 for r in results if r["sentiment"]=="NEGATIVE")

print("==========================")
print(f"Total reviews : {len(reviews)}")
print(f"Total Positive : {positive}")
print(f"Total Negative : {negative}")
print(f"\nResults saved to ai_reviews.csv✓")