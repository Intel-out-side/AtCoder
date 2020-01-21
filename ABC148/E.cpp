#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;

ll f(ll n) {
  if (n < 2) {
    return 1;
  }
  else {
    return n * f(n - 2);
  }
}

int main() {
  ll N;
  cin >> N;

  ll ans = f(N);
  ll zeros = 0;
  while (ans % 10 == 0) {
    ans /= 10;
    zeros ++;
  }

  cout << zeros << endl;
  return 0;
}
