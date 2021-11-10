//1238. 파티 - 다익스트라
//N명의 학생들이 x번 마을로 갔다가 다시 자신들의 원래 마을로 돌아오는데
//가장 오래걸리는 학생의 소요시간
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 987654321;
int N, M, X; //학생수, 도로수, 
int a, b, c; //시작점, 끝점, 소요시간
vector<pair<int, int>> map[1001];
int dist[1010];
int res[1010];

void dijkstra(int start) {

	priority_queue<pair<int, int>> pq;
	dist[start] = 0;
	pq.push(make_pair(0, start)); //가중치, 시작정점

	while (pq.empty() == 0) {
		int current = pq.top().second;
		int cost = -pq.top().first; //-를 넣어서 음수값을 넣어 최소값이 먼저 나오도록 함 ->솔루션 봄..

		pq.pop();

		if (dist[current] < cost) continue;

		for (int i = 0; i < map[current].size(); i++) {

			int next = map[current][i].first; //현재 노드 u일때 저장한 v가 다음 노드
			int ncost = map[current][i].second;

			if (ncost + cost < dist[next]) { //현재 가중치와 다음 가중치의 합이 다음 노드의 가중치보다 작으면
				dist[next] = ncost + cost; //다음 노드의 가중치는 합으로 
				pq.push(make_pair(-dist[next], next));
			}
		}
	}
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	//input
	cin >> N >> M >> X;
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> c;
		map[a].push_back(make_pair(b, c));
	}
	
	//dijkstra 실행~
	for (int i = 1; i <= N; i++) {//모든 학생들이 x번 마을로 가는데 걸리는 최단 소요시간 
		for (int j = 1; j <= N; j++) dist[j] = INF;
		dijkstra(i);
		res[i] = dist[X]; //가는 시간 저장
	}

	for (int j = 1; j <= N; j++) dist[j] = INF; 
	dijkstra(X);//x번 마을에서 자신 마을로 가는 최단 소요시간

	//두번 하는 이유는 단방향이기 때문에 갔다가 오는 시간이 같을 보장이 없음.
	//요건 솔루션보고 알았음.....

	int result = 0;
	for (int i = 1; i <= N; i++) {
		res[i] += dist[i]; //가는시간에 오는시간 더해서 저장
		result = max(result, res[i]); //가장 큰 값 출력

	}

	cout << result;
	
}