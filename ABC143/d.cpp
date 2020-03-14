#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  int L[N];
  for (int i = 0; i < N; i++) cin >> L[i];

  int s = 0;
  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
      for (int k = j+1; k < N; k++) {
        int a = L[i], b = L[j], c = L[k];

        if ( (a < b+c) && (b<a+c) && (c<a+b) ) s++;
      }
    }
  }
  cout << s << endl;
  return 0;
}
