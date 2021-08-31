#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parent[1001];

struct edge {
	int u, v, weight;
	edge(int u, int v, int weight) {
		this->u = u;
		this->v = v;
		this->weight = weight;
	}
};

int root(int x) {
	if (parent[x] == x)return x;
	return parent[x] = root(parent[x]);
}

void merge(int u, int v) {
	u = root(u);
	v = root(v);
	parent[v] = u;
}

int compare(edge& a, edge& b) {
	return a.weight < b.weight;
}

int main() {
	int V, E, st, fi, we, result = 0;
	vector<edge> v;
	cin >> V;
	cin >> E;
	for (int i = 1; i <= V; i++)
		parent[i] = i;
	for (int i = 0; i < E; i++) {
		cin >> st >> fi >> we;
		v.push_back(edge(st, fi, we));
	}
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < v.size(); i++) {
		if (root(v[i].u) != root(v[i].v)) {
			merge(v[i].u, v[i].v);
			result += v[i].weight;
		}
	}
	cout << result;
}