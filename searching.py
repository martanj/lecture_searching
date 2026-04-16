import json
import os
import time
from fileinput import filename

from setuptools.dist import seque
import json
import matplotlib.pyplot as plt
import time
# get current working directory path
# cwd_path = os.getcwd()


def read_data(path, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if key in data:
        return data[key]
    else:
        return None

    # if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
    #     return None
    #
    # file_path = os.path.join(cwd_path, file_name)
    #
    # with open(file_path, "r") as json_file:
    #     seq = json.load(json_file)
    # return seq[field]

def linear_search(sequence , search_number):
    # indices = []
    # count = 0
    #
    # idx = 0
    # while idx < len(seq):
    #     if seq[idx] == number:
    #         indices.append(idx)
    #         count += 1
    #     idx = 1
    #
    # return {
    #     "positions": indices,
    #     "count": count,
    # }
    indexes = []
    count = 0
    for i, num in enumerate(sequence):
        if num == search_number:
            indexes.append(i)
            count += 1
    return {
            "positions": indexes,
            "count": count
        }

# def pattern_search(seq, pattern):
    # pattern_size = len(pattern)
    # indices = []
    # left_idx = 0
    # right_idx = pattern_size
    # while right_idx < len(seq):
    #      for idx in range(pattern_size):
    #         if pattern[idx] != seq[left_idx + idx]:
    #             break
    #         else:
    #             indices.add(left_idx + pattern_size // 2)
    #
    #         left_idx += 1
    #         right_idx += 1
    #
    # return indices


def binary_search(indexes, search_number):
    left, right = {0, len(indexes) -1}
    while left <= right:
        middle = (right + left) // 2

        if search_number < indexes[middle]:
            right = middle -1
        elif search_number > indexes[middle]:
            left = middle + 1
        else:
            return middle
    return


sizes = [100, 500, 1000, 5000, 10000]
binko = []
sekvenko = []
for



def main():
    path = "sequential.json"

    sequence = read_data(path, key = "unordered_numbers")

    indexes = linear_search(path, key = "ordered_numbers")


    # results = linear_search(seq, number= 0)
    #
    # seq = read_data(path, key="dna_sequence")
    # pattern = 'ATA'
    #
    # matches = pattern_search(seq, pattern)
    #
    # seq = read_data(path, key= "ordered_numbers")
    #
    # number_x = binary_search(seq,number=14)
    #
    # start_time = time.time()
    #
    #
    # total_time = time.time() - start_time



if __name__ == '__main__':
    main()