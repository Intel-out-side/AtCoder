#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N, M;
  cin >> N >> M;
  priority_queue<double> A;
  for (int i = 0; i < N; i++) {
    ll tmp;
    cin >> tmp;
    A.push(tmp);
  }

  for (int i = 0; i < M; i++) {
    ll tmp = A.top(); A.pop();
    tmp /= 2;
    A.push(tmp);
  }

  ll sum = 0;
  for (int i = 0; i < N; i++) {
    sum += (ll)A.top();
    A.pop();
  }

  cout << sum << endl;
  return 0;
}
