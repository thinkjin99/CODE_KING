#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	string* arr = new string[51];
	for (int i = 0; i < N; i++) {
		string temp;
		cin >> temp;
		// 단어의 끝 구분하기 위해 . 추가했음
		arr[temp.length()] += (temp + ".");
	}

	for (int i = 1; i < 51; i++) {
		// 해당 위치에 단어가 하나라도 있을 경우 아래 코드 진입
		if (arr[i].length() != 0) {
			vector<string> v;
			string temp;
			for (int j = 0; j < arr[i].length(); j++) {
				// 배열 안에 있는 단어 가져오기 위해...
				if (arr[i][j] != '.')
					temp += arr[i][j];
				else {
					int check = 1;	// 중복되는 단어 있는지 확인 위한 변수
					// 중복된 단어 있는지 확인
					for (int k = 0; k < v.size(); k++) {
						if (v[k] == temp) {
							check = 0;
							break;
						}
					}
					if(check==1)	// 없으면 단어 목록에 추가
						v.push_back(temp);
					temp = "";
				}
			}
			sort(v.begin(), v.end());	// 히히,,,
			for (int j = 0; j < v.size(); j++) {	// 단어 목록 출력하기
				cout << v[j] << "\n";
			}
		}
	}


	return 0;
}
