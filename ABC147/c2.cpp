#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int g[15][15];

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      g[i][j] = -1; //なにも証言していない::-1
    }
  }
  for (int i = 0; i < n; i++) {
    int m;
    cin >> m;
    for (int j = 0; j < m; j++) {
      int to, judge;
      cin >> to >> judge;
      to--;
      g[i][to] = judge;
    }
  }

  int ans = 0;

  // 1<<0 = 1; 1<<1 = 2; 1<<2 = 4,....
  //すなわち, 1<<n = 2^nになる。全部の状態量は2^nなのでこれで全探索できる。
  //bit全探索？
  for (int i = 0; i < (1<<n); i++) {
    vector<int> d(n); //各ビットが各ノードが正直者かどうかの状態を保持するようになっている
    for (int j = 0; j < n; j++) {
      if ((i>>j)&1) { //iのjビット目が1であるかどうか
        d[j] = 1; //1が立ってれば正直者
      }
    }

    bool ok = true;//もし矛盾が生じなければOK
    for (int j = 0; j < n; j++) {
      if (d[j]) {
        for (int k = 0; k < n; k++) {
          if (g[j][k] == -1) continue; //証言がない場合
          if (g[j][k] != d[k]) ok = false; //もし食い違う証言をしている場合はfalse
        }
      }
    }
    if (ok) ans = max(ans, __builtin_popcount(i));
    //__builtin_popcount(i) : 2進数表記のときに1が何個存在するかをカウントする関数
  }
  cout << ans << endl;
  return 0;
}
