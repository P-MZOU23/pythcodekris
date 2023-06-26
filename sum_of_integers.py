def find_indexes(nums,target):
    #create a dict
    complements = {}

    #loop through nums
    for index in range(0, len(nums)-1):

        #calculate comp.
        complement = target - nums[index]
        #check if the comp is in the comp. dictionary
        if complement in complements:
            return [complements[complement], index]
        #if comp found in both, return both indeces
        #add current item and the index to the comp dict
        complements[nums[index]] = index

    return
def main():
    nums = [1, 2, 3, 4, 7, 8, 12]
    target = 9
    result = find_indexes(nums, target)
    print(result)

main()