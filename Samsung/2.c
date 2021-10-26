#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <vector>
#include <time.h>
#include <queue>
#include <iostream>
using namespace std;
#define FOR(i,n,m) for (int i=(n);i<=(m);i++)
#define si(n) fscanf(in,"%d",&n)
#define NM 1005
#define MOD 1000000009
typedef long long int ll;
int n, K;
int a[105][105], b[105][105];
void Input() {
    cin >> n >> K;
    for (int i = 1; i <= n; i++) {
        cin >> a[1][i];
    }
}
void Roll(int &R, int &C, int &D) {
    for (int c = D + 1; c <= C; c++) {
        b[1][c - D] = a[1][c];
        a[1][c] = 0;
    }
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= D; j++) {
            b[D - j + 2][i] = a[i][j];
            a[i][j] = 0;
        }
    }
    for (int i = 1; i <= D + 1; i++) {
        for (int j = 1; j <= C - D; j++) {
            a[i][j] = b[i][j];
            b[i][j] = 0;
        }
    }
    int _R = R;
    R = D + 1;
    C = C - D;
    D = _R;
}
void DoubleRoll() {
    // 첫번째 절반
    for (int i = 1; i <= n / 2; i++) {
        a[2][n / 2 - i + 1] = a[1][i];
    }
    for (int i = n / 2 + 1; i <= n; i++) {
        a[1][i - n / 2] = a[1][i];
        a[1][i] = 0;
    }
    // 두번째 절반
    for (int i = 1; i <= 2; i++) {
        for (int j = 1; j <= n / 4; j++) {
            a[5 - i][n / 4 - j + 1] = a[i][j];
        }
    }
    for (int i = 1; i <= 2; i++) {
        for (int j = n / 4 + 1; j <= n / 2; j++) {
            a[i][j - n / 4] = a[i][j];
            a[i][j] = 0;
        }
    }
}
int dir[4][2] = { {1,0},{0,1},{-1,0},{0,-1} };
void Press(int R, int C) {
    for (int r = 1; r <= R; r++) {
        for (int c = 1; c <= C; c++) {
            b[r][c] = 0;
        }
    }
    for (int r = 1; r <= R; r++) {
        for (int c = 1; c <= C; c++) {
            for (int k = 0; k < 4; k++) {
                int nr = r + dir[k][0];
                int nc = c + dir[k][1];
                if (a[r][c] <= a[nr][nc]) continue;
                if (a[nr][nc] == 0) continue;
                int diff = (a[r][c] - a[nr][nc]) / 5;
                b[r][c] -= diff;
                b[nr][nc] += diff;
            }
        }
    }
    for (int r = 1; r <= R; r++) {
        for (int c = 1; c <= C; c++) {
            a[r][c] += b[r][c];
            b[r][c] = 0;
        }
    }
}
void Unroll(int R, int C) {
    int idx = 0;
    for (int c = 1; c <= C; c++) {
        for (int r = 1; r <= R; r++) {
            if (a[r][c] == 0) continue;
            b[1][++idx] = a[r][c];
            a[r][c] = 0;
        }
    }
    for (int c = 1; c <= idx; c++) a[1][c] = b[1][c];
}
void Pro() {
    int ans = 0;
    while (true) {
        // 0. 종료 조건 확인
        int minV = a[1][1], maxV = a[1][1];
        for (int j = 1; j <= n; j++) minV = min(minV, a[1][j]), maxV = max(maxV, a[1][j]);
        if (maxV - minV <= K) break;
        ans++;
        // 1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어줍니다.(가장 작은 위치가 여러 개라면 모두 넣기)
        for (int j = 1; j <= n; j++) if (a[1][j] == minV) a[1][j]++;
        // 2. 도우를 말아줍니다.
        int R = 1, C = n, D = 1;
        while (R <= C - D) {
            Roll(R, C, D);
        }
        // 3. 도우를 꾹 눌러줍니다.
        Press(R, C);
        Unroll(R, C);
        // 4. 도우를 두 번 반으로 접어줍니다.
        DoubleRoll();
        // 5. 3의 과정만 한번 더 진행합니다.
        R = 4, C = n / 4;
        Press(R, C);
        Unroll(R, C);
    }
    cout << ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    Input();
    Pro();
    return 0;
}



