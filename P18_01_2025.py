# problem 10
def minimum_jumps(arr):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(arr)):
        if i > farthest:
            return -1
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if farthest >= len(arr) - 1:
                break
    return jumps

# problem 11
def findDuplicate(nums):
    low, high = 1, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low

# Others
def findDuplicate(nums) -> int:
    # Phase 1: Finding the intersection point of the two runners
        p = [0] * len(nums)
        for i in nums:
            if p[i] is not 0:
                return i
            else:
                p[i] = i


        return 0


if __name__ == "__main__":
    # inputs
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr2 = [1, 3, 4, 2, 2]

    # Problem 10
    print(minimum_jumps(arr))

    # Problem 11
    print(findDuplicate(arr2))