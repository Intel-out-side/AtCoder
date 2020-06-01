#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  int P[N][N];
  int isHonest[N];

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      P[i][j] = 1;
    }
  }

  for (int i = 0; i < N; i++) isHonest[i] = 1;

  for (int i = 0; i < N; i++) {
    int A;
    cin >> A;
    for (int j = 0; j < A; j++) {
      int x, y;
      cin >> x >> y;
      P[i][x] = y;
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
      if (P[i][j] == 1 && P[i][j] == 1) {
        isHonest[i] = 1;
        isHonest[j] = 1;
      }
      else if (P[i][j] == 1 && P[j][i] == 0) {
        isHonest[i] = 0;
        isHonest[j] = 1;
      }
      else if (P[i][j] == 0 && P[j][i] == 1) {
        isHonest[i] = 1;
        isHonest[j] = 0;
      }
      else {
        isHonest[i] = 0;
        isHonest[j] = 0;
      }
    }
  }

  int sum = 0;
  for (int i = 0; i < N; i++) isHonest[i] ? sum++ : sum = sum;

  cout << sum << endl;
  return 0;

}
