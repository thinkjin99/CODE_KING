//1918.후위 표기식
//후위 표기식: 연산자를 피연산자 뒤에 놓는 방법
//https://woongsios.tistory.com/288
//연산자 우선순위: '(', ')' > '*' , '/' > '+' , '-'
//스택은 후입선출
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string input;
	string result;
	stack <char> op;

	cin >> input;

	for (int i = 0; i < input.size(); i++) {
		if ('A' <= input[i] && 'Z' >= input[i]) {
			result += input[i];
			continue;
		}
		//피연산자들은 result에 저장

		if (input[i] == '(') {
			op.push(input[i]);
			continue;
		}
		//'('인 경우 스택에 추가

		if (input[i] == ')') {
			while (op.top() != '(') {
				result += op.top();
				op.pop();
			}
			op.pop();
			continue;
		}
		//')'인 경우 '('가 나올때까지 result에 저장후 pop

		if (input[i] == '*' || input[i] == '/') {
			while (!op.empty() && (op.top() == '*' || op.top() == '/')) {
				result += op.top();
				op.pop();
			}
		}
		//'*'과 '/'보다 높은 우선순위의 연산자는 없기 때문에 
		//'*'또는 '/'가 top일때 result에 추가

		else {
			while (!op.empty() && op.top() != '(') {
				result += op.top();
				op.pop();
			}
		}
		//'+', '-'일 경우 나머지 연산자들은 자신보다 우선순위가 높거나 같으므로 
		//'('이 나올때까지 result 에 추가
		op.push(input[i]);
		

	}
	while (!op.empty()) {
		result += op.top(); //남은 연산자 result에 추가
		op.pop();
	}
	cout << result << "\n";
	return 0;

}