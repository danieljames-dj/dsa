#include <iostream>
#include <cctype>

using namespace std;

int main() {
    int t, dig, a[101], b[101], aTop, bTop;
    char n;
    cin >> t;
    cin.ignore();
    for (int i = 1; i <= t; i++) {
        aTop = bTop = 0;
        while (1) {
            cin.get(n);
            if (!isdigit(n)) {
                break;
            }
            dig = n - '0';
            if (dig == 4) {
                a[aTop++] = 2;
                b[bTop++] = 2;
            } else {
                a[aTop++] = dig;
                b[bTop++] = 0;
            }
        }
        cout << "Case #" << i << ": ";
        for (int j = 0; j < aTop; j++) {
            cout << a[j];
        }
        cout << " ";
        for (int j = 0; j < bTop; j++) {
            cout << b[j];
        }
        cout << endl;
    }
    return 0;
}