#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, M;
  cin >> N >> M;

  vector<int> A(M);
  for (int i = 0; i < M; i++) cin >> A[i];

  ll sum = 0;

  for (int i = 0; i < M; i++) sum += A[i];

  if (N - sum >= 0) cout << N - sum << endl;
  else cout << -1 << endl;

  return 0;
}
