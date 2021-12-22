//경로찾기-Floyd-Warshall Algorithm
//플로이드 와샬 알고리즘 설명
//https://ansohxxn.github.io/algorithm/floyd

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100

int N;
int graph[MAX][MAX];

void floyd() {

	for (int k = 0; k < N; k++) { //k는 거쳐가는 정점
		for (int i = 0; i < N; i++) { //i는 행(출발 정점)
			for (int j = 0; j < N; j++) { //j는 열(도착 정점)
				if (graph[i][k] && graph[k][j]) { 
					graph[i][j] = 1;
					//i번째 줄 j번째 숫자가 1인경우 i에서 j로 가는 간선이 존재한다는 뜻을
					//두 정점이 1이면 그사이가 간선이 되므로 1로 바꿔줌...
					//잘 이해한게 맞을까?
				}
			}
		}
	}
}
int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> graph[i][j];
		}
	}
	floyd();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << graph[i][j]<<" ";
		}
		cout << '\n';
	}
}