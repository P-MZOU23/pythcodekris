import random

def sequential_search(number_list, target_value):
    for index in range(len(number_list)):
       #determine if number at current index = target_value index
       #if so, return index and end loop
       if target_value == number_list[index]:
           return index
       
    return -1

"""
function to run binary search on a sorted list
Imputs: list, target value
Output: found index
"""
def binary_search(arr, target_value):
    #define high and low indexes of the list
    low_index = 0
    high_index = len(arr) - 1
    #note the index is len - 1, because the length is one more than the last index; index starts with 0
    
    #create loop to search 4 target value
    while low_index <= high_index:
        #double slash means integer division, so it rounds down
        middle_index = (low_index + high_index)//2

        #check if target value is at middle index in list
        if arr[middle_index] == target_value:
            return middle_index
        #if the value at the midd_index is not the target, compare
        elif arr[middle_index] < target_value:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1



def main():
    #use 101 as top limit
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    #down here you can put binary or sequential. Binary is better/faster with a lot of numbers
    target_value = 77
    found_index = binary_search(number_list, target_value)

    print(number_list[found_index])

    if found_index == -1:
        print(f"{target_value} not found in list")
    else:
        print(f"{target_value} found at index {found_index}")

main()
