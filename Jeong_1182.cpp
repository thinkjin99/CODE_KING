#include<list>
#include<iostream>
using namespace std;
int s;
int cnt = 0;
void makeSubset(list<int> li, int res){
    if(li.size() < 1) return; // 더 이상 가질 수 있는 수가 없을 때
    const int size = li.size(); // pop으로 인해 .size()의 값이 계속 변동됨으로 고정 size를 만든다.
    for(int i = 0; i < size; i++){ //배열의 크기 만큼 반복해준다.
        int front = li.front();
        li.pop_front(); //현재 방문한 경로를 리스트에서 제거
        if(res + front == s) { //res는 이전까지 경로의 합을 의미한다.
            cnt++;    //지금까지 지나온 경로의 합이 비교하고자 하는 수와 같다면 횟수를 증가시킨다.
        }
        makeSubset(li,res + front); //현재 경로의 값을 더 해주고 다음 횟차로 함수를 호출한다.
    }
}

int main(){
    int n; cin >> n;
    cin >> s;
    list<int> li;
    for(int i =0; i < n; i++){
        int e;
        scanf("%d",&e);
        li.push_front(e);
    }
    makeSubset(li,0);
    cout << cnt;
}