# Remove Duplicates: Remove duplicates in-place from a sorted static array.
def remove_duplicates(arr):
    i = 1
    j = 1
    while  j < len(arr) :
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
        j+=1
    return arr[:i+1]
print(remove_duplicates([1,2,3,3,4,4,5,5]))