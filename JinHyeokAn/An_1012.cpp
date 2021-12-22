#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int mat[51][51] = { 0, };
int check[51][51] = { 0, };

void DFS(int x, int y) {
	check[x][y] = 1;
	if (mat[x + 1][y] == 1 && !check[x + 1][y])
		DFS(x + 1, y);
	if (mat[x][y + 1] == 1 && !check[x][y + 1])
		DFS(x, y + 1);
	if (mat[x - 1][y] == 1 && !check[x - 1][y])
		DFS(x - 1, y);
	if (mat[x][y - 1] == 1 && !check[x][y - 1])
		DFS(x, y - 1);
}

int main() {
	int T, M, N, K, y, x, count = 0;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M >> K;
		for (int j = 0; j < K; j++) {
			cin >> x >> y;
			mat[x][y] = 1;
		}
		for (int j = 0; j < M; j++) 
			for (int k = 0; k < N; k++) 
				if (mat[k][j] == 1 && !check[k][j]) {
					DFS(k, j);
					count++;
				}
		cout << count << endl;
		count = 0;
		for (int l = 0; l < N; l++)
			fill_n(check[l], M, 0);
		for (int l = 0; l < N; l++)
			fill_n(mat[l], M, 0);
	}
}