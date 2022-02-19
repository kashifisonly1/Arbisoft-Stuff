#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    string s;
    getline(fin, s);
    int n = s.length();
    int i = 0;
    // ^ == XOR and a-z & A-Z has just 1 bit diff soo
    while( i<n/2 && ( s[i]==s[n-i-1] || (s[i]^s[n-1-i])==32)  )
        i++;
    cout << (( s[i]==s[n-i-1] || (s[i]^s[n-1-i])==32)  )?"TRUE\n":"FALSE\n");
    fin.close();
    return 0;
}