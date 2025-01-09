class plandrome:
    def plandrome(self, x):
        
        reverse= ""

        for i in str(x):
            reverse= i+reverse
        
        if int(reverse)==x:
            return True
        else:
            return False
        # return int(reverse)


plan = plandrome()

a =121
# 214243
print(plan.plandrome(a))