#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  bool isEasy = true;
  for (int i = 1; i < S.length(); i += 2) {
    if (S[i] == 'R') isEasy = false;
  }

  for (int i = 0; i < S.length(); i += 2) {
    if (S[i] == 'L') isEasy = false;
  }

  if (isEasy) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}
