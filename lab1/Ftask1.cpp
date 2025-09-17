#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, cnt = 0;
    cin >> n;

    vector<bool> prime(100001, true);
    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= 100000; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= 100000; j += i) {
                prime[j] = false;
            }
        }
    }

    vector<int> v;
    for (int i = 2; i <= 100000; i++) {
        if (prime[i]) v.push_back(i);
    }

    vector<int> super;
    for (int i = 0; i < (int)v.size(); i++) {
        if (prime[i + 1]) { 
            super.push_back(v[i]);
        }
    }

    cout << super[n - 1];
    return 0;
}
