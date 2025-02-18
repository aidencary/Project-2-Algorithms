# Aiden Cary, Dalton Gorham, Nathan Wetherington
# Project 2 Algorithms
# Testing the efficiency of different sort 
# on a randomly generated array of numbers based on the size from user input

import sys, os

# Add the Sorts directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "Sorts"))
sys.setrecursionlimit(2000)

import random, time
from Sorts import bubble_sort
from Sorts import merge_sort
from Sorts import quick_sort
from Sorts import selection_sort

# Function to generate an array based on the case type
def generate_array(size, case_type):
    if case_type == "1":
        return list(range(size)) # Best case (sorted)
    elif case_type == "2":
        return list(range(size, -1, -1)) # Worst case (reverse sorted)
    elif case_type == "3":
        return random.sample(range(size), size) # Average case (random)

# Function use to meaure the sort execution time
def measure_sort_time(size, case_type, sort_func):
    # Generate the array
    arr = generate_array(size, case_type)
    # Get the start time
    start_time = time.time()
    # Call the sort function
    # Have not thought this implementation through yet
    sort_func(arr)
    # Get the end time
    end_time = time.time()
    # Return the execution time
    return end_time - start_time

# Print sort menu options
def print_sort_menu():
    print("Select the sorting algorithm you want to test.")
    print("--------------------------")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Selection Sort")
    print("5. Exit")
    choice = input("Select a sorting algorithm (1-5): ")
    if choice in ["1", "2", "3", "4", "5"]:
        return choice
    else:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5.")
        return print_sort_menu()
    
# Print case menu options
def print_case_menu(menu_choice):
    # If else statement to determine the sort name
    sort_name = ""
    if menu_choice == 1:
        sort_name = "Bubble Sort"
    elif menu_choice == 2:
        sort_name = "Merge Sort"
    elif menu_choice == 3:
        sort_name = "Quick Sort"
    elif menu_choice == 4:
        sort_name = "Selection Sort"
    
    print("Case Menu")
    print("1. Best Case")
    print("2. Worst Case")
    print("3. Average Case")
    print(f"4. Exit {sort_name} test")
    choice = input("Select a case type (1-3): ")
    if choice in ["1", "2", "3", "4"]:
        return choice
    else:
        print ("Invalid input. Please enter 1, 2, 3, or 4.")
        return print_case_menu(menu_choice)

# Main loop to handle user input and menu options
def main_loop():
    while True:
        sort_choice = print_sort_menu()
        if sort_choice == "5":
            break
        while True:
            case_choice = print_case_menu(sort_choice)
            if case_choice == "4":
                break
            size = int(input("Enter the size of the array: "))
            execution_time = 0
            case_scenario = "Best" if case_choice == "1" else "Worst" if case_choice == "2" else "Average" if case_choice == "3" else "Invalid choice"
            sort_name = ''
            if sort_choice == "1":
                sort_name = "Bubble Sort"
                execution_time = measure_sort_time(size, case_choice, bubble_sort.bubbleSort)
            elif sort_choice == "2":
                sort_name = "Merge Sort"
                execution_time = measure_sort_time(size, case_choice, merge_sort.merge_sort)
            elif sort_choice == "3":
                sort_name = "Quick Sort"
                execution_time = measure_sort_time(size, case_choice, quick_sort.quick_sort)
            elif sort_choice == "4":
                sort_name = "Selection Sort"
                execution_time = measure_sort_time(size, case_choice, selection_sort.selection_sort)
            with open("sort_times.txt", "a") as file:
                    file.write(f"For {sort_name} \nIn {case_scenario} case, \nFor N = {size}, it takes {execution_time} seconds to sort.\n")
                    file.write("-------------------------------------------------------------\n")


def main():
    '''
    print("Main has been called")
    # Test array
    arr = [2, 3, 1, 5, 4]
    print(f"Unsorted array: {arr}")
    # Test quick sort
    quick_sort.quick_sort(arr, 0, len(arr)-1)

    # Test bubble sort
    bubble_sort.bubbleSort(arr)

    # Test merge sort (merge sort returns a new array that is sorted)
    arr = merge_sort.merge_sort(arr)

    # Test selection sort
    selection_sort.selection_sort(arr)

    print(f"Sorted array: {arr}")
    '''

    print("Welcome to the test suire of selected sorting algorithms!\n")
    main_loop()



if __name__ == "__main__":
    main()