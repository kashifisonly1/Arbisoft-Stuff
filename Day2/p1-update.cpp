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

void solve() {
    int n;
    map< string, set<string> > tribes; 
    cin>>n;
    for(int i = 0; i<n; i++) {
        string tribe;
        cin>>tribe;
        string name;
        getline(cin, name);
        map< string, set<string> >::iterator finder = tribes.find(tribe);
        if(finder==tribes.end()) {
            // add new
            set<string> s;
            s.insert(name);
            tribes.insert( pair<string, set<string> >(tribe, s) );
        }
        else{
            // just add name in set
            finder->second.insert(name);
        }
        //tribes[tribe].insert(name);
    }
    for(map< string, set<string> >::iterator finder = tribes.begin(); finder!=tribes.end(); ++finder)
        cout<<finder->first<<" "<<finder->second.size()<<endl;
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