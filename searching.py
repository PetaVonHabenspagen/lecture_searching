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
            desired_dict["positions"].append(pos)
    return desired_dict


def main(filename, key):
    sequential_data = read_data(filename, key)
    return print(sequential_data)


if __name__ == "__main__":
    main("sequential.json", "unordered_numbers")
