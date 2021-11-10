#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 1000
//행성을 모두 연결하는데 최소비용을 구한다!
//크루스칼 알고리즘 사용
//크루스칼 알고리즘 동작 원리
//1. 모든 간선들의 가중치를 오름차순으로 정렬
//2. 가중치가 가장 작은 간선을 선택
//3. 위에서 선택한 간선이 연결하려는 2개의 노드가 서로 연결되지 않은 상태라면 2개 노드를 서로 연결
//4.이 과정을 반복
int N;
int planet[MAX][MAX];
int parent[MAX], ranks[MAX];


int findParent(int v) { //부모 찾음
	if (v == parent[v]) {
		return v;
	}

	return parent[v] = findParent(parent[v]);
}

//집합 합침
void merge(int a, int b) {
	a = findParent(a);
	b = findParent(b); //a와 b의 부모 찾음
	//같으면 루프 발생

	if (a != b) { //a와 b의 부모가 다르면
		if (ranks[a] < ranks[b]) {
			swap(a, b);
		}
		parent[b] = a;
		if (ranks[a] == ranks[b]) {
			ranks[a]++;
		}
	}
}

struct Edge { //구조체 (정점1, 정점2, 가중치), 이건 솔루션찾아봄...
	int u, v, weight;
	bool operator<(Edge const &e) {
		return weight < e.weight; //잘 이해가 되지 않는다..구조체 어렵다..
	}
};

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;

	//행렬 입력받기
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> planet[i][j];
		}
	}
	//정점1->정점2 혹은 정점2->정점1 간선을 하나만 입력받음
	vector<Edge> edge;
	for (int i = 0; i < N; i++) {
		for (int j = i+1; j < N; j++) {
			edge.push_back({ i,j,planet[i][j] });
		}
	}
	//간선의 가중치를 정렬
	sort(edge.begin(), edge.end());
	//초기화
	for (int i = 0; i < N; i++) {
		parent[i] = i;
		ranks[i] = 0;
	}

	long long result = 0;
	//간선 가중치의 최소값을 구함
	for (int i = 0; i < edge.size(); i++) {
		Edge e = edge[i];

		if (findParent(e.u) != findParent(e.v)) {//각각의 정점의 부모가 다르면
			result += e.weight; //e의 가중치 더해줌
			merge(e.u, e.v); // 합침
		}
	}

	cout << result << "\n";
	return 0;
}