#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    // Se for AM entao nao mudar nada, a nao ser que seja 12h, ai eu reduzo 12
    // Se for PM , sem ser 12h, eu somo 12, se for 12h eu mantenho
    
    if (s[8] ==  'A'){
        if(s[0] == '1' && s[1] == '2'){
            s[0] = '0';
            s[1] = '0';
        }
    }
    // 1  2   3  4  5  6  7  8  9  10 11
    // 13 14 15 16 17 18 19 20 21 22 23
    else
        if (s[0] != '1' || s[1] != '2') {
            if (s[1] == '8' || s[1] == '9') {
                s[0] = '2';            
            }
            else{
                if (s[0] == '1' && (s[1] == '0' || s[1] == '1'))
                {
                    s[0] = '2';
                }
                else s[0] = '1';
            }
            if (s[1] == '8') {
                s[1] = '0';
            }
            else{
                if (s[1] == '9') {
                    s[1] = '1';
                }
                else{
                    s[1] = s[1] + 2;
                }
            }
     }
    s.resize(8);
        
    
    
    return s;  
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
