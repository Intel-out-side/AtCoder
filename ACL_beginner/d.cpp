#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
//using ll = long long;

int op(int a, int b) {
  return max(a, b);
}

int e() {
  return 0;
}

int main() {
  int N, K, x, i;
  int ans = 0;

  cin >> N >> K;
  atcoder::segtree<int, op, e> seg(300010);

  for (int i = 0; i < N; i++) {
    cin >> x;

    int L = max(x-K, 0);
    int R = min(x+K, 300000);
    int tmp = seg.prod(L, R+1) + 1;
    ans = max(ans, tmp);
    seg.set(x, tmp);
  }

  //ans = seg.prod(0, 300000);
  cout << ans << endl;
  return 0;
}
