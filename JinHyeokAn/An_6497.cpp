#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parent[200001];

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
	if (u < v) parent[v] = u;
	else if (u > v) parent[u] = v;
}

int compare(edge& a, edge& b) {
	return a.weight < b.weight;
}

int main() {
	while (1) {
		int V, E, st, fi, we;
		long long int result = 0, all = 0;
		vector<edge> v;
		cin >> V >> E;
		if (V == 0 && E == 0) break;
		for (int i = 0; i < V; i++)
			parent[i] = i;
		for (int i = 0; i < E; i++) {
			cin >> st >> fi >> we;
			all += we;
			v.push_back(edge(st, fi, we));
		}
		sort(v.begin(), v.end(), compare);
		for (int i = 0; i < v.size(); i++) {
			if (root(v[i].u) != root(v[i].v)) {
				merge(v[i].u, v[i].v);
				result += v[i].weight;
			}
		}
		cout << all - result << endl;
	}
}