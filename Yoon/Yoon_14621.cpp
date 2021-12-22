//나만 안되는 연애
//에휴 솔루션 봐도 어디가 틀린지 모르겟다 ㅠ
//결과 13 나옴...ㅠㅠㅠㅠㅠㅠㅠ
//https://conkjh032.tistory.com/m/345?category=935025
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M; //학교수, 도로의 개수
vector<char> univ; //남대, 여대
vector<pair<pair<int,int>,int>> edge;
int u, v, d;//u학교와 v학교 d는 거리
//int parent[1000];
vector<int> parent;

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

	else return false;
}

bool sameGender(int a, int b) {
	if (univ[a] == univ[b]) return false;
	else return true;
}

void Union(int a, int b) {
	a = findParent(a);
	b = findParent(b); 

	if (a > b) parent[a] = b;

	else parent[b] = a;
}

bool compare(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b) {
	return a.second < b.second;
	//distance 비교
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	univ.resize(N + 1); //입력 오류가나서 찾아보니 사이즈를 1 늘려주었다.
	parent.resize(N + 1);

	// 성별 입력
	for (int i = 1; i <= N; i++) {
		cin >> univ[i];
	}
	
	for (int i = 0; i < M; i++) {
		cin >> u >> v >> d;
		edge.push_back(make_pair(make_pair(u,v),d));
	}

	for (int i = 1; i <=N; i++) {
		parent[i] = i;
	}
	sort(edge.begin(), edge.end(), compare);

	int sum = 0;
	//부모가 다르고 다른 성별이면 union, 거리 더하기.
	for (int i = 0; i < edge.size(); i++) {

		if (!sameParent(edge[i].first.first, edge[i].first.second) 
			&& sameGender(edge[i].first.first,edge[i].first.second)) {
			Union(edge[i].first.first, edge[i].first.second);
			sum += edge[i].second;
		}

	}

	//모두 연결되었는지 확인
	int p = parent[1];
	for (int i = 1; i <= N; i++) {
		if (findParent(i) != p) {
			cout << -1 << "\n";
			return 0;
		}
	}

	cout << sum << "\n";

	return 0;
}