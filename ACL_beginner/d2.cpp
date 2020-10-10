#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int op(int a, int b){
    return max(a, b);
}

int e(){
    return 0;
}

int main(void){
	int N,K,x,i,ans=0;
	segtree <int, op, e> seg(300010);

	cin >> N >> K;

	REP(i,N){
		cin >> x;
		int L = max(x - K, 0);
		int R = min(x + K, 300000);
		int tmp = seg.prod(L, R+1) + 1;
		ans = max(ans, tmp);
		seg.set(x, tmp);
	}

	cout << ans << endl;

	return 0;
}
