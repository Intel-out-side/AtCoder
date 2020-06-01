#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll H, W;
  cin >> H >> W;

  ll res;
  if (H == 1 || W == 1) res = 1;
  else {
    if (H * W % 2 == 0) res = H * W / 2;
    else res = (H * W / 2) + 1;
  }

  cout << res << endl;
  return 0;
}
