

class Delete:
    def delete_at_index(self, array, index):
        array.pop(index)
        return array
    
    def delete_at_value(self, array, value):

        for i in array:
            if i == value:
                array.remove(value)
                break
        return array


result= Delete()

arr= [1,2,3,4,5,6]
arr2= [1,2,3,4,5,6]

index =5
value = 3

result_index= result.delete_at_index(arr, index)

result_value= result.delete_at_value(arr2, value)

print(result_index)

print(result_value)