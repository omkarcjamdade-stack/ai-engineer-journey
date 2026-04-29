from transformers import pipeline
import matplotlib.pyplot as plt
from datetime import datetime
import csv

print("Loading AI model... please wait\n")
sentiment_model = pipeline("sentiment-analysis")
print("Model ready!\n")

reviews = [
    "This product changed my life, absolutely love it!",
    "Terrible quality, broke after one day.",
    "It was okay, nothing special.",
    "Highly recommend, fantastic value for money!",
    "Worst customer service I have ever experienced.",
    "Decent product, does the job.",
    "Amazing! Will definitely buy again.",
    "Very disappointing, not worth the price.",
    "Fast delivery, very happy with purchase!",
    "Product looks nothing like the picture."
]
print(f"Analyzing {len(reviews)} reviews...\n")

results=[]
labels=[]

for review in reviews:
    result=sentiment_model(review)
    label = result[0]["label"]
    score = result[0]["score"]
    print(f"Review :{review}")
    print(f"sentiment:{label}({round(score*100,2)}%)\n")
    results.append(label)
    labels.append(label)

positive = labels.count("POSITIVE")
negative = labels.count("NEGATIVE")

print("==============================")
print(f"Total Reviews  : {len(reviews)}")
print(f"Total Positive : {positive}")
print(f"Total Negative : {negative}")

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.pie(
    [positive, negative],
    labels=["Positive", "Negative"],
    colors=["#2ecc71", "#e74c3c"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sentiment Distribution")

plt.subplot(1, 2, 2)
plt.bar(["Positive", "Negative"], [positive, negative],
        color=["#2ecc71", "#e74c3c"])
plt.title("Review Counts")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("sentiment_chart.png")
plt.show()

print("\nChart saved as sentiment_chart.png ✓")
