#include<iostream>

using namespace std;

bool plandrome(int x){

    int reverse = 0;
    int original = x; // Store the original number

    // Simple for loop to reverse the number
    for (int i = x; i > 0; i /= 10) {
        int digit = i % 10;  // Extract the last digit
        reverse = reverse * 10 + digit;  // Build the reversed number
    }

    return reverse == original; 
    



}

int main(){
    int x= 121;
    bool result = plandrome(x);
   
   cout << (result ? "True" : "False") << endl;

}