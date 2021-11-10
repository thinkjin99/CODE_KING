#include <stdio.h>
#include <iostream>
#include <tuple>
#include <queue>
using namespace std;

int war[101][101][101] = { 0, };
int visit[101][101][101] = { 0, };

int main() {
	int M, N, H;
	cin >> M >> N >> H;
	queue<tuple<int, int, int>> q;
	for (int h = 0; h < H; h++) 
		for (int r = 0; r < N; r++) 
			for (int c = 0; c < M; c++) {
				cin >> war[h][r][c];
				if (war[h][r][c] == 1)
					q.push(make_tuple(h, r, c));
				if (war[h][r][c] == 0)
					visit[h][r][c] = -1;
			}

	int dx[6] = { 0, 0, -1, 1, 0, 0 };
	int dy[6] = { 1, -1, 0, 0, 0, 0 };
	int dz[6] = { 0, 0, 0, 0, 1, -1 };

	tuple<int, int, int> tmp;
	int nx, ny, nz, x, y, z;
	int result = -1;
	while (q.size() != 0) {
		tmp = q.front();
		q.pop();
		z = get<0>(tmp);
		x = get<1>(tmp);
		y = get<2>(tmp);
		for (int j = 0; j < 6; j++) {
			nz = z + dz[j];
			nx = x + dx[j];
			ny = y + dy[j];
			/*if (0 <= nx && nx < N && 0 <= ny && ny < M && 0 <= nz && nz < H) {
				if (!visit[ny][nx][nz] && war[nz][nx][ny] == 0) {
					war[nz][nx][ny] = 1;
					q.push(make_tuple(nz, nx, ny));
				}
			}*/
			if (nx < 0 || nx >= N || ny < 0 || ny >= M || nz < 0 || nz >= H) continue;
			if (visit[nz][nx][ny] >= 0) continue;
			visit[nz][nx][ny] = visit[z][x][y] + 1;
			q.push(make_tuple(nz, nx, ny));
		}
	}

	for (int h = 0; h < H; h++) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (visit[h][r][c] == -1) {
					cout << "-1";
					return 0;
				}
				result = max(result, visit[h][r][c]);
			}
		}
	}

	cout << result;
}