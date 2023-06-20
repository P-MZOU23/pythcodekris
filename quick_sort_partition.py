"""
a function to perform a quicksort on arr
imput: list
output: sorted list
"""
def quick_sort(arr):
    #create a stack to simulate recursive calls
    stack = []
    #place list partitions on the stack
    stack.append((0, len(arr) - 1))
        #list starts at 0, so index of the last is one less than the total length
    #inside while loop. loop runs until stack of partitions in empty. continues while there are values in "stack"
    while stack:
        #get the next partition to process
        low, high = stack.pop()
        #partition the array. find pivot index for that partition. call partition function.
        pivot_index = partition(arr, low, high)

        #if there are items on the left of the pivot, put them on stack
    if pivot_index - 1 > low:
        stack.append((low, pivot_index - 1))
        #if there are items on the right of pivot, put them on stack
    if pivot_index + 1 < high:
        stack.append((pivot_index + 1, high))

"""
functions to find a partition index in a list
imputs: (list)arr, (int)low, (int)high
output: (int)partition index
"""

def partition(arr, low, high):
    #choose the rightmost item as the pivot
    pivot = arr[high]
    #create a variable for border, i
    i = low - 1
    #loop through partition to place all items <= the pivot to the left. and >= pivot to the right
    for j in range(low, high):
        #if current item is less than or equal to the pivot, swap it witht the element at the border (extreme)
        if arr[j] <= pivot: 
            i += 1    
            #we have already checked i, move up
            #swap arr i and j
            arr[i], arr[j] = arr[j], arr[i]
        
    #place pivot in correct position
    #swap the pivot with item at the border
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

def main():
    #create a list
    arr = [40, 80, 10, 90, 30, 50, 70]
    quick_sort(arr)
    print(arr)

main()