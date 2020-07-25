#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
  int N;
  cin >> N;
  vector<ll> A(N);
  for (int i = 0; i < N; i++) cin >> A[i];

  sort(A.begin(), A.end());

  deque<ll> dq;

  dq.push_back(A[0]);
  return 0;
}
