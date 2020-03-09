#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  int index = 0;
  bool isHitachi = true;
  while (index < S.length()) {
    string str = S.substr(index, 2);
    if (str != "hi") isHitachi = false;
    index += 2;
  }

  if (isHitachi) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
