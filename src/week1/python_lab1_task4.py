def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    return sum(1 for char in text if not char.isspace())


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    numbers = []
    for word in text.split():
        clean_word = word.rstrip(".,!?;:")

        # Mənfi ədədləri və müsbət rəqəmləri yoxlamaq üçün
        # Məsələn: "-4" -> təmizlənmiş hissə "-4", əgər minusu silesək rəqəmdirmi?
        if clean_word.isdigit():
            numbers.append(int(clean_word))
        elif clean_word.startswith("-") and clean_word[1:].isdigit():
            numbers.append(int(clean_word))

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)

    total_sum = sum(nums) if nums else 0
    average = total_sum / len(nums) if nums else 0.0

    return {
        "characters": chars,
        "words": words,
        "numbers": nums,
        "sum": total_sum,
        "average": average
    }


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    user_text = input("Enter text: ")
    res = analyze_text(user_text)

    print(f"Characters (no spaces): {res['characters']}")
    print(f"Words: {res['words']}")
    print(f"Numbers: {res['numbers']}")
    print(f"Sum: {res['sum']}")
    print(f"Average: {res['average']:.2f}")