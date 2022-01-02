#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> vec;
vector<int> visited;
vector<int> ans;

void dfs(int startNode, int currentNode) {

    if (visited[currentNode]) {
        if (currentNode == startNode)
            ans.push_back(startNode);
    }
    else {
        visited[currentNode]++;
        dfs(startNode, vec[currentNode]);
    }

}
int main() {
    cin >> N;
    vec = vector<int>(N + 1, 0);
    visited = vector<int>(N + 1, 0);
    for (int i = 1; i <= N; i++)
        cin >> vec[i];
    for (int i = 1; i <= N; i++) {
        dfs(i, i);
        visited = vector<int>(N + 1, 0);
    }
    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << endl;
    return 0;
}