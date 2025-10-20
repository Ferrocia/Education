import heapq
a = [10,2,4,3,2,12,14,6]
k=3

def get_k_from_heap(some_list, K, min=True):
    heap = some_list.copy()
    heapq.heapify(heap)
    result = []
    if min:
        for z in range(K):
            result.append(heapq.heappop(heap))
    else:
        heap = [-x for x in some_list]
        heapq.heapify(heap)
        for z in range(K):
            result.append(-heapq.heappop(heap))

    return result


print(get_k_from_heap(a, k))