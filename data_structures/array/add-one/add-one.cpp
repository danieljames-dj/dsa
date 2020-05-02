#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, carry = 1;
	cout << "Enter number of digits: " << endl;
	cin >> n;
	vector<int> number(n);
	cout << "Input number with space between digits: " << endl;
	for (int i = 0; i < n; i++) {
		cin >> number[i];
	}
	for (int i = n - 1; i >= 0; i--) {
		number[i] += carry;
		carry = number[i] / 10;
		number[i] = number[i] % 10;
		if (carry == 0) {
			break;
		}
	}
	if (carry != 0) {
        number.insert(number.begin(), carry);
    }
    while (number[0] == 0) {
        number.erase(number.begin());
    }
	for (int i = 0; i < number.size(); i++) {
		cout << number[i];
	}
	cout << endl;
	return 0;
}