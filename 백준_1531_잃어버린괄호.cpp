//���� 1531 �Ҿ���� ��ȣ
#include <iostream>//cout, cin
#include <string>
using namespace std; 

int main(void) {

	string input;
	cin >> input;

	int result = 0;
	string num;
	bool isMinus = false;

	for (int i = 0; i <= input.size(); i++) {
		if (input[i] == '-' || input[i] == '+' || i == input.size()) {
			if (isMinus)// ���̳ʽ��� �����Ұ�� true
			{
				result -= stoi(num);
				
				num = "";
				cout << typeid(num).name();
				//printf(typeid(num));
			}
			else {
				result += stoi(num);
				num = "";
			}

		}
		else {
			num += input[i];

		}

		if (input[i] == '-')
		{
			isMinus = true;
		}
	}
	cout << result;
}