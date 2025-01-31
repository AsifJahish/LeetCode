class Roman:
    def RomanNumber(self, number):

        roman_value = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        
        total= 0

        pre_value=0



        for char in number[::-1]:

            current= roman_value[char]

            if current< pre_value:
                total-=current
            else:
                total+=current

            pre_value =current


        return total


    # there is two soluton to make this work 

roman= Roman()

# number= 'MCMXCIV'
# number= 'I'

number= str(input())

print(roman.RomanNumber(number))