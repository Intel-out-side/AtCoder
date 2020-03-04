#include <bits/stdc++.h>
using namespace std;
class DFS {
public:
  //　グラフの隣接リスト表現
  using Graph = vector<vector<int>>;
  //　ith node is visited -> true, not visted -> false
  vector<bool> seen;
  // ith node belongs to jth group
  vector<int> ids;
  // ith group's size
  vector<int> size_of_id;
  // edges from ith node
  vector<int> deg;
  // ノードの数
  int num_of_nodes;
  // 隣接リスト表現のリスト
  Graph G;

  DFS(int n) {
    num_of_nodes = n;
    G = vector<vector<int>>(num_of_nodes);
    seen = vector<bool>(num_of_nodes, false);
    ids = vector<int>(num_of_nodes, -1);
    size_of_id = vector<int>(num_of_nodes, 0);
    deg = vector<int>(num_of_nodes, 0);
    color = vector<int>(num_of_nodes, WHITE);
  }

  Graph get_graph() { return G; }

  bool is_seen(int ith_node) { return seen[ith_node]; }

  int get_id_of(int ith_node) { return ids[ith_node]; }

  int get_deg_of(int ith_node) { return deg[ith_node]; }

  int get_size_of_id(int id) { return size_of_id[id]; }

  void graph_init(int m) {
    for (int i = 0; i < m; i++) {
      int a, b;
      cin >> a >> b;
      a--; b--; //入力が1オリジンの場合

      /*無向グラフの場合、(5,8),(8,5)は重複するクエリなので片方を弾く*/
      //vector<int>::iterator itr1, itr2;
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

  void dfs(int v, int id) {
    seen[v] = true;
    ids[v] = id;
    size_of_id[id]++;
    // 次に訪問できる
    for (int next_v : G[v]) {
      if (seen[next_v]) continue;
      dfs(next_v, id);
    }
  }

  /*
  @param v : starting node
  @param id : grouping each node by id.
  */
  void stack_dfs(int v, int id) {
    stack<int> s;
    s.push(v);
    while (!s.empty()) {
      int now = s.top();
      int next_node = next_visit(now);
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
  const int WHITE = 0;
  const int GRAY = 1;
  const int BLACK = 2;

  vector<int> color;

  int next_visit(int now) {
    for (int adjacent_node : G[now]) {
      if (color[adjacent_node] == WHITE) return adjacent_node;
    }
    return -1;
  }
};

#define MAX 10001
vector<int> block_to[MAX];

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  int id = -1;

  DFS tansaku = DFS(n);
  tansaku.graph_init(m);

  for (int i = 0; i < k; i++) {
    int c, d;
    cin >> c >> d;
    c--; d--;
    block_to[c].push_back(d); block_to[d].push_back(c);
  }

  for (int i = 0; i < n; i++) {
    if (tansaku.is_seen(i) == true) continue;
    id++;
    tansaku.stack_dfs(i, id);
  }

  for (int i = 0; i < n; i++) {
    int result = tansaku.get_size_of_id(tansaku.get_id_of(i)) - 1 - tansaku.get_deg_of(i);
    for (int blocker : block_to[i]) {
      if (tansaku.get_id_of(blocker) == tansaku.get_id_of(i)) result--;
    }
    if (i > 0) cout << " ";
    cout << result;
  }
  cout << endl;
  return 0;
}
