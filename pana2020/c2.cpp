#include <bits/stdc++.h>
using namespace std;
using ll = long long;

//floating numberを比較する場合、精度の問題で答えが正確でない場合がある
//->最も安全な方法は比較式を同値変形して整数同士の比較にする。
int main() {
  ll a, b, c;
  cin >> a >> b >> c;

  if (c-a-b < 0) {
    cout << "No" << endl;
    return 0;
  }
  if (4*a*b < (c-a-b)*(c-a-b)) {
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }

  return 0;
}
