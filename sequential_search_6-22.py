import random

def sequential_search(number_list, target_value):
    for index in range(len(number_list)):
       #determine if number at current index = target_value index
       #if so, return index and end loop
       if target_value == number_list[index]:
           return index
       
    return -1


def main():
    #use 101 as top limit
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    found_index = sequential_search(number_list, 23)

    print(found_index)
    


main()

#add explanation notes that printwith results
