#include <iostream>

using namespace std;

int searchInsert(int nums[], int& length, int target) {
    // Search for the target
    for (int i = 0; i < length; i++) {
        if (nums[i] == target) {
            return i; // Return index if found
        }
    }

    // Insert target at the end if not found
    nums[length] = target; // Add target at the next available position
    length++; // Increase the array length

    // Return the index of the newly inserted target
    return length - 1;
}

int main() {
    const int MAX_SIZE = 100; // Define a maximum size for the array
    int nums[MAX_SIZE] = {1, 3, 5, 6}; // Initial array
    int length = 4; // Current size of the array
    int target = 7;

    // Call the function
    int index = searchInsert(nums, length, target);

    // Output the results
    cout << "Target " << target << " is at index: " << index << endl;

    // Print the updated array
    cout << "Updated array: ";
    for (int i = 0; i < length; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}
