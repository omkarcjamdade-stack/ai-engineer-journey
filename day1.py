reviews=["This product is amazing!",
         "Terrible experince, never buying again.",
         "It was okay, nothing special.",
         "Loved it,will recommend to friends!",
         "Very bad quality, broke in two days.",
         "The worst product I ever bought, absolutely horrible!"]

positive_words=["amazing","loved","great", "good","recommend"]
negative_words=["terrible","bad","broke","worst","never"]

for review in reviews:
    review_lower=review.lower()

    is_positive=any(word in review_lower for word in positive_words)
    is_negative=any(word in review_lower for word in negative_words)

    if is_positive:
        print(f"POSITIVE:{review}")
    elif is_negative:
        print(f"NEGATIVE:{review}")
    else:
        print(f"NEUTRAL:{review}")
