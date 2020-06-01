#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int dblcmp(double x, double y, double eps) {
  return (x > y + eps ? 1 : y > x + eps ? -1 : 0);
}

int main() {
  ll a, b, c;
  cin >> a >> b >> c;

  double a_ = sqrt(a), b_ = sqrt(b), c_ = sqrt(c);

  //int res = dblcmp(a_+b_-c_, 0, DBL_EPSILON);
  bool res = a_+(b_-c_) < 0;

  if (res) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
