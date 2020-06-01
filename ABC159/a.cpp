#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  int res = M * (M-1) / 2 + N * (N-1) / 2;
  cout << res << endl;
  return 0;
}
