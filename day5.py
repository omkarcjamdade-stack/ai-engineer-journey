from transformers import pipeline

print("Loading AI model.....please wait\n")

sentiment_model=pipeline("sentiment-analysis")

print("Model ready!\n")
print("=== AI Sentiment Analyzer")
print("Type a review and press Enter.Type 'quit' to stop\n")

while True:
    review=input("Enter review: ")

    if review.lower()=="quit":
        break
    result = sentiment_model(review)
    label=result[0]["label"]
    score=result[0]["score"]

    print(f"->{label}")
    print(f"-> Confidence:{round(score*100,2)}%\n")