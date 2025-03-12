import time
start_time = time.time() * 1000
def reverse_array(arr,k):
    
    # Type 1
    # arr[:] = arr[::-1]
    # arr[:k] = arr[:k][::-1]
    # arr[k:] = arr[k:][::-1]

    # Type 2
    for i in range(k):
        arr.insert(0,arr[-1])
        arr.pop()
    
    return arr
end_time = time.time() * 1000
if __name__ == "__main__" :
    print(reverse_array([1,2,3,4,5,6,7,8,10,23,4,14,1,5,1,4,1,4,1,45,56,6,6,72,4,5,7,2,6,8,2,7,2,6,9,2,6,2,7,26,2,6,2,6,2,6,5,8,2],6))
    print(f"Time Taken - {end_time - start_time} ms")
