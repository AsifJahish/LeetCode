#include <iostream>
#include <string>

using namespace std;

string longCommonPrefix(string strs[], int n) {
    if (n == 0) {
        return "";
    }

    // Loop through characters of the first string
    for (int i = 0; i < strs[0].length(); i++) {
        char first = strs[0][i];  // character from the first string

        // Loop through all strings and check the current character
        for (int j = 1; j < n; j++) {
            // Check if we have reached the end of a string or the characters don't match
            if (i >= strs[j].length() || strs[j][i] != first) {
                return strs[0].substr(0, i);  // Return the prefix up to this point
            }
        }
    }

    return strs[0];  // If all strings match, return the whole first string
}

int main() {
    string stri[] = {"flower", "flow", "flight"};
    int n = sizeof(stri) / sizeof(stri[0]);  // Get the size of the array
    
    string result = longCommonPrefix(stri, n);
    cout << result << endl;  // Output should be "fl"
    
    return 0;
}
