

class Searh:
    def search_on_value(self, array,value,):
        for i in array:
            if i== value:
                return i
            
    def search_element_index(self, array, value):

        for i in range(len(array)):
            if arr[i]== value:
                return i
        return -1 

result= Searh()

arr=[1,2,3,4,5,6,7,7,7,8,]
value= 7
result_value= result.search_on_value(arr, value)
result_element= result.search_element_index(arr, value)

print(result_value)
print(result_element)