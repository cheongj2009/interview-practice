from typing import List


# This was my solution, which is accepted
def pivotIndex1(nums: List[int]) -> int:

    for index, _ in enumerate(nums):
        l_sum = sum(nums[:index])
        r_sum = sum(nums[(index + 1):])
        if l_sum == r_sum:
            return index

    return -1


# This is one suggested solution which improves upon my original solution
# It keeps a running sums of the left side and right side and
# adds / subtracts values from those sums as we traverse the array
# otherwise check approach is similar as above
# If there is no index that satisfies condition, return -1
# Time Complexity : O(n)
# Space Complexity : O(1)
def pivotIndex2(nums):

    # Initialize leftSum & rightSum to store the sum of all the numbers strictly
    # to the index's left & right respectively
    leftSum, rightSum = 0, sum(nums)
    for idx, ele in enumerate(nums):
        rightSum -= ele
        if leftSum == rightSum:
            return idx
        leftSum += ele

    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Case 1
    nums = [1, 7, 3, 6, 5, 6]
    expected = 3
    print(pivotIndex1(nums) == expected)
    print(pivotIndex2(nums) == expected)

    # Case 2
    nums = [1, 2, 3]
    expected = -1
    print(pivotIndex1(nums) == expected)
    print(pivotIndex2(nums) == expected)

    # Case 3
    nums = [2, 1, -1]
    expected = 0
    print(pivotIndex1(nums) == expected)
    print(pivotIndex2(nums) == expected)
