#include <iostream>
#include <string>
using namespace std;

int romanToInt(string roman) {
    int total = 0;
    
    for (int i = 0; i < roman.size(); i++) {
        // Get the value of the current Roman numeral
        int current = (roman[i] == 'I') ? 1 :
                      (roman[i] == 'V') ? 5 :
                      (roman[i] == 'X') ? 10 :
                      (roman[i] == 'L') ? 50 :
                      (roman[i] == 'C') ? 100 :
                      (roman[i] == 'D') ? 500 : 1000;
        
        // Get the value of the next Roman numeral (if it exists)
        int next = (i + 1 < roman.size()) ? 
                   (roman[i + 1] == 'I') ? 1 :
                   (roman[i + 1] == 'V') ? 5 :
                   (roman[i + 1] == 'X') ? 10 :
                   (roman[i + 1] == 'L') ? 50 :
                   (roman[i + 1] == 'C') ? 100 :
                   (roman[i + 1] == 'D') ? 500 : 1000 : 0;
        
        // Add or subtract the current value
        if (current < next) {
            total -= current;  // Subtract if the next numeral is larger
        } else {
            total += current;  // Otherwise, add
        }
    }
    
    return total;
}

int main() {
    string romanNumeral;
    cout << "Enter a Roman numeral: ";
    cin >> romanNumeral;
    
    cout << "Integer value: " << romanToInt(romanNumeral) << endl;
    return 0;
}
