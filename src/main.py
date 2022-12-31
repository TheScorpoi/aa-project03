import math
import random
from prettytable import PrettyTable

random.seed(98491)

K_VALUES = [3, 5, 10]

def exact_counter(text: str) -> list:
    letters_freq = {}
    for letter in text:
        if letter != ' ':
            if letter in letters_freq:
                letters_freq[letter] += 1
            else:
                letters_freq[letter] = 1
    return sorted(letters_freq.items(), key=lambda x: x[1], reverse=True)

def increment_function(current_count):
    count = 0
    if random.random() <= 1 / math.sqrt(2) ** current_count: 
        count += 1
    return count

def approximate_counter(text: str) -> list:
    counts = {}
    for letter in text:
        counter = 0
        if letter in counts.keys():
            counter = counts[letter]
            
        increment = increment_function(counter)
        
        counter += increment
        counts[letter] = counter
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

def count_letters_lossy(text: str, threshold=0.00001, k=None) -> list:
    counts = {}
    error = 1
    for letter in text:
        if letter != ' ':
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
            error -= threshold
            if error < 0:
                counts = { key : math.floor(counts[key] / 2) for key in counts.keys() }
                error = 1
    
    #retrive all the list or just the k most frequent letters
    if k is None:
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
    return sorted_counts

with open('../data/after-preprocessing/text3.txt', 'r') as f:
    text = f.read()

    #print("Counter Letters Exact: ", exact_counter(text))
    #print("\n\nCounter Letters Aprox: ", approximate_counter(text))
    #print("\n\nCounter Letters Lossy: ", count_letters_lossy(text))

    table = PrettyTable()
    table.field_names = ["Letter", "Exact Counter", "Approximate Counter", "Lossy Counter"]
    
    exac_counter_ = exact_counter(text)
    approximate_counter_ = approximate_counter(text)
    count_letters_lossy_ = count_letters_lossy(text)
    
    for i in K_VALUES:
        print("Most frequent letters witk k = ", i, " -- ", count_letters_lossy(text, k=i))
    
    for i in range(len(exact_counter(text))):
        table.add_row([exac_counter_[i][0], exac_counter_[i][1], approximate_counter_[i][1], count_letters_lossy_[i][1]])
    print(table)
    
    approximate_counter_ = approximate_counter(text)
    lst = []
    for i in range(10):
        lst.append(approximate_counter_)

    highest_value = 0
    lowest_value = 100
    average_value = 0
    counter = 0
    
    for i in range(10):
        for k, v in lst[i]:
            counter += 1
            average_value += v
            if v > highest_value:
                highest_value = v
            if v < lowest_value:
                lowest_value = v
    
    print("------------------------------------------------------------------------")
    print("---------------------------Aproximate-Counter---------------------------")
    print("------------------------------------------------------------------------")
            
    print("Highest value: ", highest_value)
    print("Lowest value: ", lowest_value)
    print("Average value: ", average_value / counter)
         
def compute_absolute_error(lst) -> None:
    highest_value = 0
    lowest_value = 100
    average_value = 0
    counter = 0
    
    for i in range(10):
        for k, v in lst[i]:
            counter += 1
            average_value += v
            if v > highest_value:
                highest_value = v
            if v < lowest_value:
                lowest_value = v