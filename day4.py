import csv
from datetime import datetime

positive_words=["amazing","loved","great","good","recommend","excellent","fantastic"]
negative_words=["terrible","bad","broke","worst","never","horrible","awful"]

positive_count=0
negative_count=0
neutral_count=0

results=[]

print("===== Review Sentiment Analyzer =====")
print("Type a review and press Enter. Type 'quit' to stop.\n")

while True:
    review=input("Enter review:")

    if review.lower()=="quit":
        break
    review_lower=review.lower()
    is_positive=any(word in review_lower for word in positive_words)
    is_negative=any(word in review_lower for word in negative_words)

    if is_positive:
        sentiment="POSITIVE"
        positive_count+=1
    elif is_negative:
        sentiment="NEGATIVE"
        negative_count+=1
    else:
        sentiment="NEUTRAL"
        neutral_count+=1
    print(f"-> {sentiment}\n")

    results.append({
        "review":review,
        "sentiment":sentiment,
        "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     })
    
    #save to CSV
with open("review.csv","w",newline="") as f:
    writer=csv.DictWriter(f, fieldnames=["review", "sentiment", "time"])
    writer.writeheader()
    writer.writerows(results)

print("================================")
print(f"Total Positive : {positive_count}")
print(f"Total Negative : {negative_count}")
print(f"Total Neutral : {neutral_count}")

print(f"\nResults saved to reviews.csv ✓")