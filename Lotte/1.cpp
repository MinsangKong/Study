#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define MAX_LEN 1000
using namespace std;
int cnt[1000000];
int n, m;
void input() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        int x; cin >> x;
        cnt[x]++;
    }
}
void pro() {
    for (int i = 1; i <= m; i++) {
        int x; cin >> x;
        int ans = 0;
        for (int digit = 1; digit <= 100000; digit *= 10) {
            // digit_zero := x 에서 digit 자리 수만 0으로 바꾼 수
            int digit_zero = x / (digit * 10) * (digit * 10) + x % (digit);
            for (int num = 0; num <= 9; num++) {
                // new_x := x 에서 digit 자리 수만 num으로 바꾼 수
                int new_x = digit_zero + num * digit;
                if (x == new_x) continue;
                ans += cnt[new_x];
            }
        }
        cout << ans << ' ';
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    input();
    pro();
    return 0;
}