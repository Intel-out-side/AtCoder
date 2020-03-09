#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, P;
  cin >> N >> P;
  string S;
  cin >> S;

  long long ans = 0;
  for (long long i = 1; i <= N; i++) {
    for (long long j = 0; j < N - i + 1; j++) {
      string part = S.substr(j, i);
      cout << part << endl;
      long long num = stoll(part);
      if (num % P == 0) ans++;
    }
  }
  cout << ans << endl;
  return 0;
}
