def maximum(nums):
    nums = [str(x) for x in nums]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i] 

    result = "".join(nums)
    return result if result[0] != "0" else "0"


print(maximum([21, 2]))
print(maximum([9, 4, 6, 1, 9]))
print(maximum([23, 39, 92]))
print(maximum([6, 2, 34, 9]))
