#!/usr/bin/env python3
def return_evens(num_list):
    # return only even numbers using list comprehension
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    # add "!" at the end of each string
    return [s + "!" for s in sentence_list]

