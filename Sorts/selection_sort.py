def selection_sort(arr):
    #Get the length
    n=len(arr)

    #Loop through the array except the last element
    for i in range(n-1):
        #Starting smallest element 
        min_index=i 
        #Loops through the rest of the array looking for a smaller element 
        for j in range(i+1,n):
            #If smaller element is found update min_index
            if arr[j] < arr[min_index]:
                min_index=j
                
        arr[i], arr[min_index]= arr[min_index], arr[i]
    return arr