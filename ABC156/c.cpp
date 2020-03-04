#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> x(n);
  for (int i = 0; i < n; i++) cin >> x[i];

  int sum = 0;
  for (int i = 0; i < n; i++) sum += x[i];
  float ave = (float)sum / n;
  int int_ave = round(ave);

  long long min_sum = 0;
  for (int i = 0; i < n; i++) min_sum += (x[i] - int_ave) * (x[i] - int_ave);

  cout << min_sum << endl;
  return 0;
}
