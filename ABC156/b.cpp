#include <bits/stdc++.h>
using namespace std;

int main() {
  long long n;
  int k;
  cin >> n >> k;

  long long res = 0;
  while (n != 0) {
    res++;
    n = n / k;
  }

  cout << res << endl;
  return 0;
}
