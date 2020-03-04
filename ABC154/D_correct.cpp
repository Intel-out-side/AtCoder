#include <bits/stdc++.h>
#define rep(i, n) for (long long i = 0; i < n; i++)
using namespace std;
using ll = long long;

//累積和を取って考える
//和の期待値＝期待値の和（E[X+Y] = E[x]+E[Y]）を用いて解ける
int main() {
  ll N, K;
  cin >> N >> K;
  ll p[N];
  ll E[N];

  rep(i, N) cin >> p[i];

  ll sum = 0;
  ll max_sum = 0;
  queue<ll> q;

  for (ll i = 0; i < N; i++) {
    E[i] = (p[i] + 1);
  }


  for (ll i = 0; i < N; i++){
    sum += E[i];
    q.push(E[i]);
    if (q.size() > K) {
      sum -= q.front(); q.pop();
    }
    if (q.size() == K) max_sum = max(max_sum, sum);
  }

  double answer = max_sum * 0.5;

  printf("%.10f\n", answer);
  //cout は整数部、小数部合わせて6桁
  //printfはデフォルトで小数点以下6桁
  //cout << fixed << setprecision(6)とすれば10^-6までの精度で出力できる
  return 0;
}
