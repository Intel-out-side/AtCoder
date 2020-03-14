#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  string S;
  cin >> S;

  stack<char> st;
  st.push(S[0]);

  for (ll i = 1; i < N; i++) {
    if (st.top() != S[i]) st.push(S[i]);
  }

  ll res = st.size();
  cout << res << endl;
  return 0;
}
