

def quicksort(arr):

    #IF ARRAY HAS ONE (or zero) ITEM(s), RETURN
    if len(arr) <= 1:
        return arr
    
    stack = []
    stack.append((0, len(arr) - 1))

    while len(stack) > 0:
        pass


def main():
    empty_array = [50, 30, 80, 20, 10 ,70, 60]
    empty_array = []
    quicksort(empty_array)

main()