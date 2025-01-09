class plandrome:
    def plandrome(self, x):
        if str(x)[::-1]== str(x):
            return True
        else:
            return False

plan = plandrome()

b= 121

print(plan.plandrome(b))