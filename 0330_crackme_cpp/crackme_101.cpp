#include <iostream>
#include <string>

using namespace std;

class Access {
	public:
		int unlock();
};

int Access::unlock() {
	string s1;
	string s2 = "l3tm31n!";
	cout << "Enter the password: ";
	cin >> s1;
	if (s1.compare(s2) == 0) {
		cout << "Access allowed!" << endl;
		return 0;
	} else {
		cout << "Access denied!" << endl;
		return 1;
	}
}

int main() {
	Access a;

	return a.unlock();
}
