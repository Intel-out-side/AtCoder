#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, K;
  cin >> N >> K;

  long long x = N / K;

  long long ans = min(abs(N - x*K), abs(N - (x+1)*K));

  cout << ans << endl;
  return 0;
}
