#include <iostream>
using namespace std;

int mat[101][101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> mat[i][j];

	for(int k = 0; k < N; k++)
		for(int i = 0; i < N; i++)
			for (int j = 0; j < N; j++) {
				if (mat[i][k] == 1 && mat[k][j] == 1)
					mat[i][j] = 1;
			}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cout << mat[i][j] << " ";
		cout << "\n";
	}
}