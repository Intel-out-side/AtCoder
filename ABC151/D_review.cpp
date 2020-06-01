#include <bits/stdc++.h>
using namespace std;
#define INF 10000

vector<int> dx = {1, 0, -1, 0};
vector<int> dy = {0, -1, 0, 1};

int main() {
  int H, W;
  cin >> H >> W;
  vector<string> S(H);
  for (int i = 0; i < H; i++) cin >> S[i];

  int ans = 0;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      vector<vector<int>> dist(H, vector<int>(W, INF));
      if (S[i][j] != '.') continue;
      dist[i][j] = 0;
      queue<pair<int, int>> q;
      q.push(make_pair(i, j));

      while (!q.empty()) {
        pair<int, int> now = q.front(); q.pop();
        for (int k = 0; k < 4; k++) {
          int tgt_y = now.first + dy[k], tgt_x = now.second + dx[k];
          if (tgt_x < 0 || tgt_x >= W || tgt_y < 0 || tgt_y >= H) continue;
          if (dist[tgt_y][tgt_x] != INF) continue;
          if (S[tgt_y][tgt_x] == '#') continue;
          dist[tgt_y][tgt_x] = dist[now.first][now.second]+1;
          q.push(make_pair(tgt_y, tgt_x));
        }
      }

      for (int x = 0; x < H; x++) {
        for (int y = 0; y < W; y++) {
          if (dist[x][y] == INF) continue;
          ans = max(ans, dist[x][y]);
        }
      }
    }
  }
  cout << ans << endl;
  return 0;
}
