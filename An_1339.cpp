#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

char str[10][10];
int alpabet[26][8];
int alpa_num[10] = { 0, };

int al2int(char c) {
	return c - 'A';
}

void find(int number) {
	int count = 0, max = 0, max_in = -1;
	for (int i = 0; i < 26; i++)
		for (int j = 7; j >= 0; j--)
			alpa_num[i] += alpabet[i][j] * pow(10, 7 - j);
	for (int k = 9; k >= 0; k--) {
		for (int i = 0; i < 26; i++)
			if (max < alpa_num[i]) {
				max = alpa_num[i];
				max_in = i;
			}
		if(max_in != -1)
			alpa_num[max_in] = alpa_num[max_in] * k * (-1);
		max = 0;
		max_in = -1;
	}
}

int main() {
	int number, sum = 0;
	cin >> number;
	for (int i = 0; i < number; i++) {
		cin >> str[i];
		for (int j = 0; j < strlen(str[i]); j++)
			alpabet[al2int(str[i][j])][8 - strlen(str[i]) + j]++;
	}
	find(number);
	for (int i = 0; i < 26; i++)
		if(alpa_num[i] != 0)
			sum += alpa_num[i] * (-1);
	cout << sum;
}