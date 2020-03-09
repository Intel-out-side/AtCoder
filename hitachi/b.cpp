#include <bits/stdc++.h>
using namespace std;
#define MAX 100010

int main() {
  long long A, B, M;
  cin >> A >> B >> M;

  vector<long long> a(A, 0), b(B, 0);
  vector<vector<long long>> m(M, vector<long long>(3, 0));
  for (long long i = 0; i < A; i++) {
    long long tmp; cin >> tmp;
    a[i] = tmp;
  }
  for (long long j = 0; j < B; j++) {
    long long tmp; cin >> tmp;
    b[j] = tmp;
  }

  for (long long k = 0; k < M; k++) {
    long long x, y, c;
    cin >> x >> y >> c;
    m[k][0] = x - 1;
    m[k][1] = y - 1;
    m[k][2] = c;
  }

  // a, b 単体でのminを見つける
  long long a_min = a[0], b_min = b[0];
  for (long long i = 0; i < A; i++) a_min > a[i] ? a_min = a[i] : a_min = a_min;
  for (long long i = 0; i < B; i++) b_min > b[i] ? b_min = b[i] : b_min = b_min;
  long long normal_min = a_min + b_min;

  // 割引対象になっているもののなかから最小のものを見つける
  long long discount_min = a[m[0][0]] + b[m[0][1]] - m[0][2];
  for (long long i = 0; i < M; i++) {
    long long tmp = a[m[i][0]] + b[m[i][1]] - m[i][2];
    discount_min > tmp ? discount_min = tmp : discount_min = discount_min;
  }

  if (discount_min > normal_min) cout << normal_min << endl;
  else cout << discount_min << endl;
  return 0;
}
