#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {
  long long N, K;
  long long R, S, P;
  string T;
  long long sum = 0;

  cin >> N >> K;
  cin >> R >> S >> P;
  cin >> T;

  string ownPlays = "";

  for (long long i = 0; i < N; i++){
    if (i - K > 0) {
      char playsBackToKth = ownPlays[i - K];
      if (T[i] == 's') {
        if (playsBackToKth == 'r') ownPlays += 's';
        else ownPlays += 'r';
      }
      else if (T[i] == 'r') {
        if (playsBackToKth == 'p') ownPlays += 'r';
        else ownPlays += 'p';
      }
      else if (T[i] == 'p') {
        if (playsBackToKth == 's') ownPlays += 'p';
        else ownPlays += 's';
      }
    }

    else {
        if (T[i] == 'r') ownPlays += 'p';
        else if (T[i] == 'p') ownPlays += 's';
        else if (T[i] == 's') ownPlays += 'r';
    }
  }
  for (long long i = 0; i < N; i++) {
    if (ownPlays[i] == 'r' && T[i] != 'r') sum += R;
    else if (ownPlays[i] == 's' && T[i] != 's') sum += S;
    else if (ownPlays[i] == 'p' && T[i] != 'p') sum += P;
  }
  cout << sum << endl;
  return 0;
}
