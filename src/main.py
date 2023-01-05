import math
import random
import time
from prettytable import PrettyTable

#K_VALUES = [3, 5, 10]
K_VALUES = [3]

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
        if letter != ' ':
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

def calculate_error_metrics(error_dict : dict) -> None:
    """mean, highest and lowest error for approximate counter"""
    sum_values = 0
    highest_value = 0
    lowest_value = 100
    
    for k, v in error_dict.items():
        sum_values += v
        if v > highest_value:
            highest_value = v
        if v < lowest_value:
            lowest_value = v
    
    mean = sum_values / len(error_dict)

    return mean, highest_value, lowest_value

if __name__ == "__main__":

    text = None
    with open('../data/after-preprocessing/alice_fr.txt', 'r') as f:
        text = f.read()

    table = PrettyTable()
    table.title = "Counters"
    table.field_names = ["Letter", "Exact Counter", "Approximate Counter", "Lossy Counter"]
    
    #calculate execution time for each counter
    A = time.time()
    exac_counter_ = exact_counter(text)
    B = time.time()
    exac_counter_time = B - A
    
    approximate_counter_ = approximate_counter(text)
    C = time.time()
    approximate_counter_time = C - B
    
    count_letters_lossy_ = count_letters_lossy(text)
    count_letters_lossy_time = time.time() - C
    
    for i in K_VALUES:
        #print("Most frequent letters witk k = ", i, " -- ", count_letters_lossy(text, k=i))
        for i in count_letters_lossy(text, k=i):
            if i[0] in [j[0] for j in approximate_counter_]:
                print(i[0], " - ", i[1], " - ", [j[1] for j in approximate_counter_ if j[0] == i[0]][0])

            
    print(approximate_counter_)
    print(count_letters_lossy_)
        
    #! comport a ordem das letras do aproximate counter e do lossy counter
    
    for i in range(len(exact_counter(text))):
        table.add_row([exac_counter_[i][0], exac_counter_[i][1], approximate_counter_[i][1], count_letters_lossy_[i][1]])
    
    table.add_row(["---------", "-----------", "-------------", "-----------"])
    table.add_row(["--TIME--", "{:.3f}".format(exac_counter_time), "{:.3f}".format(approximate_counter_time), "{:.3f}".format(count_letters_lossy_time)])
    
    with open("../results/alice_en.txt", "w") as f:
        f.write(table.get_string())
        print(table)
        
    ##########
        
    approximate_counter_ = approximate_counter(text)
    lst = []
    for i in range(10):
        lst.append(approximate_counter_)
        
    
    ## abs and relative error for approximate counter
    abs_error_aproximate_counter = {}
    relative_error_aproximate_counter = {}
    
    i = 0
    for letter, freq in approximate_counter_:
        real_counter = exac_counter_[i]
        i += 1
        if freq != real_counter:
            abs_error_aproximate_counter[letter] = abs(freq - real_counter[1])
            relative_error_aproximate_counter[letter] = abs(freq - real_counter[1]) / real_counter[1]
            
    print("\n\n\n")
    
    table_errors = PrettyTable()
    table_errors.title = "Absolute and Relative Error for Approximate Counter"
    table_errors.field_names = ["Letter", "Absolute Error", "Relative Error"]
    for i in range(len(abs_error_aproximate_counter)):
        table_errors.add_row([list(abs_error_aproximate_counter.keys())[i], list(abs_error_aproximate_counter.values())[i], list(relative_error_aproximate_counter.values())[i]])
    
    
    mean_abs, highest_abs, lowest_abs = calculate_error_metrics(abs_error_aproximate_counter)
    mean_rel, highest_rel, lowest_rel = calculate_error_metrics(relative_error_aproximate_counter)

    table_errors.add_row(["---------", "-----------", "-------------"])
    table_errors.add_row(["---MEAN---", "{:.3f}".format(mean_abs), "{:.3f}".format(mean_rel)])
    table_errors.add_row(["--HIGHEST--", "{:.0f}".format(highest_abs), "{:.3f}".format(highest_rel)])
    table_errors.add_row(["--LOWEST--", "{:.0f}".format(lowest_abs), "{:.3f}".format(lowest_rel)])
    
    print(table_errors)
    
    
    with open("../results/alice_en.txt", "a") as f:
        f.write("\n\n\n")
        f.write(table_errors.get_string())
        
        
    ##########
    
    
    
    
    
    
    
    
    
    