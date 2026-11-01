def analyze_sentence(text: str) -> tuple:
    """Analyze the text and return character count, word count, and Python presence."""
    char_count = len(text)
    word_count = len(text.split())
    has_python = "python" in text.lower()

    return (char_count, word_count, has_python)


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    user_sentence = input("Enter a sentence: ")
    chars, words, contains_python = analyze_sentence(user_sentence)

    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")