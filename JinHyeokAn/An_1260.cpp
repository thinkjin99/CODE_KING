#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void DFS(int st, vector<int> graph[], int check[]) {
	check[st] = 1;
	cout << st << " ";
	for (int i = 0; i < graph[st].size(); i++) {
		int nx = graph[st][i];
		if (check[nx] == 0)
			DFS(nx, graph, check);
	}
}

void BFS(int st, vector<int> graph[], int check[]) {
	queue<int> q;
	q.push(st);
	check[st] = 1;
	while (!q.empty()) {
		int t = q.front();
		q.pop();
		cout << t << " ";
		for (int i = 0; i < graph[t].size(); i++) {
			if (check[graph[t][i]] == 0) {
				q.push(graph[t][i]);
				check[graph[t][i]] = 1;
			}
		}
	}
}

int main() {
	int N, M, start;
	int* check_d, * check_b;
	cin >> N >> M >> start;
	vector<int> * graph = new vector<int>[N + 1];
	check_d = (int*)calloc(N + 1, sizeof(int));
	check_b = (int*)calloc(N + 1, sizeof(int));

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 1; i <= N; i++)
		sort(graph[i].begin(), graph[i].end());
	DFS(start, graph, check_d);
	cout << "\n";
	BFS(start, graph, check_b);
}