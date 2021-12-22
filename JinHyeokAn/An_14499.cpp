#include <iostream>
using namespace std;

int dice[7] = { 0, };
int map[21][21] = { 0, };

int main() {
	int N, M, x, y, K, num;
	cin >> N >> M >> y >> x >> K;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			cin >> num;
			map[i][j] = num;
		}
	for (int i = 0; i < K; i++) {
		cin >> num;
		int nx = x, ny = y, tmp = 0;
		if (num == 1) nx++;
		else if (num == 2) nx--;
		else if (num == 3) ny--;
		else if (num == 4) ny++;
		if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
			if (num == 1) {
				tmp = dice[4]; dice[4] = dice[6]; dice[6] = dice[2]; dice[2] = dice[3]; dice[3] = tmp;
			}
			else if (num == 2) {
				tmp = dice[4]; dice[4] = dice[3]; dice[3] = dice[2]; dice[2] = dice[6]; dice[6] = tmp;
			}
			else if (num == 3) {
				tmp = dice[1]; dice[1] = dice[6]; dice[6] = dice[5]; dice[5] = dice[3]; dice[3] = tmp;
			}
			else if (num == 4) {
				tmp = dice[1]; dice[1] = dice[3]; dice[3] = dice[5]; dice[5] = dice[6]; dice[6] = tmp;
			}
			if (map[ny][nx] == 0) map[ny][nx] = dice[3];
			else {
				dice[3] = map[ny][nx];
				map[ny][nx] = 0;
			}
			cout << dice[6] << endl;
			x = nx; y = ny;
		}
	}
}