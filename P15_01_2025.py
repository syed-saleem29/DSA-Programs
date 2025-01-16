# problem 1
def reverse_array(arr):
    length_of_array = len(arr)
    new_arr = [0]*length_of_array
    for i in range(length_of_array):
        new_arr[i] = arr[length_of_array - 1 - i]
    return new_arr

    #str(x)[::-1]                     	--can be used to reverse the integers by converting into string and then reversing
    # for item in my_list[::-1]        	--traverse list in backward
    # for item in reversed(my_list)    	--traverse list in backward(2nd method)
    # for i in range(len(digits)-1, -1, -1):  --traversing the index of the list in backward
#problem 2
def min_max(arr):
    return min(arr), max(arr)

def min_max2(arr):
    arr.sort()
    return arr[0], arr[-1]

# problem 3
# QuickSort is the best sorting algorithm to sort an array with less time complexity
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def kthSmallest(arr, k):
    arr = quick_sort(arr)
    return arr[k - 1]

# problem 4
def sort012(arr):
    num_dict = {0 : 0,
                1 : 0,
                2 : 0}
    for numbers in arr:
        num_dict[numbers] += 1
    arr[:num_dict[0]] = [0] * num_dict[0]                               #This is used for in-place replacement
    arr[num_dict[0]:num_dict[0] + num_dict[1]] = [1] * num_dict[1]
    arr[num_dict[0] + num_dict[1]:] = [2] * num_dict[2]










if __name__ == "__main__":
    # Inputs
    demo_arr = [1, 2, 9, 4, 5, 6, 7, 8]
    sort012arr = [0, 1, 2, 0, 1, 2]


    # Problem 1
    # print(reverse_array(demo_arr))

    # Problem 2
    # print(list(min_max(demo_arr)))
    # print(list(min_max2(demo_arr)))

    # Problem 3
    # print(kthSmallest(demo_arr,3))

    # Problem 4
    # print("Sorted array In-Place (Before):", sort012arr)
    # sort012(sort012arr)
    # print("Sorted array In-Place (After) :",sort012arr)


