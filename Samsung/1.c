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
struct Cell {
    vector<int> eggs, monsters, next_monsters;
    int cadaver[3];  // cadaver[x]: 지속 시간이 x인 시체의 개수
} a[5][5];
int ans = 0;
int n = 4, T;
inline bool InRange(int x, int y) {
    return 1 <= x && x <= n && 1 <= y && y <= n;
}
struct Packman {
    int dirs[4][2] = { {-1,0},{0,-1},{1,0},{0,1} };
    int x, y;  // x행 y열에 존재
    int _Move(int bit) {
        if (bit == 15) {
            bit = bit;
        }
        int moves[] = { bit / 16, (bit / 4) % 4, bit % 4 };
        int visit[5][5] = { 0, };
        int cx = x, cy = y;
        int res = 0;
        for (int i = 0; i < 3; i++) {
            cx += dirs[moves[i]][0];
            cy += dirs[moves[i]][1];
            if (!InRange(cx, cy)) return -1;
            if (visit[cx][cy] == 0) res += a[cx][cy].monsters.size();
            visit[cx][cy] = 1;
        }
        return res;
    }
    void Move() {  // 조건에 맞는 이동을 수행하고, 먹은 몬스터 수 return
        int maxV = -1, maxBit = 0;
        for (int bit = 0; bit < 64; bit++) {
            int v = _Move(bit);  // bit 방법으로 이동하면 먹는 몬스터 수 계산
            if (maxV < v) {  // 최댓값일 때를 저장
                maxV = v;
                maxBit = bit;
            }
        }
        int moves[] = { maxBit / 16, (maxBit / 4) % 4, maxBit % 4 };
        for (int i = 0; i < 3; i++) {
            x += dirs[moves[i]][0];
            y += dirs[moves[i]][1];
            a[x][y].cadaver[2] += a[x][y].monsters.size();
            a[x][y].monsters.clear();
        }
    }
} packman;
void Input() {
    int m;
    cin >> m >> T;
    cin >> packman.x >> packman.y;
    for (int i = 1; i <= m; i++) {
        int x, y, d;
        cin >> x >> y >> d;
        a[x][y].monsters.push_back(d - 1);
    }
}
void ReadyReplication() {
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            a[i][j].eggs = a[i][j].monsters;
        }
    }
}
void ConfirmReplication() {
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            a[i][j].monsters.insert(a[i][j].monsters.end(), a[i][j].eggs.begin(), a[i][j].eggs.end());
            a[i][j].eggs.clear();
        }
    }
}
inline bool Possible(int i, int j) {
    if (!InRange(i, j)) return false;
    if (i == packman.x && j == packman.y) return false;
    for (int k = 0; k < 3; k++) if (a[i][j].cadaver[k] != 0) return false;
    return true;
}
int dirs[8][2] = { {-1,0},{-1, -1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1} };
void MoveMonster() {
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            for (int d : a[i][j].monsters) {
                int flag = 0;
                // i 행 j 열에, d 방향의 몬스터가 존재한다.
                for (int k = 0; k < 8; k++) {
                    int ni = i + dirs[d][0];
                    int nj = j + dirs[d][1];
                    if (Possible(ni, nj)) {
                        a[ni][nj].next_monsters.push_back(d);
                        flag = 1;
                        break;
                    }
                    d = (d + 1) % 8;
                }
                if (flag == 0) a[i][j].next_monsters.push_back(d);
            }
        }
    }
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            a[i][j].monsters = a[i][j].next_monsters;
            a[i][j].next_monsters.clear();
        }
    }
}
void VanishCadaver() {
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 2; k++) {
                a[i][j].cadaver[k] = a[i][j].cadaver[k + 1];
            }
            a[i][j].cadaver[2] = 0;
        }
    }
}
void Pro() {
    while (T--) {
        // 몬스터 복제 시도
        ReadyReplication();
        // 몬스터 이동
        MoveMonster();
        // 팩맨 이동
        packman.Move();
        // 몬스터 시체 소멸
        VanishCadaver();
        // 몬스터 복제 완성
        ConfirmReplication();
    }
    int ans = 0;
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            ans += a[i][j].monsters.size();
        }
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
