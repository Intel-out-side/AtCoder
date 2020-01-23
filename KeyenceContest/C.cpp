#include <bits/stdc++.h>
#define rep(i, N) for(int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int main() {
  int N, K;
  ll S;
  cin >> N >> K >> S;
  ll MAX = 1e9; // 1 * 10^9
  vector<ll> answer(N, 0);

  if (S != MAX) {
    for (int i = 0; i < K; i++) {
      answer[i] = S;
    }
    for (int i = K; i < N; i++) {
      answer[i] = MAX;
    }
  }
  else {
    for (int i = 0; i < K; i++) {
      answer[i] = S;
    }
    for (int i = K; i < N; i++) {
      answer[i] = 1;
    }
  }
  for (int i = 0; i < N - 1; i++) {
    cout << answer[i] << " ";
  }
  cout << answer.back() << endl;
  return 0;
}
