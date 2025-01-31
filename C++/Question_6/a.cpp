#include <iostream>

#include <stack>

#include <unordered_map>

using namespace std;

bool isValid(string s){

    stack<char> st;

    unordered_map<char, char> bracketPairs= {{')', '('}, {'}', '{'}, {']', '['}};

    

    for (char c: s){

        if (bracketPairs.count(c)){
            if (!st.empty() && st.top()== bracketPairs[c]){
                st.pop();
            }else{
                return false;
            }
        }else{
            st.push(c);
        }
    }
    return st.empty();

}


int main(){

    
  string s;
    cout << "Enter a string of brackets: ";
    cin >> s;

    if (isValid(s)) {
        cout << "The string is valid." << endl;
    } else {
        cout << "The string is not valid." << endl;
    }

    return 0;


}