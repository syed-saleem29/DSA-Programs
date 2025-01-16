# Move all negative numbers to beginning and positive to end with constant extra space
#problem 5
def rearrange(arr):                                  # Can be done using two pointers as well
     j = 0
     for i in range(0,len(arr)):
         if arr[i] < 0:
             arr[j], arr[i] = arr[i], arr[j]
             j += 1

# problem 6
def find_union(a, b):
    record = {}
    for items in (a+b):
        if items in record:
            pass
        else:
            record[items] = items

    return len(record)

# problem 7
def rotate(arr):
    # My method
    # arr.insert(0, arr[-1])
    # arr.pop(-1)
    arr[:] = arr[-1:] + arr[:-1]



if __name__ == "__main__":
    #input
    demo = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]

    #Problem 5
    # rearrange(demo)
    # print(demo)

    # Problem 6
    # print(find_union(a, b))

    # Problem 7
    rotate(a)
    print(a)