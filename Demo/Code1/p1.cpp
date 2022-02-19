#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    unsigned long long int n;
    fin >> n;
    cout << (n%2==0 ? "YES\n" : "NO\n");
    fin.close();
    return 0;
}