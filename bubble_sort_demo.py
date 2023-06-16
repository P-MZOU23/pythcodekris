import random

def bubble_sort(data_list):
    number_of_items = len(data_list)
    #loop through list
    for i in range(number_of_items):
        #loop through list to visit each item, as many times as there are items in the list
        for j in range(number_of_items - 1):
            #compare adjacent items
            if(data_list[j+1] < data_list[j]):
                #if right element (Number) is less than left, switch position
                temp=data_list[j]
                data_list[j]=data_list[j+1]
                data_list[j+1]=temp

    return data_list

#create a list of integers




#def is the way to intoduce the function of the following
def main():
    #create the list
    my_list = [5,7,8,10]
    integer_list = random.sample(range(0,1000), 100)
    print(integer_list)

    #call bubble sort function
    sorted_list = bubble_sort(integer_list)

    print(sorted_list)

main()