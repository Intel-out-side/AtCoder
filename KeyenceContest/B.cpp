#include <bits/stdc++.h>
#include <algorithm>
#define rep(i, n) for(long long i = 0; i < n; i++)
#define MAX 10e9
using namespace std;
using ll = long long;
using P = pair<ll, ll>;

void vprint(vector<P> v);

int main() {
  ll N;
  cin >> N;
  vector<ll> X(N), L(N);
  vector<P> answers;
  ll current = -MAX;
  ll sum = 0;
  rep(i, N) {
    cin >> X[i] >> L[i];
  }

  vector<P> robots;

  rep(i, N) {
    robots.push_back(P(X[i] + L[i], X[i] - L[i]));
  }

  sort(robots.begin(), robots.end());
  //vector<pair<int, int>> をソートすると、デフォルトではpair型.firstの
  //小さい順にソートするようになっている
  //参照:https://www.geeksforgeeks.org/sorting-vector-of-pairs-in-c-set-1-sort-by-first-and-second/

  rep(i, N) {
    if (current <= robots[i].second) {
      sum++;
      current = robots[i].first;
      answers.push_back(robots[i]);
    }
  }

  cout << sum << endl;

  return 0;
}
