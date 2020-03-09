#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, P;
  cin >> N >> P;
  string S;
  cin >> S;

  long long max = stoll(S);

  vector<long> f((N*(N+1)/2), 0);
  f[0] = f[1] = -1;

  for (long long i = 2; i <= (N*(N+1)/2); i++) {
    if (f[i]) continue;
    if (i == P) {
      f[i] = i;
      for (long long j = i*i; j <= (N*(N+1)/2); j+=i) {
        if (!f[j]) f[j] = i;
      }
    }
  }
  long long ans = f.size() - (max/P);
  cout << ans << endl;
  return 0;
}
