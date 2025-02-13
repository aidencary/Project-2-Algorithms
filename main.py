# Aiden Cary, Dalton Gorham, Nathan Wetherington
# Project 2 Algorithms
# Testing the efficiency of different sort 
# on a randomly generated array of numbers based on the size from user input

import sys, os

# Add the Sorts directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "Sorts"))

import random, time
import bubble_sort
import merge_sort
import quick_sort
import selection_sort

def main():
    print("Main has been called")
    # Test array
    arr = [1, 3, 2, 5, 4]
    
    # Test quick sort
    #quick_sort.quick_sort(arr, 0, len(arr)-1)

    # Test bubble sort
    #bubble_sort.bubbleSort(arr)

    # Test merge sort [FIX MERGE SORT IMPLEMEQNTATION]
    # I think the merge_sort I grabbed is from Python2
    #merge_sort.merge_sort(arr)

    # Test selection sort
    selection_sort.selection_sort(arr)

    print(arr)



if __name__ == "__main__":
    main()