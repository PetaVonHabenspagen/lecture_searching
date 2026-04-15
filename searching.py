from imp import load_source
from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(f"{file_path}", mode="r", encoding="utf-8") as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    return None

def linear_search(sequence, wanted_number):
    desired_dict = {
        "counter": 0,
        "positions": []
    }
    for number in sequence:
        if number == wanted_number:
            desired_dict["counter"] += 1
            pos = sequence.index(number)
            sequence[pos] += 1
            desired_dict["positions"].append(pos)
    return desired_dict

def binary_search(numbers_list, wanted_number):
    left = 0
    right = len(numbers_list) -1
    while left <= right:
        middle = (left + right) // 2
        if numbers_list[middle] == wanted_number:
            return middle
        elif numbers_list[middle] < wanted_number:
            left = middle + 1
        elif numbers_list[middle] > wanted_number:
            right = middle - 1

    return None

def test_complexity(list_of_n):
    for n in list_of_n:
        unordered = unordered_sequence(n)
        ordered = ordered_sequence(n)
        times_linear = []
        times_binary = []

        duration_linear = 0
        duration_binary = 0
        rep = 100
        for measurements in range(rep):
            start_linear = time.perf_counter()
            linear = linear_search(unordered, 42)
            end_linear = time.perf_counter()
            duration_linear = end_linear - start_linear

            start_binary = time.perf_counter()
            binary = binary_search(ordered, 42)
            end_binary = time.perf_counter()
            duration_binary = end_binary - start_binary
        times_linear.append(duration_linear / rep)
        times_binary.append(duration_binary / rep)
    plt.plot(list_of_n, times_linear)
    plt.plot(list_of_n, times_binary)
    return

def pattern_search(sequency, pattern):
    indices = {}
    for i in range(sequency):
        if sequency[i:i+len(pattern)] == pattern:
            indices["index"].append(i)
    return indices

def main():
    sequential_data_linear = read_data("sequential.json", "unordered_numbers")
    sequential_data_binary = read_data("sequential.json", "ordered_numbers")
    wanted_number = 5

    linear_data = linear_search(sequential_data_linear, wanted_number)

    start = time.perf_counter()
    binary_data = binary_search(sequential_data_binary, 21)
    end = time.perf_counter()
    diff = end - start
    # print(diff)
    sizes = [100, 500, 1000, 5000, 10000]
    print(linear_data)
    print(binary_data)
    test_complexity(sizes)
    return



if __name__ == "__main__":
    main()