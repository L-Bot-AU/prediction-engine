#include <iostream>
#include <fstream>
#include "include\nlohmann\json.hpp"
#include <string>
#include <iomanip>

using json = nlohmann::json;
using namespace std;

int main(){
    const string location = "calcData.json";
    const string days[5] = {"Mon", "Tue", "Wed", "Thu", "Fri"};
    ifstream fin{location};
    
    string library;
    int year, m, b;
    json data;
    fin >> data;

    cout << "Enter Library Jnr/Snr: ";
    cin >> library;
    cout << "Enter year: ";
    cin >> year;

    for(int i = 1; i<2; i++){ /*For the 4 terms*/
        for(int j=0; j<2; j++){ /*Each day of week*/
            cout << "For term " << i << " " << days[i] << " enter the following values for:";
            cout << "\n\tbefore school:";
            cout << "\n\tGradient (m): ";
            cin >> m;
            cout << "\n\tConstant (b): ";
            cin >> b;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["bs"]["m"] = m;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["bs"]["b"] = b;
            cout << "\n\tbreak 1:";
            cout << "\n\tGradient (m): ";
            cin >> m;
            cout << "\n\tConstant (b): ";
            cin >> b;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["b1"]["m"] = m;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["b1"]["b"] = b;
            cout << "\n\tbreak 2:";
            cout << "\n\tGradient (m): ";
            cin >> m;
            cout << "\n\tConstant (b): ";
            cin >> b;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["b2"]["m"] = m;
            data[library][to_string(year)]["Term"+to_string(i)][days[j]]["b2"]["b"] = b;
        }
    }
    ofstream fout{location};
    fout << setw(4) << data;
}