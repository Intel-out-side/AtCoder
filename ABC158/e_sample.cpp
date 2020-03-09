#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, p;
  cin >> n >> p;
  string s;
  cin >> s;

  //pが２または５のとき、s*10^n % p はかならずゼロになる
  if (10 % p == 0) { //ｐが２または５のとき
    long long ans = 0;
    for (int r = 0; r < n; r++) {
      if ((s[r] - '0')%p == 0) { ans += r + 1; } //右端がpの倍数になっていれば左側はなんでもよい。
    }
    cout << ans << endl;
    return 0;
  }


  vector<int> d(n+1, 0); //累積和を格納するベクトル
  int ten = 1;
  for (int i = n - 1; i >= 0; i--) {
    int a = (s[i] - '0') * ten % p; //各桁のmod p
    d[i] = (d[i+1] + 1) % p;
    ten *= 10; ten %= p;
  }

  vector<int> cnt(p);
  long long ans = 0;
  for (int i = n; i >= 0; i--) {
    ans += cnt[d[i]];
    cnt[d[i]]++;
  }
  cout << ans << endl;
  return 0;
}
