def merge_sorted_array(arr1,arr2,len_arr3):
    i = 0
    j = 0
    arr3 = []
    while i < len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        
        else:
            arr3.append(arr2[j])
            j+=1
    if len(arr1) == len(arr2):
        return arr3[:len_arr3]
    elif len(arr1) > len(arr2):
        arr3 += arr1[-(len(arr1) - len(arr2)):]
        return arr3[:len_arr3]
    else:
        arr3 += arr2[-(len(arr2) - len(arr1)):]
        return arr3[:len_arr3]

print(merge_sorted_array([1, 3, 5],[2,4],5))
array1 = [10, 20, 30]

array2 = [15, 25]

print(merge_sorted_array(array1,array2,4))

# Output: [10, 15, 20, 25] (capacity 4)