#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<ll, ll>;


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

struct Sieve {
  int n;
  vector<ll> f, primes;
  Sieve(ll n = 1): n(n), f(n + 1) {
    f[0] = f[1] = -1;
    for (ll i = 2; i <= n; i++) {
      if (f[i]) continue; //印がなければ素数扱い
      primes.push_back(i);
      for (ll j = i; j <= n; j += i) {
        f[j] = i; //iの倍数のところに印をつけていく
      }
    }
  }

  bool isPrime(int x) { return f[x] == x; }

  //ｘを素因数分解する関数
  // return -> 素因数
  vector<ll> factorList(ll x) {
    vector<ll> res;
    while (x != 1) {
      res.push_back(f[x]);
      x /= f[x];
    }
    return res; //大きい順で素因数がvectorに格納されて出てくる
  }

  //各素因数が何乗されているかをpair typeで返す
  vector<P> factorPower(int x) {
    vector<ll> factors = factorList(x);
    if (factors.size() == 0) return {};
    vector<P> res(1, P(factors[0], 0));
    for (int p : factors) {
      if (res.back().first == p) {
        res.back().second ++;
      }
      else {
        res.emplace_back(p, 1);
      }
    }
      return res;
    }
  };

ll nCr(ll n, ll r) {
  ll ans = 1;
  for (ll i = n; i > n - r; --i) {
    ans = ans*i;
  }
  for (ll i = 1 ; i < r + 1; ++i) {
    ans = ans / i;
  }
  return ans;
}

int main() {
  ll A, B;
  cin >> A >> B;

  Sieve s1 = Sieve(A);
  vector<ll> factorA = s1.factorList(A);
  factorA.push_back(1);

  Sieve s2 = Sieve(B);
  vector<ll> factorB = s2.factorList(B);
  factorB.push_back(1);

  UnionFind uf = UnionFind(max(factorA[0], factorB[0])+3);
  ll a_idx = max(factorA[0], factorB[0])+2;
  ll b_idx = a_idx+1;
  uf.makeSet(a_idx);
  uf.makeSet(b_idx);
  // -2::A, -1::B

  for (auto item : factorA) uf.unite(a_idx, item);
  for (auto item : factorB) uf.unite(b_idx, item);

  //ここまでは通る

  ll N = 0;
  for (ll i = 0; i < factorA.size(); i++) {
    if (uf.same(factorA[i], a_idx) && uf.same(factorA[i], b_idx)) N++;
  }

  if (N == 1) cout << 1 << endl;
  else if (2 <= N && N < 4) {
    ll ans = nCr(N, 2) + nCr(N, 2) * (N-2);
    cout << ans << endl;
  }
  else {
    ll ans = nCr(N, 2) + nCr(N, 2) * (N-2) + nCr(N, 4) * nCr(4, 2);
    cout << ans << endl;
  }
  

  return 0;

}
