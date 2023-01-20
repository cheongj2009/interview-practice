from typing import List


# This was my solution, which is accepted
def runningSum1(nums: List[int]) -> List[int]:
    tracker = 0
    result = []

    for num in nums:
        tracker += num
        result.append(tracker)

    return result


# This is one suggested elegant solution
# which actually uses the existing array and increments across it
# starting from the second position, which is index of 1
def runningSum2(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Case 1
    nums = [1, 2, 3, 4]
    expected = [1, 3, 6, 10]
    print(runningSum1(nums) == expected)
    print(runningSum2(nums) == expected)

    # Case 2
    nums = [1, 1, 1, 1, 1]
    expected = [1, 2, 3, 4, 5]
    print(runningSum1(nums) == expected)
    print(runningSum2(nums) == expected)

    # Case 3
    nums = [3, 1, 2, 10, 1]
    expected = [3, 4, 6, 16, 17]
    print(runningSum1(nums) == expected)
    print(runningSum2(nums) == expected)
