#include <iostream>
using namespace std;

int** visited;
int** arr;
int M, N;

// visited랑 arr배열 재사용 위해 초기화해주는 함수
void init(int row, int col) {
	visited = new int* [row];
	arr = new int* [row];

	for (int i = 0; i < row; i++) {
		visited[i] = new int[col];
		arr[i] = new int[col];
	}

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			visited[i][j] = 0;
			arr[i][j] = 0;
		}
	}
}

void dfs(int r, int c) {
	if (arr[r][c] == 0)	// 배추 없잖아!
		return;
	if (arr[r][c] == 1 && visited[r][c] == 1)	// 배추 있는데 이미 방문한 곳
		return;
	if (arr[r][c] == 1 && visited[r][c] == 0) {	// 배추 있는데 아직 방문을 안 했네!
		visited[r][c] = 1;	// 방문기록 남기고 갑니다요,,,~

		// 여기서 나오는 조건문은 다 충돌검사 위한 거
		// 그리고 상하좌우 재귀로 탐색하기
		if (r - 1 >= 0)
			dfs(r - 1, c);
		if (r + 1 < N)
			dfs(r + 1, c);
		if (c - 1 >= 0)
			dfs(r, c - 1);
		if (c + 1 < M)
			dfs(r, c + 1);
	}

	return;
}

int main() {

	int T;
	cin >> T;

	while (T--) {
		int K;

		// ㅋㅋ 아니 보통 행-열 이렇게 주는데 얘넨 반대로 주더라
		cin >> M >> N >> K;

		// 난 열-행보단 행-열맨이라 ㅎㅅㅎ
		init(N, M);
		int cnt = 0;

		for (int i = 0; i < K; i++) {
			int x, y;
			cin >> x >> y;
			arr[y][x] = 1;	// 배추 있는 곳 위치 표시
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				// 배추 있는데 방문 안 한 곳만
				if (arr[i][j] == 1 && visited[i][j] == 0) {
					cnt++;	 // 개수 더해주고
					dfs(i, j);	// 거기서부터 탐색할랭
				}
				else;
			}
		}

		cout << cnt << "\n";

	}


	return 0;
}
