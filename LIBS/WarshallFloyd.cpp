#include <bits/stdc++.h>
using namespace std;



#define MAX 1000100100LL
using ll = long long;
using Graph = vector<vector<ll>>;
class WF {
public:
  Graph g;
  ll num_of_nodes;

  WF(ll n) {
    num_of_nodes = n;
    g = vector<vector<ll>>(n, vector<ll>(n, MAX));
    for (ll i = 0; i < n; i++) { g[i][i] = 0; }
  }

  Graph get_graph() {
    return g;
  }

  void graph_init(ll e) {
    //e: number of edges
    for (ll i = 0; i < e; i++) {
      ll a, b, c;
      cin >> a >> b >> c;
      //a--; b--; //入力が1オリジンのとき

      g[a][b] = c;
    }

  }

  //ワーシャルフロイド法で各頂点i->jの最短距離をモトメル
  void get_shortest() {
    for (ll k = 0; k < num_of_nodes; k++) {
      for (ll i = 0; i < num_of_nodes; i++) {
        if (g[i][k] == MAX) continue;
        for (ll j = 0; j < num_of_nodes; j++) {
          if (g[k][j] == MAX) continue;
          g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
        }
      }
    }
  }
};

//--------------------------

int main() {
  ll n, e;
  cin >> n >> e;
  WF warshall_floyd = WF(n);
  warshall_floyd.graph_init(e);
  warshall_floyd.get_shortest();

  Graph g = warshall_floyd.get_graph();

  bool negative = false;
  for (ll i = 0; i < n; i++) g[i][i] < 0 ? negative = true : negative = negative;

  if (negative) { cout << "NEGATIVE CYCLE" << endl; }
  else {
    for (ll i = 0; i < n; i++) {
      for (ll j = 0; j < n; j++) {
        if (j > 0) cout << " ";
        if (g[i][j] == MAX) cout << "INF";
        else cout << g[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
