#include <iostream>

using namespace std;

int lenghtofLastLetter(string s){

    int lenght= 0;
    bool foundWord = false;

    for (int i=s.size()-1; i>=0;  i--){
          if (s[i] != ' ') {  // If it's a letter, count it
                lenght++;
            foundWord = true;
            } else if (foundWord) {  // Stop counting when a space is found after the last word
                break;
            }
        }

    return lenght;

    
};

int main(){


    string  s = "luffy is still joyboy";

    cout<< lenghtofLastLetter(s)<<endl;

}