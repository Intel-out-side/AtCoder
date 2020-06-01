//floor(a/b) == (a - a%b)/bで整数除算のみを使って表せる
//->極めて競プロ的な変形なのでおぼえておくと良いらしい

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll A, B, N;

  cin >> A >> B >> N;

  ll ans;
  if ((B-1) <= N) {
    ans = floor(A*(B-1)/B) - A * floor((B-1)/B);
  }
  else {
    ans = floor(A * N / B) - A * floor(N/B);
  }

  cout << ans << endl;
  return 0;
}
