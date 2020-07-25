#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, M, K;
  cin >> N >> M >> K;

  queue<ll> A, B;
  for (int i = 0; i < N; i++) {
    ll a;
    cin >> a;
    A.push(a);
  }

  for (int i = 0; i < M; i++) {
    ll b;
    cin >> b;
    B.push(b);
  }

  int counter = 0;
  while (K > 0) {
    if (!A.empty() && !B.empty()) {
      ll small = A.front() <= B.front() ? A.front() : B.front();
      K -= small;
      A.front() <= B.front() ? A.pop() : B.pop();
      counter ++;
    }
    else if (A.empty() && !B.empty()) {
      K -= B.front();
      B.pop();
      counter ++;
    }
    else if (!A.empty() && B.empty()){
      K -= A.front();
      A.pop();
      counter ++;
    }
    else {
      break;
    }
  }

  if (K >= 0) {
    cout << counter << endl;
  }
  else {
    cout << counter - 1 << endl;
  }

  return 0;
}
