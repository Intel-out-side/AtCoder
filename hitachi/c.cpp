#include <bits/stdc++.h>
using namespace std;
using ll = long long;

class DFS {
public:
  //　グラフの隣接リスト表現
  using Graph = vector<vector<ll>>;
  //　ith node is visited -> true, not visted -> false
  vector<bool> seen;
  // ith node belongs to jth group
  vector<ll> ids;
  // ith group's size
  vector<ll> size_of_id;
  // edges from ith node
  vector<ll> deg;
  // ノードの数
  ll num_of_nodes;
  // 隣接リスト表現のリスト
  Graph G;

  DFS(ll n) {
    num_of_nodes = n;
    G = vector<vector<ll>>(num_of_nodes);
    seen = vector<bool>(num_of_nodes, false);
    ids = vector<ll>(num_of_nodes, -1);
    size_of_id = vector<ll>(num_of_nodes, 0);
    deg = vector<ll>(num_of_nodes, 0);
    color = vector<ll>(num_of_nodes, WHITE);
  }

  Graph get_graph() { return G; }

  bool is_seen(ll ith_node) { return seen[ith_node]; }

  ll get_id_of(ll ith_node) { return ids[ith_node]; }

  ll get_deg_of(ll ith_node) { return deg[ith_node]; }

  ll get_size_of_id(ll id) { return size_of_id[id]; }

  void graph_init(ll m) {
    for (ll i = 0; i < m; i++) {
      ll a, b;
      cin >> a >> b;
      a--; b--; //入力が1オリジンの場合

      /*無向グラフの場合、例えば(5,8),(8,5)は重複するクエリなので片方を弾く*/
      //vector<ll>::iterator itr1, itr2;
      auto itr1 = find(G[a].begin(), G[a].end(), b);
      auto itr2 = find(G[b].begin(), G[b].end(), a);
      if (itr1 == G[a].end() && itr2 == G[b].end()) {
        G[a].push_back(b); G[b].push_back(a); //重複を許さない
        deg[a]++; deg[b]++;
      }

      /*有効グラフなら下記を使う*/
      //G[a].push_back(b); deg[a]++;
      //G[b].push_back(a); deg[b]++; // 無向グラフなら双方に足す
    }
  }

  void dfs(ll v, ll id) {
    seen[v] = true;
    ids[v] = id;
    size_of_id[id]++;
    // 次に訪問できる
    for (ll next_v : G[v]) {
      if (seen[next_v]) continue;
      dfs(next_v, id);
    }
  }

  /*
  @param v : starting node
  @param id : grouping each node by id.
  */
  void stack_dfs(ll v, ll id) {
    stack<ll> s;
    s.push(v);
    while (!s.empty()) {
      ll now = s.top();
      ll next_node = next_visit(now);
      bool isCompleted = true;

      if (next_node >= 0) {
        isCompleted = !isCompleted;
        s.push(next_node);
        color[next_node] = GRAY;
      }

      if (isCompleted) {
        color[now] = BLACK;
        if (ids[now] == -1) {
          ids[now] = id;
          size_of_id[id]++;
        }
        seen[now] = true;
        s.pop();
      }
    }
  }

private:
  const ll WHITE = 0;
  const ll GRAY = 1;
  const ll BLACK = 2;

  vector<ll> color;

  ll next_visit(ll now) {
    for (ll adjacent_node : G[now]) {
      if (color[adjacent_node] == WHITE) return adjacent_node;
    }
    return -1;
  }
};

int main() {
  ll N;
  cin >> N;
  DFS d = DFS(N);
  d.graph_init();

  for (ll i = 0; i < N; i++) {
    
  }
  return 0;
}
