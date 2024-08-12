#!/usr/bin/python3
"""
This module contains a function that finds a peak in a 
list of unsorted integers using binary search algorithm
"""
def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None

    int_list = list_of_integers
    start = 0
    end = len(int_list) - 1
    mid = (start + end) // 2
    
    # check first element
    if int_list[start] > int_list[start + 1]:
        return int_list[start]
    # check last element
    elif int_list[end] > int_list[end - 1]:
        return int_list[end]
    # check the middle element
    elif int_list[mid - 1] <= int_list[mid] and int_list[mid + 1] <= int_list[mid]:
        return int_list[mid]
    # search left
    elif int_list[mid] < int_list[mid - 1]:
        return find_peak(int_list[start:mid + 1])
    # search right
    else: 
        return find_peak(int_list[mid:end + 1])
