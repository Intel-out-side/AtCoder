#include <bits/stdc++.h>
#define rep(i, n) for(long long i = 0; i < n; i++)
#define MAX 1e4 + 1
using namespace std;
using ll = long long;
using P = pair<int, int>;
ll HP = MAX;
vector<P> candidates;

vector<P> f(vector<P> x) {
  ll len = x.size();
  ll minCost = MAX;
  ll sumDamage = -1;
  sort(x.begin(), x.end());
  for (auto p : x) {
    if (p.first > HP) {
      sumDamage = p.first;
      if (p.second < minCost) minCost = p.second;
    }
  }
  if (sumDamage > HP) {
    vector<P> result = {P(sumDamage, minCost)};
    return result;
  }
  else {
    for (auto p : x) {
      for (auto q : candidates) {
        x.push_back(P( p.first + q.first, p.second + q.second ));
      }
    }
    for (ll i = 0; i < len; i++) x.erase(x.begin());
    return f(x);
  }
}

void vprint(vector<P> x) {
  for (int i = 0; i < x.size(); i++) {
    cout << x[i].first << " " << x[i].second << endl;
  }
}

int main() {
  int H, N;
  cin >> H >> N;
  HP = H;
  vector<int> A(N), B(N), cost(N);
  vector<P> ab(N);
  rep(i, N) cin >> A[i] >> B[i];
  rep(i, N) ab.push_back(P(A[i], B[i]));
  candidates = ab;
  cout << HP << endl;
  vprint(candidates);

  ll minCost = f(ab)[0].second;
  cout << minCost << endl;
  return 0;
}
