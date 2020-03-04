#include <bits/stdc++.h>
using namespace std;

long long value(long long a, long long b, long long n) {
  long long d_n = to_string(n).length();
  return a * n + b * d_n;
}

int main() {
  long long a, b, x;
  cin >> a >> b >> x;

  long long l = 1;
  long long r = 1000000000;
  long long mid_val;

  while (true) {
    if (l == r - 1) break;
    long long mid = (l + r) / 2;

    mid_val = value(a, b, mid);

    if (mid_val <= x) l = mid;
    else if (mid_val > x) r = mid;
  }
  if (value(a, b, l) <= x && x < value(a, b, r)) cout << l << endl;
  else if (value(a, b, r) <= x) cout << r << endl;
  else if (x < value(a, b, l)) cout << 0 << endl;
  //long long result = a * (i-1) + b * floor(log10(i));
  return 0;
}
