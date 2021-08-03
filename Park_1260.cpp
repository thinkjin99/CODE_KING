#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, V;
vector<int> visitedD(1001);	// DFS 위한 visited

void dfs(vector<vector<int>> v, int start) {
	visitedD[start] = 1;
	cout << start << " ";
	for (int i = 0; i < v[start].size(); i++) {
		int key = v[start][i];
		if (visitedD[key] == 0) {	// 방문하지 않았을 경우
			dfs(v, key);
		}
		else
			;
	}
}

void bfs(vector<vector<int>> v) {
	vector<int> visited(N + 1);

	queue<int> q;	// 큐 선언
	q.push(V);	// 하나씩 뒤에 넣어줌
	visited[V] = 1;	// 방문 확인

	while (!q.empty()) {	// 종료조건을 잘 생각해야함!
		int start = q.front();	// 큐의 앞대가리를 대상으로 그래프 확인
		cout << start << " ";
		q.pop();
		
		for (int i = 0; i < v[start].size(); i++) {
			int key = v[start][i];
			if (visited[key] == 0) {	// 방문하지 않았을 경우
				q.push(key);	// 큐에 넣어줌
				visited[key] = 1;
			}
			else;
		}
	}
}

int main() {

	cin >> N >> M >> V;

	vector<vector<int>> v(N+1);

	// 2차원 벡터에 넣어줬음
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	// 같을 때 숫자가 작은 것부터 탐색하기로 했으니깐,,, 정렬
	for (int i = 1; i <= N; i++)
		sort(v[i].begin(), v[i].end());

	dfs(v, V);
	cout << "\n";
	bfs(v);

	return 0;
}
