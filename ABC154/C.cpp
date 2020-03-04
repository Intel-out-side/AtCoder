#include <bits/stdc++.h>
#define rep(i, n) for (long long i = 0; i < n; i++)
using namespace std;

int main() {
  long long N;;

  cin >> N;
  vector<long long> A(N);
  rep(i, N) cin >> A[i];

  sort(A.begin(), A.end());

  bool isDifferent = true;

  rep(i, N - 1) {
    if (A[i] == A[i+1]) isDifferent = false;
  }

  if (isDifferent) cout << "YES" << endl;
  else cout << "NO" << endl;

  return 0;
}
