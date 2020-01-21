#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll g1(ll n, int p) {
  if (n == 0) return 0;
  return n/p + g1(n/p, p);
}

ll g2(ll n, int p) {
  if (n % 2 == 1) {
    return g1(n, p) - g2(n-1, p);
  }

  ll res = g1(n/2, p);
  if (p == 2) res += n/2;
  return res;
}

int main() {
  ll n;
  cin >> n;
  ll ans = min(g2(n, 2), g2(n, 5));
  cout << ans << endl;
  return 0;
}
