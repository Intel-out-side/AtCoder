#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll count = 0;

bool isLun(ll num) {
  string n = to_string(num);
  bool res = true;
  for (ll i = 0; i < n.length()-1; i++) {
    if (abs(n[i] - n[i+1]) > 1) res = false;
  }
  return res;
}

int main() {
  ll K;
  cin >> K;

  ll i = 1;
  ll count = 0;
  while (true) {
    if (count == K) break;

    if
    count++;
    i++;
  }
  return 0;
}
