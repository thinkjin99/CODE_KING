#include <iostream>
#include <vector>
using namespace std;

int** arr;
int** visited;
int N;
int rain;

// visited 배열 재사용 위한 함수랄까,,,~
void init() {

	visited = new int* [N];
	for (int i = 0; i < N; i++) {
		visited[i] = new int[N];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			visited[i][j] = 0;
		}
	}
}

void dfs(int r, int c) {
	if (arr[r][c] <= rain)
		return;
	if (arr[r][c] > rain && visited[r][c] == 1)	// 피해 없었지만 방문한 곳
		return;
	if (arr[r][c] > rain && visited[r][c] == 0) {	// 피해 없었고 방문 안 한 곳
		visited[r][c] = 1;	// 방문기록 남기고 갑니다요,,,~

		// 여기서 나오는 조건문은 다 충돌검사 위한 거
		// 그리고 상하좌우 재귀로 탐색하기
		if (r - 1 >= 0)
			dfs(r - 1, c);
		if (r + 1 < N)
			dfs(r + 1, c);
		if (c - 1 >= 0)
			dfs(r, c - 1);
		if (c + 1 < N)
			dfs(r, c + 1);
	}

	return;
}

int main() {

	cin >> N;

	int max = 0;

	arr = new int* [N];
	for (int i = 0; i < N; i++)
		arr[i] = new int[N];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
			if (arr[i][j] > max)	// 최대 강수량 구하기
				max = arr[i][j];
		}
	}

	rain = 0;
	int noRain = 0;	// 비 피해 없었던 지역 개수
	
	while (max > rain) {
		init();

		int cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// 더 높은 지역이면서 방문 안 한 곳
				if (arr[i][j] > rain && visited[i][j] == 0) {
					cnt++;	 // 개수 더해주고
					dfs(i, j);	// 거기서부터 탐색할랭
				}
				else;
			}
		}

		if (noRain < cnt)
			noRain = cnt;
		rain++;	// 강수량 늘려주기
	}
	
	cout << noRain;


	return 0;
}
