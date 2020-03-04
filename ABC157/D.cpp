#include <bits/stdc++.h>
#define MAX 100001
using namespace std;

class UnionFind {
public:
  vector<int> rank, p, num_of_nodes;
  //rank : 各ノードxを根としたときの木の高さをrank[x]とする
  //p : 各ノードxの親をp[x]とする

  UnionFind() {} // Default constructor

  UnionFind(int size = 0) {
    rank.resize(size, 0);
    p.resize(size, 0);
    num_of_nodes.resize(size, 1);
    for (int i = 0; i < size; i++) makeSet(i);
  }

  void makeSet(int x) {
    p[x] = x;
    rank[x] = 0;
  }

  bool same(int x, int y) {
    return root(x) == root(y);
  }

  void unite(int x, int y) {
    if (root(x) == root(y)) return; //すでに同じ根に属している場合は何もしない
    link(root(x), root(y));
  }

  void link(int x, int y) {
    //低い木を高い木に結合する
    if (rank[x] > rank[y]) { // xのほうが高い木 : xにyを統合
      p[y] = x;
      num_of_nodes[x] += num_of_nodes[y];
    }
    else if (rank[y] > rank[x]){ // yのほうが高い木 : yにxを統合
      p[x] = y;
      num_of_nodes[y] += num_of_nodes[x];
    }
    else {
      p[x] = y;
      rank[y]++;
      num_of_nodes[y] += num_of_nodes[x];
    }
  }

  int root(int x) {
    if (x != p[x]) { // if x is not root
      p[x] = root(p[x]);
    }
    return p[x];
  }

  int size(int x) {
    return num_of_nodes[root(x)];
  }

private:

};

int deg[MAX]; // 各ノードの出次数
vector<int> brock_to[MAX]; //各ノードへのブロック

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  UnionFind uf = UnionFind(n);

  //create united groups
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    uf.unite(a, b);
    deg[a]++; deg[b]++;
  }

  //create map for brock-brocked persons relation
  for (int j = 0; j < k; j++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    brock_to[a].push_back(b);
    brock_to[b].push_back(a);
  }

  for (int i = 0; i < n; i++) {
    int result = uf.size(i) - 1 - deg[i];
    for (int brocker : brock_to[i]) {
      if (uf.same(brocker, i) == true) result--;
    }
    if (i > 0) cout << " ";
    cout << result;
  }
  cout << endl;
  return 0;
}
