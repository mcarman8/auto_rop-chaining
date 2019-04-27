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
	cout << "Enter the password: ";
	cin >> s1;
	if (s1.compare(this->password) == 0) {
		cout << "Access allowed!" << endl;
		return 0;
	} else {
		cout << "Access denied!" << endl;
		return 1;
	}
}


int main() {
	Access a("unlock");

	return a.unlock();
}
