#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX 100
//색상이 상하좌우로 인접해 있는 경우가 같은 구역.
//예시 보면 처음 R이 같은 구역, 다음 B가 같은 구역.
//G가 같은 구역, R이 같은구역-> 총 4
//G를 모두 R이라고 하면
//중간에 있는 B를 제외하고 R-B-R순서대로 BFS ->총 3

int N;
char map[MAX][MAX];
int visit[MAX][MAX];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

void bfs(int a, int b) {

	queue < pair<int, int >> q;
	q.push(make_pair(a, b));
	visit[a][b] = true;

	while (q.empty() == 0) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
            //상하좌우 방문
			if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
				if (visit[nx][ny] == false) {
					if (map[nx][ny] == map[x][y]) {
						visit[nx][ny] = true;
						q.push(make_pair(nx, ny));
					}
				}
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N;

    //입력
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}

    int Answer, Answer2; //처음, 적록색양인 경우

    Answer = Answer2 = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (visit[i][j] == false)
            {
                bfs(i, j);
                Answer++;
                //cout << i << j << '\n';

            }
        }
    }

    //적록색양인 경우 초록색와 빨간색을 구분할 수 없으므로 G를 R로 바꿈
    memset(visit, false, sizeof(visit));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){

            if (map[i][j] == 'G') map[i][j] = 'R';
        }
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){

            if (visit[i][j] == false)
            {
                bfs(i, j);
                Answer2++;
               // cout << i << j << '\n';
            }
        }
    }

    cout << Answer << " " << Answer2 << endl;



	return 0;
}

// 참고  https://yabmoons.tistory.com/55 