//좌표 압축
//좌표 압축: 해당 좌표의 값을 그 값보다 작은 좌표값들의 개수로 대체
//문제 이해 안되서 설명 찾아봄

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, x;
vector<int> v, back;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> x;
		v.push_back(x);
		back.push_back(x);
	}

	//중복 원소 제거
	sort(v.begin(), v.end());//오름차순으로 정렬
	v.erase(unique(v.begin(), v.end()), v.end());
	//unique: 중복값을 맨 뒤로 쓰레기값으로 보냄, 끝나면 vector의 쓰레기값의 첫번째 위치가 반환되어
	//erase: 반환된 주소부터 맨 뒤 값까지 제거
	//이렇게 되면 모든 중복 원소를 제거할 수 있다.
	//https://codingwell.tistory.com/26

	for (int i = 0; i < N; i++) {
		int result;
		result=lower_bound(v.begin(), v.end(), back[i]) - v.begin();

		cout << result << ' ';
	}

	return 0;
}