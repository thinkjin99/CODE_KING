#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
string site, password;
vector<pair<string, string>> list;

int search(int l, int r, string a) {
	int mid = (l + r) / 2;  //기준점을 중앙으로 잡는다.
	if (list[mid].first == a) return mid;

	//return list[mid].first >= a ? search(l, mid, a) : search(mid + 1, r, a);

	if (list[mid].first >=a){
	    return search(l, mid, a);
	}
	else
	    return search(mid+1, r, a);

	//이거는 내가 아는걸로 바꾸고싶은데
	//list가 오름차순으로 정렬되어있으니까
	//중앙에 위치한 site보다 작으면 앞쪽, 크면 뒤쪽을 찾는다.
}
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	//cout, cin의 성능을 빠르게 만들어주는 역할

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> site >> password;
		list.push_back({ site, password });
	}
	sort(list.begin(), list.end());
	//list를 오름차순으로 정렬해줌.
	//왜일까?

	for (int i = 0; i < m; i++) {
		cin >> site;
		int x = search(0, n - 1, site);
		//search 함수를 통해 list처음부터 끝까지 입력받은 site와 저장되어있는 site 비교
		cout << list[x].second << '\n';
		//list의 password만 출력
	}
}

//소감: c++만 익숙해지면 할만한 문제였다. 어렵지 않았다.
