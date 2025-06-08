
class Index:
    def index_baseon_value(self, array, value):

        for i in range(len(array)):

            if array[i]== value:
                return i
    

result= Index()
    
arr=[1,2,3,3,2,2,2,2,2,3,3,3,7,7,8,3,2,2,2,2,2,2]
value= 7 
result_index= result.index_baseon_value(arr, value)

print(result_index)