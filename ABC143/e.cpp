#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define MAX 301
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define INF (1<<21)

ll N, M, L;
vector<vector<ll>> town(MAX, vector<ll>(MAX, INF));

ll djkstra(ll start, ll goal) {
  int minv;
  ll d[MAX], color[MAX];
  vector<ll> route;

  for (int i = 0; i < N; i++) {
    d[i] = INF;
    color[i] = WHITE;
  }

  d[start] = 0;
  color[start] = GRAY;

  while (true) {
    minv = INF;
    ll now = -1;
    for (ll i = 0; i < N; i++) {
      if (minv > d[i] && color[i] != BLACK) {
        now = i;
        minv = d[i];
      }
    }
    if (now == -1) break;
    route.push_back(now);
    color[now] = BLACK;

    for (ll v = 0; v < N; v++) {
      if (color[v] != BLACK && town[now][v] != INF) {
        if (d[v] > d[now] + town[now][v]) {
          d[v] = d[now] + town[now][v];
          color[v] = GRAY;
        }
      }
    }
  }

  if (d[goal] == INF) return -1;

  ll s = 0;
  ll tank = L;
  cout << endl;
  for (auto item : route) cout << item << " ";
  cout << endl;
  for (ll i = 1; i < route.size(); i++) {
    if (i == goal) return s;
    if (tank < town[route[i]][route[i-1]]) {
      tank = L;
      s++;
    }
    else {
      tank -= (town[route[i]][route[i-1]]);
    }
  }
}

int main() {
  cin >> N >> M >> L;

  for (ll i = 0; i < M; i++) {
    int A, B;
    ll C;
    cin >> A >> B >> C;
    A--; B--;
    if (C > L) continue;
    town[A][B] = town[B][A] = C;
  }

  ll Q;
  cin >> Q;
  for (ll i = 0; i < Q; i++) {
    int s, t;
    cin >> s >> t;
    s--; t--;

    cout << djkstra(s, t) << endl;
  }
  return 0;
}
