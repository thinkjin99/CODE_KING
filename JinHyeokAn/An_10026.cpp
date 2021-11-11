#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int mat[101][101];
int check[101][101] = { 0, };

void DFS(int x, int y, int h) {
	check[x][y] = 1;
	if (mat[x + 1][y] == h && !check[x + 1][y])
		DFS(x + 1, y, h);
	if (mat[x][y + 1] == h && !check[x][y + 1])
		DFS(x, y + 1, h);
	if (mat[x - 1][y] == h && !check[x - 1][y])
		DFS(x - 1, y, h);
	if (mat[x][y - 1] == h && !check[x][y - 1])
		DFS(x, y - 1, h);
}

int main() {
	int N, count = 0, result = 1;
	char alpa;
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			cin >> alpa;
			if (alpa == 'R') mat[i][j] = 1;
			else if (alpa == 'G') mat[i][j] = 2;
			else if (alpa == 'B') mat[i][j] = 3;
		}
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (!check[i][j]) {
				DFS(i, j, mat[i][j]);
				count++;
			}
	cout << count << endl;
	count = 0;
	for (int l = 0; l < N; l++)
		fill_n(check[l], N, 0);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (mat[i][j] == 1)
				mat[i][j] = 2;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (!check[i][j]) {
				DFS(i, j, mat[i][j]);
				count++;
			}
	cout << count;
}