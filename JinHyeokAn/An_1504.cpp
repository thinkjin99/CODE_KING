#include <iostream>
using namespace std;

#define INF 10000000

int mat[801][801];

int main() {
	int N, M, st, fi, w, v1, v2, result1 = INF, result2 = INF, result;

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			mat[i][j] = INF;

	for (int i = 0; i < M; i++) {
		cin >> st >> fi >> w;
		mat[st][fi] = w;
		mat[fi][st] = w;
	}

	cin >> v1 >> v2;

	for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) {
				if (mat[i][k] + mat[k][j] < mat[i][j])
					mat[i][j] = mat[i][k] + mat[k][j];
			}

	if (mat[1][v1] != INF && mat[v1][v2] != INF && mat[v2][N] != INF)
		result1 = mat[1][v1] + mat[v1][v2] + mat[v2][N];
	if (mat[1][v2] != INF && mat[v2][v1] != INF && mat[v1][N] != INF)
		result2 = mat[1][v2] + mat[v2][v1] + mat[v1][N];
	
	result = min(result1, result2);
	if (result == INF)
		cout << -1;
	else
		cout << result;
}