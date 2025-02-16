import random, time

def bubbleSort(myList): # Bubble Sort Algorithm
    n = len(myList)
    for i in range(n - 1):
        swapped = False
        for j in range(n-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = myList[j + 1], myList[j]
                swapped = True
        if not swapped:
            break # For best case scenario where the list is already sorted
    return myList

'''
def main(k = 100):

    #m = [random.randint(1, 10*k) for i in range(k)]

    m = random.sample(range(10*k), k)
    
    t1 = time.perf_counter()
    sortedList = bubbleSort(m)
    t2 = time.perf_counter()
    print('Bubble sort', k, 'items costs', round((t2-t1), 5), 'seconds')
    #print(sortedList)

if __name__ == "__main__":
    main(1000)
'''
