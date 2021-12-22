#include <iostream>
#include <algorithm>
using namespace std;

int dy[4] = { 1,-1,0,0 };
int dx[4] = { 0,0,1,-1 };

char mat[21][21] = { 0, };
int alpha[26] = { 0, };
int result = 0;
int N, M;

void DFS(int y, int x, int cnt) {
	if (result < cnt)
		result = cnt;
	for (int i = 0; i < 4; i++) {
		int ny = y + dy[i];
		int nx = x + dy[i];
		if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
		int k = (int)mat[ny][nx] - 65;
		if (alpha[k]) continue;
		alpha[k]++;
		DFS(ny, nx, cnt + 1);
		alpha[k]--;
	}
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> mat[i][j];
	alpha[(int)mat[0][0] - 65]++;
	DFS(0, 0, 1);
	cout << result << endl;
}