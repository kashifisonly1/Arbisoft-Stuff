#include <cmath>
#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    int n;
    fin>>n;
    int mat[n][n];
    int sum_main = 0, sum_secondary = 0;
    for(int i =0; i<n; i++) {
        for(int j = 0; j<n; j++) {
            fin>>mat[i][j];
        }
        sum_main += mat[i][i];
        sum_secondary += mat[i][n-i-1];
    }
    cout<<abs(sum_main-sum_secondary)<<endl;
    fin.close();
    return 0;
}