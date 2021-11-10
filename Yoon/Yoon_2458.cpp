//키 순서-플로이드 와샬
//왜 틀린지 모르겠다 ㅠㅠ

#include <iostream>
#include <algorithm>
//#define MAX 502
//#define INF 987654321
using namespace std;

const int INF = 9999999;
const int MAX = 502;
int N, M;
int a, b;
int graph[MAX][MAX];

void floyd() {

	for (int k = 1; k <= N; k++) { //k는 거쳐가는 정점
		for (int i = 1; i <= N; i++) { //i는 행(출발 정점)
			for (int j = 1; j <= N; j++) { //j는 열(도착 정점)
				if (graph[i][j] > graph[i][k] + graph[k][j]) {
					graph[i][j] = graph[i][k] + graph[k][j];
				}
				//graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]); 

			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			graph[i][j] = INF;
		}
	}

	
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		graph[a][b] = 1;
	}
	
	floyd();

	int result = 0;
	int cnt = 0;

	for (int i = 1; i <= N; i++) {
		int cnt = 0;
		for (int j = 1; j <= N; j++) {
			if (graph[i][j] != INF) {
				cnt++;
			}
			if(graph[j][i] != INF) {
				cnt++; //갈 수 있는 노드 수++
			}
		}
		if (cnt == N-1) {//자신 빼고 모두 갈 수 있으면 다 연결되어있다는 뜻으로
			result++; //키가 몇번째인지 알수있는 사람++
		}
	}
	cout << result << endl;
	return 0;
}