#include <bits/stdc++.h>
using namespace std;

//全点間の距離を求めたあとに、燃料補給なしで渡れる点を結んだ新しいマップを作る。
//全点間の距離をもとめる -> ダイクストラまたはワーシャルフロイド　

//始点固定でstart -> goal の最短距離 :: ダイクストラが便利
//全点間の最短距離 start -> goalの最短距離 :: WFが便利(O(N^3)が間に合うなら)

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
      a--; b--; //入力が1オリジンのとき

      g[a][b] = g[b][a] = c;
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


int main() {
  int N, M, L;
  cin >> N >> M >> L;
  WF wf = WF(N);
  wf.graph_init(M);
  wf.get_shortest(); //全点間の最小距離が求められた

  vector<vector<ll>> new_graph(N, vector<ll>(N, MAX));
  for (ll i = 0; i < N; i++) new_graph[i][i] = 0;

  for (ll i = 0; i < N; i++) {
    for (ll j = i+1; j < N; j++) {
      if (wf.g[i][j] <= L) {
        new_graph[i][j] = new_graph[j][i] = 1;
      }
    }
  }

  WF wf2 = WF(N);
  wf2.g = new_graph;

  wf2.get_shortest();


  vector<vector<ll>> ans_graph = wf2.get_graph();

  ll Q;
  cin >> Q;
  for (ll i = 0; i < Q; i++) {
    ll s, t;
    cin >> s >> t;
    s--; t--;
    if (ans_graph[s][t] == MAX) cout << -1 << endl;
    else cout << ans_graph[s][t] - 1 << endl;
  }
  return 0;

}
