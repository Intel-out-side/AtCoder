#include <bits/stdc++.h>
using namespace std;
# define M_PI 3.14159265358979323846

int main() {
  int a, b, x;
  cin >> a >> b >> x;

  double s = (2 * x)/((double)a * b);

  double theta;
  if (s > a) {
    theta = atan(((double)b - (double)x/a/a)*2/a);
  }
  else {
    theta = atan((double)a*b*b/2/x);
  }

  double deg = theta * 180 / M_PI;

  cout << fixed << setprecision(7);
  cout << deg << endl;
  return 0;
}
