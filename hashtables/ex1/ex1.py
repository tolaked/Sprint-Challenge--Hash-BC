#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # cycle over array elements
    for i in range(length):
        # get difference of limit and current weight
        diff = limit - weights[i]

        # Check if current weight exist in cache
        cached = hash_table_retrieve(ht, diff)
        print(cached)

        if cached is None:
            hash_table_insert(ht, weights[i], i)
        else:
            if cached < i:
                return (i, cached)
            else:
                return (cached, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
