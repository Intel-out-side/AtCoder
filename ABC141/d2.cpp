#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, M;
  cin >> N >> M;

  priority_queue<double> pq;

  for (ll i = 0; i < N; i++) {
    double tmp;
    cin >> tmp;
    pq.push(tmp);
  }

  //top が最大値
  for (ll i = 0; i < M; i++) {
    double top = pq.top(); pq.pop();
    pq.push(top/2);
  }

  ll ans = 0;
  for (ll i = 0; i < N; i++) {
    ans += (ll) pq.top();
    pq.pop();
  }
  cout << ans << endl;
  return 0;
}
