#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100001

int v, e;
int A, B, C;
int parent[MAX];

struct Edge { //정점 2개와 가중치
	int u, v, weight;
	Edge(int u, int v, int weight) {
		this->u=u;
		this->v = v;
		this->weight = weight;
	}
	
};
int findParent(int v) {
	if (parent[v] == v) { //현재 노드가 집합의 루트면
		//자신이 속한 집합을 찾았으므로 node반환
		return v;
	}
	//아니라면 노드의 루트에 대해 재귀 호출하면서 parent 업데이트
	return parent[v] = findParent(parent[v]);

}
//집합을 합침
void merge(int u, int v) {
	u = findParent(u);
	v = findParent(v);

	parent[v] = u;
}

int compare(Edge& a, Edge& b) {
	return a.weight < b.weight;
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	vector<Edge> edge;
	int result=0 ;

	cin >> v >> e;

	for (int i = 0; i < v; i++) {
		parent[i] = i;
	}
	for (int i = 0; i < e; i++) {
		cin >> A >> B >> C;
		edge.push_back(Edge(A, B, C));
	}
	sort(edge.begin(), edge.end(),compare);
	for (int i = 0; i < edge.size(); i++) {
		if (findParent(edge[i].u) != findParent(edge[i].v)) {
			merge(edge[i].u, edge[i].v);
			result += edge[i].weight;
		}
	}

	cout << result << '\n';

	return 0;
}