#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
  int h, w, k;
  cin >> h >> w >> k;

  int ans = 0;
  vector<string> s(h);

  for (int i = 0; i < h; i++) cin >> s[i];

  for (int is = 0; is < (1<<h); is++) { //横の列を消す場合
    for (int js = 0; js < (1<<w); js++) { // 縦の列を消す場合
      int cnt = 0;
      for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) { //すべてのマスを見る
          if (is >> i & 1) continue; // その列のi番目のビットが1なら(i.e.その列のi番目が消されているなら)
          if (js >> j & 1) continue;
          if (s[i][j] == '#') cnt++;
        }
      }
      if (cnt == k) ans++;
    }
  }

  cout << ans << endl;
  return 0;
}
