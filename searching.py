from pathlib import Path
import json


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
    import json
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





def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    wanted_number = 5
    linear_data = linear_search(sequential_data, wanted_number)
    binary_data = binary_search(sequential_data, 21)
    return print(binary_data)



if __name__ == "__main__":
    main()