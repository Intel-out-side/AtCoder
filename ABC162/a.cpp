#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  string a = to_string(n);

  if (a[0] == '7' || a[1] == '7' || a[2] == '7') cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}
