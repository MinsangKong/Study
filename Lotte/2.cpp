2.
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define NM 35
using namespace std;
int cnt[1000000];
int a[NM][NM];
int N, M;
void Input() {
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> a[i][j];
        }
    }
}
#include <queue>
int dir[4][2] = { {1,0},{0,1},{-1,0},{0,-1} };
int flooded[NM][NM];
void Flooding(int height) {  // 해수면 높이가 heigth라고 생각했을 때, 침수되는 위치 찾기
    queue<int> Q;
    // 테두리에 대해서 침수되는 위치 찾기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (i == 1 || i == N || j == 1 || j == M) {
                flooded[i][j] = 0;
                if (a[i][j] <= height) {
                    flooded[i][j] = 1;
                    Q.push(i); Q.push(j);
                }
            }
        }
    }
    // 테두리로부터 추가로 침수되는 위치 찾기
    while (!Q.empty()) {
        int x = Q.front(); Q.pop();
        int y = Q.front(); Q.pop();
        for (int k = 0; k < 4; k++) {
            int nx = x + dir[k][0];
            int ny = y + dir[k][1];
            if (nx < 1 || ny < 1 || nx > N || ny > M) continue;
            if (a[nx][ny] > height) continue;
            if (flooded[nx][ny] == 1) continue;
            Q.push(nx);
            Q.push(ny);
            flooded[nx][ny] = 1;
        }
    }
}
int visit[NM][NM];
int CountIsland() {  // 침수되지 않은 땅 덩어리 개수 찾기
    queue<int> Q;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            visit[i][j] = 0;
        }
    }
    int island_cnt = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (flooded[i][j] == 0 && visit[i][j] == 0) {
                // 새로운 땅 덩어리 발견
                island_cnt++;
                Q.push(i); Q.push(j);
                visit[i][j] = 1;
                while (!Q.empty()) {
                    int x = Q.front(); Q.pop();
                    int y = Q.front(); Q.pop();
                    for (int k = 0; k < 4; k++) {
                        int nx = x + dir[k][0];
                        int ny = y + dir[k][1];
                        if (nx < 1 || ny < 1 || nx > N || ny > M) continue;
                        if (visit[nx][ny]) continue;
                        if (flooded[nx][ny]) continue;
                        Q.push(nx); Q.push(ny);
                        visit[nx][ny] = 1;
                    }
                }
            }
        }
    }
    return island_cnt;
}
void Pro() {
    vector<int> H;
    for (int i = 1; i <= N; i++) for (int j = 1; j <= M; j++) H.push_back(a[i][j]);
    sort(H.begin(), H.end());
    for (int h : H) {
        // 1. 침수되는 위치 찾기
        Flooding(h);
        // 2. 땅 덩어리 개수 세기
        int island_cnt = CountIsland();
        // 3. 정답 여부 확인하기
        if (island_cnt >= 2) {
            cout << h;
            return;
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    Input();
    Pro();
    return 0;
}