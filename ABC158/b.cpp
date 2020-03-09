#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, A, B;
  cin >> N >> A >> B;

  if ((A + B) == 0) {
    cout << 0 << endl;
    return 0;
  }

  long long n, r;
  n = N / (A+B);
  r = N % (A+B);

  long long ans;
  if (r < A) {
    ans = n * A + r;
  }
  else {
    ans = n * A + A;
  }

  cout << ans << endl;
  return 0;
}
