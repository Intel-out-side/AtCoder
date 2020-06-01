#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll A, B, C, K;

  cin >> A >> B >> C >> K;

  ll res;
  if (K <= A) {
    res = K;
  }
  else if (A < K && K <= (A+B)) {
    res = A;
  }
  else if ((A+B) < K && K <= (A+B+C)) {
    res = A - (K - A - B);
  }
  else {
    res = A - C;
  }

  cout << res << endl;
  return 0;
}
