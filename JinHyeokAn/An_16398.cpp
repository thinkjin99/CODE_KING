#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int parent[10001];

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
	vector<edge> v;
	int N, number;
	long long result = 0;
	cin >> N;
	for (int i = 0; i < N; i++)
		parent[i] = i;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> number;
			if(i != j)
				v.push_back(edge(i, j, number));
		}
	}
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < v.size(); i++) {
		if (root(v[i].u) != root(v[i].v)) {
			merge(v[i].u, v[i].v);
			result += v[i].weight;
		}
	}
	cout << result << endl;
}