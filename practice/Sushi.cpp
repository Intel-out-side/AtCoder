#include <bits/stdc++.h>
#include <cstring>
#include <iomanip>
using namespace std;
using ll = long long;

int N;

double dp[310][310][310];

double f(int c1, int c2, int c3) {

  if (dp[c1][c2][c3] >= 0) return dp[c1][c2][c3];

  if (c1 == 0 && c2 == 0 && c3 == 0) return 0.0;

  double res = 0.0;
  if (c3 > 0) res += f(c1, c2 + 1, c3 - 1) * c3;

  if (c2 > 0) res += f(c1+1, c2-1, c3) * c2;

  if (c1 > 0) res += f(c1-1, c2, c3) * c1;

  res += N;

  res *= 1.0/(c1 + c2 + c3);

  return dp[c1][c2][c3] = res;
}


int main() {
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; i++) cin >> a[i];

  for (int i = 0; i < 310; i++) {
    for (int j = 0; j < 310; j++) {
      for (int k = 0; k < 310; k++) {
        dp[i][j][k] = -1.0;
      }
    }
  }

  int v1 = 0;
  int v2 = 0;
  int v3 = 0;

  for (int item : a) {
    if (item == 1) v1++;
    else if (item == 2) v2++;
    else v3++;
  }

  double ans = f(v1, v2, v3);
  cout << fixed << setprecision(10) << ans << endl;
  return 0;
}
