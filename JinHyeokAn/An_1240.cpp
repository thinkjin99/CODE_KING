#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define INF 999999999

vector<pair<int, long long>> node[2000]; //vector 인덱스 시작점
long long result[2000];

void dijkstra(int start) {
	priority_queue<pair<long long, int>> pq;
	pq.push({ 0,start }); //{최소거리, end}
	result[start] = 0;
	while (!pq.empty()) {
		int now = pq.top().second; //node
		long long dis = -pq.top().first; //현재 거리
		pq.pop();
		for (int i = 0; i < node[now].size(); i++) {
			int next = node[now][i].first;
			int edge = node[now][i].second;
			if (edge + dis < result[next]) {
				result[next] = edge + dis;
				pq.push({ -result[next], next }); //방문 처리 위해서 -
			}
		}
	}
}

int main() {
	int N, M, start, end, weight;
	cin >> N >> M;
	for (int i = 0; i < N - 1; i++) { //edge 입력
		cin >> start >> end >> weight;
		node[start].push_back({ end, weight });
		node[end].push_back({ start, weight });
	}
	for (int j = 0; j < M; j++) {
		cin >> start >> end;
		for (int k = 0; k <= N; k++) result[k] = INF; //무한대 초기화
		dijkstra(start); //start에 대한 모든 최단거리
		cout << result[end] << endl;
	}
}
//2시간 12분