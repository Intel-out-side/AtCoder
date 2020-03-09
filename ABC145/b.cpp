#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  string S;
  cin >> N >> S;

  if (N % 2 != 0) {
    cout << "No" << endl;
  }
  else {
    string left = S.substr(0, N/2);
    string right = S.substr(N/2, N/2);
    if (left == right) cout << "Yes" << endl;
    else cout << "No" << endl;
  }

  return 0;
}
