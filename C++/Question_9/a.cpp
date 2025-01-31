#include <iostream>

using namespace std;

int removeElement(int nums[], int size, int val, int result[]) {
    int j = 0; // Index for the result array

    for (int i = 0; i < size; ++i) {
        if (nums[i] != val) {
            result[j++] = nums[i]; // Copy elements not equal to 'val'
        }
    }

    return j; // Return the new size of the result array
}

int main() {
    int nums[] = {1, 2, 3, 4, 3, 5}; // Input array
    int size = sizeof(nums) / sizeof(nums[0]); // Calculate size of the array
    int val = 3; // Element to remove
    int result[size]; // Array to store the modified array

    // Call the removeElement function
    int newSize = removeElement(nums, size, val, result);

    // Print the modified array
    cout << "Modified array: ";
    for (int i = 0; i < newSize; ++i) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}
