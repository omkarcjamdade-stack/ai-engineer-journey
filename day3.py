positive_words=["amazing","loved","great","good","recommend","excellent","fantastic"]
negative_words=["terrible","bad","broke","worst","never","horrible","awful"]
positive_count=0
negative_count=0
neutral_count=0

print("=== Review Sentiment Analyzer ===")
print("Type a review and press Enter. Type 'quit' to stop.\n")

while True:
    review=input("Enter review:")
    if review.lower()=="quit":
        break
    review_lower=review.lower()
    is_positive=any(word in review_lower for word in positive_words)
    is_negative=any(word in review_lower for word in negative_words)

     

    if is_positive:
        print(f"-> POSITIVE ✓\n" )
        positive_count+=1
    elif is_negative:
        print(f"-> NEGATIVE ✘\n")
        negative_count+=1
    else:
        print(f"-> NEUTRAL -\n")
        neutral_count+=1

print("==============================")
print(f"Total Positive:{positive_count}")
print(f"Total Negative:{negative_count}")
print(f"Total Neutral:{neutral_count}")

