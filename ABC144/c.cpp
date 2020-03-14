#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main() {
  ll N;
  cin >> N;

  double mid = sqrt(N);
  ll a = 1;
  if (N % 2 == 0) {
    for (ll i = 1; i <= mid; i++) {
      if (N % i == 0) a = i;
    }
  }
  else {
    for (ll i = 1; i <= mid; i++) {
      if (N % i == 0) a = i;
    }
  }
  ll b = N / a;

  ll res = a + b - 2;
  cout << res << endl;
  return 0;
}
