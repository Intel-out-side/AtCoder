#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  int s = 0;
  for (int i = 1; i <= N; i++) {
    if (i % 2 == 1) s++;
  }

  double ans = (double)s/N;
  cout << fixed << setprecision(7);
  cout << ans << endl;
  return 0;
}
