#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> L(N);
  for (int i = 0; i < N; i++) cin >> L[i];

  sort(L.begin(), L.end());

  int ans = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < i; j++) {
      int right = lower_bound(L.begin(), L.end(), L[i]+L[j]) - L.begin();
      //L[i]+L[j]以上の最初の要素になる
      int left = i + 1;
      //range = [l, r)
      ans += right - left;
    }
  }
  cout << ans << endl;
  return 0;
}
