#include <bits/stdc++.h>
#define rep(i, n) for (long long i = 0; i < n; i++)
using namespace std;



int main() {
  int N, K;
  cin >> N >> K;
  int p[N];

  rep(i, N) scanf("%d", &p[i]);

  double sum = 0.0;

  for (int i = 0; i < N - K + 1; i++) {
    double tmp = 0.0;

    for (int j = i; j < i + K; j++) {
      tmp += 0.5 * (p[j] + 1);
    }

    sum = max(sum, tmp);
    tmp = 0.0;
  }

  cout << sum << endl;
  return 0;
}
//この計算を行うとO(NK)になってKがNに近づくとO(N^2)になって間に合わない
