#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll gcd(ll, ll);
ll lcm(ll, ll);

int main() {
  int A, B;
  cin >> A >> B;

  ll ans = lcm(A, B);

  cout << ans << endl;
  return 0;

}

ll gcd(ll a, ll b) {
  if (a % b == 0) {
    return b;
  }
  else {
    return (gcd(b, a%b));
  }
}

ll lcm(ll a, ll b) {
  return a * b / gcd(a, b);
}
