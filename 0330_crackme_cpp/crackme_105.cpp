#include <iostream>
#include <string>

using namespace std;

class Access {
	private:
		string password;
	public:
		Access(string p = "THEPASSWORD");
		virtual int unlock();
		string getPassword() { return this->password; };
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
		SpecialAccess(string p): Access(p) {};
		int unlock();
};

int SpecialAccess::unlock() {
	int v;
	cout << "Enter the password: ";
	cin >> v;
	if (v == this->getPassword()[0]) {
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
	SpecialAccess sa("unlock");
	Access * aPtr;

	aPtr = &a;
	rv += aPtr->unlock();
	aPtr = &sa;
	rv += aPtr->unlock();

	return rv; 
}
