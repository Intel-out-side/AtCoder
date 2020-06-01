#include <bits/stdc++.h>
using namespace std;
using ll = long long;

template <typename T> T gcd(T x, T y) {
  return y ? gcd(y, x%y) : x;
}

int main() {
  int K;
  cin >> K;

  ll sum = 0;
  for (int i = 1; i <= K; i++) {
    for (int j = 1; j <= K; j++) {
      for (int k = 1; k <= K; k++) {
        sum += gcd(gcd(i, j), k);
      }
    }
  }

  cout << sum << endl;
  return 0;
}
