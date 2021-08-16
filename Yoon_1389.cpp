//케빈 베이컨의 6단계 법칙-플로이드 와샬

#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 101
using namespace std;

const int INF = 987654321;

int N, M; //유저의 수, 친구 관계의 수
int A, B;
int graph[MAX][MAX];

void floyd() {
	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j) continue;

				else if (graph[i][k] && graph[k][j]) {
					if (graph[i][j] == 0) {
						graph[i][j] = graph[i][k] + graph[k][j]; //베이컨 수
					}
					else
						graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]); //더 적은 베이컨 수로 
				}
			}
		}
	}
}
int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;
	
	for (int i = 0; i < M; i++) {
		cin >> A >> B;
		graph[A][B] = graph[B][A] = 1;
	}

	floyd();

	int result = INF;
	int person=0;

	for (int i = 1; i <= N; i++) {
		int sum = 0;

		for (int j = 1; j <= N; j++) {
			sum += graph[i][j]; //i의 베이컨 수를 더해줌
		}

		if (result > sum) {
			result = sum; //sum(총 베이컨 수)이 가장 작을 때
			person = i;
		}
	}
	cout << person << '\n';
	return 0;
}
