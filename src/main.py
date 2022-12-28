import math
import random

def count_letters_exact(text):
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

def count_letters_approx(text, probability=1/math.sqrt(2)):
    counts = {}
    for letter in text:
        if letter in counts:
            p = probability / math.sqrt(2)**counts[letter]
            if p > random.uniform(0, 1):
                counts[letter] += 1
        else:
            counts[letter] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

def count_letters_lossy(text, threshold=10):
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    for key in list(counts.keys()):
        counts[key] -= 1
        if counts[key] < threshold:
            del counts[key]
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


with open('../data/after-preprocessing/text1.txt', 'r') as f:
    text = f.read()

    print("Counter Letters Exact: ", count_letters_exact(text))
    print("\n\nCounter Letters Aprox: ", count_letters_approx(text))
    print("\n\nCounter Letters Lossy: ", count_letters_lossy(text))
