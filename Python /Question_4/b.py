class solution:
    def romanToInt(self, roNumber):

        roman_value = {
             'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }

        total = 0

        preNumber= 0

        for char in reversed(roNumber):

            current= roman_value[char]

            if preNumber < preNumber:
                total -=current
            else:
                total += current 
            preNumber= current
        return total

roman = solution()

number= str(input())

print(roman.romanToInt(number))