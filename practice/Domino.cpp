#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define MAX_M 20
#define MAX_N 20

int dp[2][1 << MAX_M];

void solve() {
  int *crt = dp[0];
  int *next = dp[1];

  crt[0] = 1;

  for (int i = n-1, i >= 0; i--) {
    for (int j = m-1; j >= 0; j--) {

      for (int used = 0; used < (1<<m); used++) {

        if ((used >> j & 1) || color[i][j]) {
          //すでに使われているならそこにブロックを置く必要はない
          next[used] = crt[used & ~(i<<j)];
        } else {
          //2通りの向きを試す
          int res = 0;

          //横向き
          if (j + 1 < M && !(used >> (j+1) & 1) && !color[i][j+1]) res += crt[used | 1 << (j+1)]

          //縦向き
          if (i + 1 < N && !color[i+1][j]) res += crt[used | 1 << j];
        }

      }
    }
  }
}

int main() {
}
