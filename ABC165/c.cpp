#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define DEFINED -1

int main() {
  int N, M, Q;
  cin >> N >> M >> Q;
  vector<int> a(Q), b(Q), c(Q), d(Q);
  vector<int> A(N, 1);
  map<pair<int, int>, int> m;

  for (int i = 0; i < Q; i++) {
    cin >> a[i] >> b[i] >> c[i] >> d[i];


    A[b[i]] = A[a[i]] + c[i];

    pair<int, int> p = make_pair(b[i], a[i]);
    m[p] = -1;
  }

  for (int i = 0; i < Q; i++) {
    pair<int, int> p = make_pair(b[i], a[i]);

    if (m[p] < d[i]) m[p] = d[i];
  }

  ll sum = 0;
  for (auto item : m) {
    sum += item.second;
  }


  cout << sum << endl;
  return 0;
}
