
#include<iostream>

using namespace std;

void merge(int nums1[], int m, int nums2[], int n){

    int i= m-1;
    int j=n-1;

    for (int k = m + n - 1; k >= 0; k--) {

        if (j<0){
            break;
        } else if(i>=0 & nums1[i]>nums2[j]){
            nums1[k]=nums1[i];
            i--;
        }else{
            nums1[k]=nums2[j];
            j--;
        }


    }
    
}

int main(){
    int nums1[6] = {1, 2, 3, 0, 0, 0}; // nums1 has extra space for nums2
    int m = 3;
    int nums2[3] = {2, 5, 6};
    int n = 3;

    merge(nums1, m, nums2, n);

    // Print the merged array
    for (int i = 0; i < m + n; i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;

    return 0;
}