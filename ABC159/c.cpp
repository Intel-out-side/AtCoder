#include <bits/stdc++.h>
using namespace std;

int main() {
  int L;
  cin >> L;

  double l = (double)L / 3;

  double ans = l * l * l;

  cout << fixed << setprecision(7) << ans << endl;
  return 0;
}
