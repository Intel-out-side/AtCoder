#include <bits/stdc++.h>
using namespace std;
using ll = long long;

class TopologicalSort {
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
  //やるべき仕事の順番に入っているvector
  vector<ll> task;
  //ノードiに入ってくる有向辺の数
  vector<ll> indeg;
  //タスクが終わったかどうか
  vector<bool> isCompleted;


  TopologicalSort(ll n) {
    num_of_nodes = n;
    G = vector<vector<ll>>(n);
    deg = vector<ll>(n, 0);
    dist = vector<ll>(n, INF);
    indeg = vector<ll>(n, 0);
    isCompleted = vector<bool>(n, false);
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
      indeg[b]++;
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
    isCompleted[start] = true;

    while(!q.empty()) {
      ll now = q.front(); q.pop();
      task.push_back(now);
      for (ll i = 0; i < G[now].size(); i++) {
        ll v = G[now][i]; //今の頂点に隣接する頂点ｖ
        indeg[v]--;
        if (indeg[v] == 0 && !isCompleted[v]) {
          isCompleted[v] = true;
          q.push(v);
        }
      }
    }
  }

  void tsort() {
    for (ll i = 0; i < num_of_nodes; i++) indeg[i] = 0;

    for (ll i = 0; i < num_of_nodes; i++) {
      for (ll j = 0; j < G[i].size(); j++) {
        int v = G[i][j];
        indeg[v]++;
      }
    }

    for (ll u = 0; u < num_of_nodes; u++) {
      if (indeg[u] == 0 && !isCompleted[u]) bfs(u);
    }
  }
};

int main() {
  ll V, E;
  cin >> V >> E;

  TopologicalSort ts = TopologicalSort(V);

  ts.DAG_init(E);
  ts.tsort();

  for (auto item : ts.task) {
    cout << item << endl;
  }

  return 0;
}
