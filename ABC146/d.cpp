#include <bits/stdc++.h>
using namespace std;

long N;
long M[N+1][N+1];
long color[N+1];
long visit_next[N+1];

int main() {
  cin >> N;

  for (int i = 0; i <= N; i++) {
    for (int j = 0; j <= N; j++) M[i][j] = 0;
  }

  for (long i = 1; i <= N; i++) {
    long a, b;
    cin >> a >> b;
    M[a][b] = M[b][a] = 1;
  }


}
