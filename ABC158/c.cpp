#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int ans = 0;
  for (ans = 1; ans <= 1000; ans++) {
    int a, b;
    a = floor(ans * 0.08);
    b = floor(ans * 0.10);

    if ((a == A) && (b == B)) {
      cout << ans << endl;
      return 0;
    }
  }

  cout << -1 << endl;
  return 0;
}
