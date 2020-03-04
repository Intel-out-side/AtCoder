#include <bits/stdc++.h>
using namespace std;
#define NIL -1

int main() {
  int A[3][3];

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      int tmp;
      cin >> tmp;
      A[i][j] = tmp;
    }
  }

  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    for (int j = 0; j < 3; j++) {
      for (int k = 0; k < 3; k++) {
        if (A[j][k] == tmp) A[j][k] = NIL;
      }
    }
  }

  bool isBingo = false;
  //縦
  if (A[0][0] == A[1][0] && A[1][0] == A[2][0]) isBingo = true;
  if (A[0][1] == A[1][1] && A[1][1] == A[2][1]) isBingo = true;
  if (A[0][2] == A[1][2] && A[1][2] == A[2][2]) isBingo = true;

  if (A[0][0] == A[0][1] && A[0][1] == A[0][2]) isBingo = true;
  if (A[1][0] == A[1][1] && A[1][1] == A[1][2]) isBingo = true;
  if (A[2][0] == A[2][1] && A[2][1] == A[2][2]) isBingo = true;

  if (A[0][0] == A[1][1] && A[1][1] == A[2][2]) isBingo = true;
  if (A[0][2] == A[1][1] && A[2][0] == A[1][1]) isBingo = true;

  if (isBingo) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}
