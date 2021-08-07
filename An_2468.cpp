#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int mat[101][101];
int check[101][101] = { 0, };

void DFS(int x, int y, int h) {
	check[x][y] = 1;
	if (mat[x + 1][y] > h && !check[x + 1][y])
		DFS(x + 1, y, h);
	if (mat[x][y + 1] > h && !check[x][y + 1])
		DFS(x, y + 1, h);
	if (mat[x - 1][y] > h && !check[x - 1][y])
		DFS(x - 1, y, h);
	if (mat[x][y - 1] > h && !check[x][y - 1])
		DFS(x, y - 1, h);
}

int main() {
	int N, min = 1000, max = 0, count = 0, result = 1;
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			cin >> mat[i][j];
			if (max < mat[i][j]) max = mat[i][j];
			if (min > mat[i][j]) min = mat[i][j];
		}
	for (int k = min; k < max; k++) {
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (mat[i][j] > k && !check[i][j]) {
					DFS(i, j, k);
					count++;
				}
		for(int l = 0; l < N; l++)
			fill_n(check[l], N, 0);
		if (result < count)
			result = count;
		count = 0;
	}
	cout << result;
}