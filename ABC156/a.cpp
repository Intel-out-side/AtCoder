#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, r;
  cin >> n >> r;
  int internal;
  if (n >= 10) {
    internal = r;
  }
  else {
    internal = r + 100 * (10-n);
  }

  cout << internal << endl;
  return 0;
}
