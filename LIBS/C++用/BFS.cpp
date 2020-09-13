#include <bits/stdc++.h>
using namespace std;
using ll = long long;

class BFS {
public:
  //グラフの隣接リスト表現
  using Graph = vector<vector<ll>>;
  //INF
  const ll INF = 100100100;
  //ノードの数
  ll num_of_nodes;
  //隣接表現のリスト
  Graph G;
  //各リストの出次数
  vector<ll> deg;
  //始点からの距離を格納するvector
  vector<ll> dist;


  BFS(ll n) {
    num_of_nodes = n;
    G = vector<vector<ll>>(n);
    deg = vector<ll>(n, 0);
    dist = vector<ll>(n, INF);
  }

  //distを格納するvectorのgetter
  vector<ll> get_dist() {
    return dist;
  }

  void graph_init(ll m) {
    for (ll i = 0; i < m; i++) {
      ll a, b;
      cin >> a >> b;
      a--; b--; //入力が１オリジンの場合

      /*無向グラフの場合、例えば(5,8),(8,5)は重複するクエリなので片方を弾く*/
      //vector<ll>::iterator itr1, itr2;
      auto itr1 = find(G[a].begin(), G[a].end(), b);
      auto itr2 = find(G[b].begin(), G[b].end(), a);
      if (itr1 == G[a].end() && itr2 == G[b].end()) {
        G[a].push_back(b); G[b].push_back(a); //重複を許さない
        deg[a]++; deg[b]++;
      }
    }
  }

  //有向グラフの初期化
  void DAG_init(ll m) {
    for (ll i = 0; i < m; i++) {
      ll a, b;
      cin >> a >> b;


      G[a].push_back(b);
      deg[a]++;
      /*
      //O(N)かかるので外したほうが良いかも
      auto itr = find(G[a].begin(), G[a].end(), b);
      if (itr == G[a].end()) {
        G[a].push_back(b);
        deg[a]++;
      }
      */
    }
  }

  void bfs(ll start) {
    queue<ll> q;
    dist[start] = 0;
    q.push(start);

    while(!q.empty()) {
      ll now = q.front(); q.pop();
      for (ll i = 0; i < G[now].size(); i++) {
        ll v = G[now][i]; //今の頂点に隣接する頂点ｖ
        if (dist[v] != INF) continue;

        dist[v] = dist[now]+1;
        q.push(v);
      }
    }
  }
};

// 以下はABC151のD問題の例
// 入力が
/*
  ..#..
  .....
  .###.
  みたいな感じで与えられる
*/
int main() {
  int H, W;
  cin >> H >> W;

  vector<string> G(H);
  for (int i = 0; i < H; i++) {
    cin >> G[i];
  }

  BFS b = BFS(H * W);

  vector<int> dh = {0, -1, 0, 1};
  vector<int> dw = {1, 0, -1, 0};


  for (int h = 0; h < H; h++) {
    for (int w = 0; w < W; w++) {
      if (G[h][w] == '#') continue;

      for (int i = 0; i < 4; i++) {
        int w_ = w + dw[i], h_ = h + dh[i];
        if (w_ < 0 || h_ < 0 || h_ >= H || w_ >= W) continue;

        if (G[h_][w_] == '.') b.G[W * h + w].push_back(W * h_ + w_);
      }
    }
  }

  vector<vector<ll>> setup_graph = b.get_graph();
  vector<ll> init_dist = b.get_dist();

  int max = -100;
  for (int i = 0; i < H*W; i++) {
    b.bfs(i);
    vector<ll> dists = b.get_dist();

    for (int j = 0; j < dists.size(); j++) {
      if (dists[j] == INF) continue;
      max = max < dists[j] ? dists[j] : max;
    }
    b.G = setup_graph;
    b.dist = init_dist;
  }

  cout << max << endl;
  return 0;

}
