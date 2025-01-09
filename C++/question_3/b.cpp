#include <iostream>

using namespace std;

bool isPalindrome(int x) {
    // Handle negative numbers and numbers ending with 0 (except 0 itself)
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int reverse = 0;
    int original = x; // Store the original number

    // Simple for loop to reverse the number
    for (int i = x; i > 0; i /= 10) {
        int digit = i % 10;  // Extract the last digit
        reverse = reverse * 10 + digit;  // Build the reversed number
    }

    return reverse == original;  // Compare the reversed number with the original
}

int main() {
    int x = 121;
    bool result = isPalindrome(x);
    cout << (result ? "True" : "False") << endl;
    return 0;
}
