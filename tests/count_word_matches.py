def count_word_matches(text, target):
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")
    if not isinstance(target, str):
        raise TypeError(f"target must be a string, got {type(target).__name__}")

    if not text or not target:
        return 0

    words = text.lower().split()
    target = target.lower()

    return words.count(target)
