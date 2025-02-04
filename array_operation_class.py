class Static_Array:
    def __init__(self,length,values = None):
        self.length = length
        self.arr = [None] * length
        if values:
            min_value = min(length,len(values))
            self.arr[:min_value] = values[:min_value]
    def static_insert(self,value ,index):
        self.value = value
        if index >= self.length:
            raise IndexError
        while index < len(self.arr):
            temp = self.arr[index]
            self.arr[index] = self.value
            self.value = temp
            index += 1
    def dynamic_insert(self,value ,index):
        self.value = value
        if index >= self.length:
            raise IndexError("Index out of range")
        while index < len(self.arr):
            temp = self.arr[index]
            self.arr[index] = self.value
            self.value = temp
            index += 1
        self.arr.append(value)
    def static_delete_at_index(self,index):
        if index > len(self.arr):
            raise IndexError("Index out of Range")
        self.index = index
        while self.index < len(self.arr)-1:
            self.arr[self.index] = self.arr[self.index + 1]
            self.index +=1
        self.arr[-1] = None
    def dynamic_delete_at_index(self,index):
        if index > len(self.arr):
            raise IndexError("Index out of Range")
        self.index = index
        while self.index < len(self.arr)-1:
            self.arr[self.index] = self.arr[self.index + 1]
            self.index +=1
        arr = [None] * (len(self.arr)-1)
        arr[:] =self.arr[:-1]
        self.arr = arr
    def static_delete_element(self,ele):
        self.element = ele
        if self.element not in self.arr:
            raise ValueError("Element not in Array")
        for i in range(len(self.arr)):
            if self.arr[i] == self.element:
                arr.static_delete_at_index(i)
                break
        
    def dynamic_delete_element(self,ele):
        self.element = ele
        if self.element not in self.arr:
            raise ValueError("Element not in Array")
        for i in range(len(self.arr)):
            if self.arr[i] == self.element:
                arr.dynamic_delete_at_index(i)
                break
    def get(self,index):
        if index >= self.capacity:
            raise IndexError("Index out of bounds")
        return self.arr[index]
    def search(self,ele):
        if ele not in self.arr:
            raise ValueError("Element not in array")
        for i in range(len(self.array)):
            if self.array[i] == ele :
                return i

    def dynamic_append(self,ele):
        temp_arr = [None] * (len(self.arr) + 1)
        temp_arr[:-1] = self.arr
        temp_arr[-1] = ele
        self.arr = temp_arr

    def true_length(self):
        count = 0
        for i in self.arr:
            if i is not None:
                count += 1
        return count



arr = Static_Array(4)
arr1 = Static_Array (3,[1,2,3,4])
arr2 = Static_Array(4,[1,2,3])
arrr3 = Static_Array(4,[1,2,3,4])
arr.static_insert(1,0)
arr.static_insert(2,1)
arr.static_insert(3,0)
arr.static_insert(4,2)
arr.dynamic_insert(5,1)
arr.static_insert(3,1)
arr.static_delete_at_index(3)
arr.dynamic_delete_at_index(2)
arr.static_delete_element(3)
arr.dynamic_delete_element(3)
arr.dynamic_append(4)


