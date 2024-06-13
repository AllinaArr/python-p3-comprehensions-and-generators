#!/usr/bin/env python3

def return_evens(num_list):
    list = []
    for num in num_list:
        if num % 2 == 0:
            list.append(num)
    return list

def make_exclamation(sentence_list):
    list = []
    for word in sentence_list:
        if isinstance(word, str):
            list.append(word+"!")
    return list