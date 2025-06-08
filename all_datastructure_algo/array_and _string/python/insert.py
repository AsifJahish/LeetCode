

class Insert:
    def inset_at_index(self, arr, index, value):
        arr.insert(index, value)
        return arr
    


result= Insert()


arr= [1,2,3,4]

index= 3
value =34

res= result.inset_at_index(arr, index, value)

print(arr)