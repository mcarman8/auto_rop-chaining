#include <iostream>
#include <string>

using namespace std;

class Access {
	private:
		string password;
	public:
		Access(string p = "THEPASSWORD");
		int unlock();
};

Access::Access(string p) {
	this->password = p;
}

int Access::unlock() {
	string s1;
	char c;
	cout << "Enter the password: ";
	cin >> s1;
	cin.ignore();
	if (s1.compare(this->password) == 0) {
		cout << "Access allowed!" << endl;
		return 0;
	} else {
		cout << "Access denied!" << endl;
		return 1;
	}
}

class SpecialAccess:public Access {
	public:
		int unlock();
};

int SpecialAccess::unlock() {
	int v;
	cout << "Enter the password: ";
	cin >> v;
	if (v == 'A') {
		cout << "Access allowed!" << endl;
		return 0;
	} else {
		cout << "Access denied!" << endl;
		return 1;
	}
}

int main() {
	int rv = 0;
	Access a("unlock");
	SpecialAccess sa;

	rv += a.unlock();
	rv += sa.unlock();

	return rv; 
}
