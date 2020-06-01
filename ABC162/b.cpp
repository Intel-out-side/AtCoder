#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;
  ll sum = 0;
  for (ll i = 1; i <= N; i++) {
    if ((i % 3 == 0) || (i % 5 == 0)) {
      continue;
    }
    else {
      sum += i;
    }
  }
  cout << sum << endl;
  return 0;
}
