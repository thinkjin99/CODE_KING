#include <iostream>
using namespace std;

char** arr;
int** visited;
int N;

void initVisit(int size) {
	visited = new int* [size];
	for (int i = 0; i < size; i++)
		visited[i] = new int[size];

	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			visited[i][j] = 0;
}

void dfs(int r, int c, char color) {
	if (arr[r][c] != color)
		return;
	if (arr[r][c] == color && visited[r][c] == 1)
		return;

	visited[r][c] = 1;
	if (r >= 1)
		dfs(r - 1, c, color);
	if (r < N - 1)
		dfs(r + 1, c, color);
	if (c >= 1)
		dfs(r, c - 1, color);
	if (c < N - 1)
		dfs(r, c + 1, color);

	return;
}

int main() {

	cin >> N;
	
	arr = new char* [N];
	for (int i = 0; i < N; i++)
		arr[i] = new char[N];

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> arr[i][j];
	initVisit(N);

	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) {
				cnt++;
				dfs(i, j, arr[i][j]);
			}
		}
	}

	cout << cnt << " ";

	// 걍 적록 상황을 바꿔줌
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j] == 'R')
				arr[i][j] = 'G';
		}
	}

	initVisit(N);
	cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) {
				cnt++;
				dfs(i, j, arr[i][j]);
			}
		}
	}

	cout << cnt;

	return 0;
}
