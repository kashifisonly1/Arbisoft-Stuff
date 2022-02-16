#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
#define cin fin
#define cout fout

ifstream fin;
ofstream fout;
struct Tribe{
    string name;
    vector<string> people;
    Tribe(string nm, string p) {
        name = nm;
        people.push_back(p);
    }
};
/*

{
    key: value,
    key: value
}

*/
/*
[]
ABC xyz
[ {name: abc, [xyz]} ]
ABC aaa
[ {name: abc, [xyz, aaa]} ]
ABC aaa
[ {name: abc, [xyz, aaa]} ]
*/
bool sorter(Tribe& a, Tribe& b) {
    return a.name<b.name;
}
void solve() {
    int n;
    vector<Tribe> tribes;
    cin>>n;
    for(int i = 0; i<n; i++) {
        string tribe;
        cin>>tribe;
        string name;
        getline(cin, name);
        // if tribe exists
        int j = 0;
        while(j<tribes.size() && tribes[j].name!=tribe)
            j++;
        // j ya to end pr hoga
        // ya phr found
        if(j==tribes.size()) {
            // end
            tribes.push_back( Tribe(tribe, name) );
        }
        else{
            //found
            int k = 0;
            while(k<tribes[j].people.size() && tribes[j].people[k]!=name)
                k++;
            // not found
            if(k==tribes[j].people.size())
                tribes[j].people.push_back(name);
        }
    }
    sort(tribes.begin(), tribes.end(), sorter);
    for(int i = 0; i<tribes.size(); i++)
        cout << tribes[i].name << " " << tribes[i].people.size()<<endl;
}

int main() {
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    cin>>T;
    for(int t = 1; t<=T; t++) {
        cout << "Case: "<<t<<endl;
        solve();
    }
    fin.close();
    fout.close();
}