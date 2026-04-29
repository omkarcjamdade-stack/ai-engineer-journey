reviews=[
    "This product is amazing",
    "terrible experince never buying again",
    "It was okay, nothing special.",
    "Loved it, will recommend to friends!",
    "Very bad quality, broke in two days."
]

positive_words=["amazing","loved","great","good","recommend"]
negative_words=["terrible","bad","broke","worst","never"]

positive_count=0
negative_count=0
neutral_count=0

for review in reviews:
    review_lower=review.lower()
    is_positive=any(word in review_lower for word in positive_words)
    is_negative=any(word in review_lower for word in negative_words)

    if is_positive:
        print(f"POSITIVE:{review}")
        positive_count=positive_count+1
    elif is_negative:
        print(f"NEGATIVE:{review}")
        negative_count=negative_count+1
    else:
        print(f"NEUTRAL:{review}")
        neutral_count=neutral_count+1
print("--------------------------")
print(f"Total Positive ={positive_count}")
print(f"Total Negative={negative_count}")
print(f"Total Neutral={neutral_count}")
