"""
AI-Augmented Task
Text Analysis Module
"""

from typing import Dict


def count_words(text: str) -> int:
    """Count number of words in text"""
    return len(text.split())


def count_sentences(text: str) -> int:
    """Count sentences in text"""
    return text.count('.') + text.count('!') + text.count('?')


def find_longest_word(text: str) -> str:
    """Find longest word in text"""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def simple_sentiment(text: str) -> str:
    """Very basic sentiment analysis"""

    positive_words = ["good", "great", "excellent", "happy", "love"]
    negative_words = ["bad", "poor", "sad", "hate"]

    score = 0

    for word in text.lower().split():

        if word in positive_words:
            score += 1

        if word in negative_words:
            score -= 1

    if score > 0:
        return "positive"

    if score < 0:
        return "negative"

    return "neutral"


def analyze_text(text: str, **options) -> Dict:
    """
    Analyze text based on enabled options.

    Options:
    count_words
    count_sentences
    find_longest_word
    sentiment_simple
    """

    if not text:
        return {}

    results = {}

    if options.get("count_words", True):
        results["word_count"] = count_words(text)

    if options.get("count_sentences", True):
        results["sentence_count"] = count_sentences(text)

    if options.get("find_longest_word", True):
        results["longest_word"] = find_longest_word(text)

    if options.get("sentiment_simple", True):
        results["sentiment"] = simple_sentiment(text)

    return results


if __name__ == "__main__":

    text = "Python is great. I love machine learning!"

    result = analyze_text(text)

    print(result)