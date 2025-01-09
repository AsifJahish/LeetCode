#include <iostream>
using namespace std;

void sumIndex(int arr[], int target) {
    // Use sizeof(arr) only within this function, when it's a fixed-size array
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        for (int j = i + 1; j < sizeof(arr) / sizeof(arr[0]); j++) { // Start j from i+1
            if (arr[i] + arr[j] == target) {
                cout << "Indices: " << i << ", " << j << endl;
                return; // Exit the function after finding the first pair
            }
        }
    }
    cout << "No solution found." << endl; // If no pair is found
}

int main() {
    int arr1[] = {2, 7, 11, 15}; // Example array
    int target = 9;              // Example target

    sumIndex(arr1, target); // Call function directly with array and target

    return 0;
}
