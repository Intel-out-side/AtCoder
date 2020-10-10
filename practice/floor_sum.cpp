#include <atcoder/math>
#include <bits/stdc++.h>

using namespace std;
using namespace atcoder;

int main() {
  long long T;
  cin >> T;
  long long ans = 0;

  for (long long i = 0; i < T; i++) {
    long long n, m, a, b;
    cin >> n >> m >> a >> b;
    ans = floor_sum(n, m, a, b);
    cout << ans << endl;
  }

  cout << ans << endl;
}
