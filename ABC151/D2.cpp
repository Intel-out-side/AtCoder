#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; i++)
#define INF 100100
using namespace std;
using ll = long long;
using P = pair<int, int>;

vector<int> di = {-1, 0, 1, 0};
vector<int> dj = {0, 1, 0, -1};

//BFS: 幅優先探索
int main() {
  int H, W;
  cin >> H >> W;
  int ans = 0;
  vector<string> S(H);
  for (int i = 0; i < H; i++) cin >> S[i];

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
    if (S[i][j] == '#') continue;
    vector<vector<int>> dist(H, vector<int>(W, INF));
    queue<P> q;

    //無名関数
    //[&]で関数外のスコープも参照できる
    auto update = [&](int ii, int jj, int x) {
      if (dist[ii][jj] != INF) return; //すでに訪問されてたらskip

      dist[ii][jj] = x;
      q.push(P(ii, jj));
    };

    update(i, j, 0);
    while(!q.empty()) {
      int si = q.front().first;
      int sj = q.front().second;
      q.pop(); //popしないと無限ループになる

      for(int dif = 0; i < 4; i++) {
        int tgt_x = si + di[dif];
        int tgt_y = sj + dj[dif];

        if (tgt_x < 0 || tgt_x >= W || tgt_y < 0 || tgt_y >= H) continue;
        if (S[tgt_x][tgt_y] == '#') continue;
        update(tgt_x, tgt_y, dist[si][sj] + 1);
      }
    }

    rep(ni, H)rep(nj, W) {
      if (dist[ni][nj] == INF) continue;
      if (dist[ni][nj] > ans) ans = dist[ni][nj];
    }
  }
}
  cout << ans << endl;
  return 0;
}
