#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>

using namespace std;

int parent[101];

typedef struct edge {
	int u, v;
	double weight;
	edge(int u, int v, double weight) {
		this->u = u;
		this->v = v;
		this->weight = weight;
	}
};

int compare(edge& a, edge& b) {
	return a.weight < b.weight;
}

int root(int x) {
	if (parent[x] = x) return x;
	return parent[x] = root(x);
}

void merge(int u, int v) {
	u = root(u);
	v = root(v);
	parent[u] = v;
}

int main() {
	int N;
	double x, y, result = 0;
	vector<pair<double, double>> code;
	vector<edge> v;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> x >> y;
		code.push_back(make_pair(x, y));
	}
	for (int i = 1; i <= N; i++)
		parent[i] = i;
	for (int i = 0; i < code.size() - 1; i++)
		for (int j = i + 1; j < code.size(); j++)
			v.push_back(edge(i + 1, j + 1, sqrt(pow(code[i].first - code[j].first, 2) + pow(code[i].second - code[j].second, 2))));
	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < v.size() - 1; i++) {
		if (root(v[i].u) != root(v[i].v)) {
			merge(v[i].u, v[i].v);
			result += v[i].weight;
		}
	}
	cout << fixed;
	cout.precision(2);
	cout << result;
}