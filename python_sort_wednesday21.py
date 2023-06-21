import random

def sequential_search(number_list, target_value):
    for index in range(len(number_list)):
       #determine if number at current index = target_value index
       #if so, return index and end loop
       if target_value == number_list[index]:
           return index and print("NOTE TO SELF: This index is the target_value minus one.")
       
    return -1
    print("NOTE TO SELF: Remember that -1 is not in the list. This is the default if the target value was not in the list.")

def main():
    #use 101 as top limit
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    found_index = sequential_search(number_list, 23)

    print(found_index)
    


main()