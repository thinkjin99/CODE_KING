//9205.맥주 마시면서 걸어가기-DFS

#include <iostream>
#include <vector>
#include <vector>
#include <cstring>
using namespace std;

const int MAX = 100 + 2;
int t;
int n;
float x, y;
bool visited[MAX]; 
vector<int> map[MAX]; //간선 표시된 그래프

//맨해튼 거리: 두 좌표 사이의 거리는 x좌표의 차이 + y좌표의 차이
int distance(pair<int, int>v1, pair<int, int>v2) {
	return abs(v1.first - v2.first) + abs(v1.second - v2.second);
}

void DFS(int n) {
	visited[n] = true;

	for (int i = 0; i < map[n].size(); i++) {
		int next = map[n][i];
		if (visited[next] == false) { //방문하지 않았으면 DFS
			DFS(next);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t; //테스트 케이스

	for(int i=0;i<t;i++) { //map과 visited 초기화
		for (int j = 0; j < MAX; j++) {
			map[j].clear();
		}
		memset(visited, false, sizeof(visited));

		cin >> n; //편의점 개수
		vector<pair<int, int>> xygraph; //좌표 벡터

		for (int j = 0; j < n + 2; j++) {
			cin >> x >> y;
			xygraph.push_back(make_pair(x, y));
		}

		for (int j = 0; j < n + 2; j++) {
			for (int k = j + 1; k < n + 2; k++) {
				if (distance(xygraph[j], xygraph[k]) <= 50 * 20) {
					//맥주 1병으로 50m 갈 수 있고, 최대 20병까지 가지고 있을 수 있으니까
					//한번에 1000m까지 갈 수 있음
					//양방향 그래프로 만들어줌
					map[j].push_back(k);
					map[k].push_back(j);
				}
			}
		}
		DFS(0);
		//도착지점 n+1에 갈 수 있으면
		if (visited[n + 1]==1) {
			cout << "happy\n";
		}
		else
			cout << "sad\n";
	}
	return 0;
}