#include <bits/stdc++.h>
using namespace std;
#define MAX 10000001

const int mod = 1000000007;

vector<vector<long long>> M;
long long X, Y;

long long get_sum(long long x, long long y) {
  if (x == X && y == Y) return (long long)1;

  if (x > X || y > Y) return (long long)0;

  if (M[x][y] == MAX) {
    M[x][y] = get_sum(x+1, y+2) % mod + get_sum(x+2, y+1) % mod;
    return M[x][y];
  }
  else { return M[x][y]; }
}

int main() {
  cin >> X >> Y;

  M = vector<vector<long long>>(X+1, vector<long long>(Y+1, MAX));

  long long ans = get_sum(0, 0);
  cout << ans << endl;
  return 0;
}
