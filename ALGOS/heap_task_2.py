import heapq


nums = [5, 15, 1, 3]

def streaming_median(nums):
    low = []
    high = []
    result = []

    for n in nums:
        if not low or n < -low[0]:
            heapq.heappush(low, -n)
        else:
            heapq.heappush(high, n)

        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2
        else:
            median = -low[0]

        result.append(median)

    return result

print(streaming_median(nums))