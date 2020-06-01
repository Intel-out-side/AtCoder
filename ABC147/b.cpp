#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  int sum = 0;
  for (int i = 0; i < s.length()/2; i++) {
    if (s[i] != s[s.length()-1-i]) sum++;
  }
  cout << sum << endl;
  return 0;
}
