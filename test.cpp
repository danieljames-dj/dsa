#include <bits/stdc++.h>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long n, q;
    cin >> n;
    vector<vector<long>> counts;
    vector<long> v(26, 0);
    counts.push_back(v);
    for (long i = 1; i <= n; i++) {
        string s;
        cin >> s;
        vector<long> freq(26);
        for (long j = 0; j < s.length(); j++) {
            freq[s[j] - 'a']++;
        }
        counts.push_back(freq);
        for (long j = 0; j < 26; j++) {
            counts[i][j] += counts[i-1][j];
        }
    }
    
    cin >> q;
    while (q--) {
        long ans = LONG_MAX;
        string s;
        cin >> s;
        vector<long> freq(26);
        for (long j = 0; j < s.length(); j++) {
            freq[s[j] - 'a']++;
        }
        long i = 0, j = 1;
        while (j <= n) {
            bool enough = false;
            while (!enough && j <= n) {
                enough = true;
                for (long h = 0; h < 26; h++) {
                    if (counts[j][h] - counts[i][h] < freq[h]) enough = false;
                }
                if (!enough) j++;
            }
            if (enough) {
                ans = min(ans, j - i);
                i++;
            }
        }
        if (ans == LONG_MAX) cout << -1 << "\n";
        else cout << ans << "\n";
    }
    
    return 0;
}