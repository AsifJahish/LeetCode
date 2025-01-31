#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0; // Edge case: Empty array

    int unique = 0; // Pointer for the last unique element

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] != nums[unique]) { // Check if current element is different from the last unique
            unique++;                  // Move the unique pointer
            nums[unique] = nums[i];    // Place the current element in the correct position
        }
    }

    return unique + 1; // The number of unique elements
}

int main() {
    vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};

    int k = removeDuplicates(nums); // Get the number of unique elements

    cout << "Number of unique elements: " << k << endl;

    cout << "Array after removing duplicates: ";
    for (int i = 0; i < k; i++) { // Print only the first k elements
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}
