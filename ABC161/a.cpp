#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, y, z;
  cin >> x >> y >> z;

  int a = x, b = y, c = z;

  int tmp;
  tmp = a;
  a = b;
  b = tmp;

  tmp = a;
  a = c;
  c = tmp;

  cout << a << " " << b << " " << c << endl;
  return 0;
}
