# problem 8
# Maximum Subarray Sum using --: Kadane's Algorithm :--
def largest_sum_contiguous_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# problem 9
def get_min_diff(arr, k):
    arr.sort()
    # code
    result = arr[-1] - arr[0]

    for i in range(len(arr) - 1):
        min_height = min(arr[0] + k, arr[i + 1] - k)
        max_height = max(arr[i] + k, arr[-1] - k)

        if min_height >= 0:
            result = min(result, max_height - min_height)

    return result


if __name__ == "__main__":
    # inputs
    arr = [2, 3, -8, 7, -1, 2, 3]
    arr2 = [3, 9, 12, 16, 20]
    k = 3
    # Problem 8
    print(largest_sum_contiguous_subarray(arr))

    # Problem 9
    print(get_min_diff(arr2, k))