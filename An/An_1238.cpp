#include <iostream>
using namespace std;

#define INF 100000

int mat[1001][1001];


int main() {
	int N, M, X, st, fi, w, result = 0, move = 0;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M >> X;

	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			mat[i][j] = INF;

	for (int i = 0; i < M; i++) {
		cin >> st >> fi >> w;
		mat[st][fi] = w;
	}

	for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) {
				if (mat[i][k] + mat[k][j] < mat[i][j])
					mat[i][j] = mat[i][k] + mat[k][j];
			}

	for (int i = 1; i <= N; i++) {
		if (i != X) {
			move += mat[i][X];
			move += mat[X][i];
			if (move > result)
				result = move;
			move = 0;
		}
	}
	cout << result;
}