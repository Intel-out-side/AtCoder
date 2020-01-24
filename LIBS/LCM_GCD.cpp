/*
DONT FORGET
#include <vector>
#include
*/
typedef long long ll;

template <typename T> T gcd(T a, T b) {
  if (a % b == 0) {
    return b;
  }
  else {
    return (gcd(b, a%b));
  }
}

template <typename T> T lcm(T a, T b) {
  return a * b / gcd(a, b);
}

template <typename T> T LCM(vector<T> x) {
  T ans = lcm(x[0], x[1]);
  for (T i = 0; i < x.size(); i++) {
    ans = lcm(ans, x[i]);
  }
  return ans;
}

ll GCD(vector<ll> x) {
}
