//별자리 만들기-MST
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
#define MAX 1000

vector<pair<double, double>> star;
vector<pair<double, pair<int, int>>> edge;
float parent[MAX];
int ranks[MAX];
double ans;

int findParent(int v) { 
	if (v == parent[v]) {
		return v;
	}
	return parent[v] = findParent(parent[v]);
}

bool sameParent(int a, int b) {
	a = findParent(a);
	b = findParent(b);
	if (a == b) return true;

	return false;
}

void Union(int a, int b) {
	a = findParent(a);
	b = findParent(b);

	parent[b] = a;
}

double Distance(double x, double y, double xx, double yy) {
	double dx = (x - xx) * (x - xx);
	double dy = (y - yy) * (y - yy);
	double distance = sqrt(dx + dy);

	return distance;
}


int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n;
	double a, b;
	double distance;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		star.push_back(make_pair(a, b));
	}

	for (int i = 0; i < n; i++) {
		double x = star[i].first;
		double y = star[i].second;

		for (int j = i + 1; j < n; j++) {
			double xx = star[j].first;
			double yy = star[j].second;

			distance = Distance(x, y, xx, yy);
			edge.push_back(make_pair(distance, make_pair(i, j)));
		}
	}

	for (int i = 0 ; i < n; i++) {
		parent[i] = i;
	}

	sort(edge.begin(), edge.end());

	for (int i = 0; i < n; i++) {
		double cost = edge[i].first;
		int node1 = edge[i].second.first;
		int node2 = edge[i].second.second;

		if (sameParent(node1, node2) == false) {
			Union(node1, node2);
			ans = ans + cost;
		}
	}
	cout << fixed;
	cout.precision(2);
	cout << ans << endl;
	return 0;
}