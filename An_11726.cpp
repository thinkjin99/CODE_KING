#include <iostream>
using namespace std;

long long int num[1001] = { 0, };

int main() {
	int N;
	num[1] = 1; num[2] = 2;
	cin >> N;
	for (int i = 3; i <= N; i++) num[i] = num[i - 1] % 10007 + num[i - 2] % 10007;
	cout << num[N] % 10007;
}