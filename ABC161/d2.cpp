#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
	ll K;
	cin >> K;

	queue<ll> q;

	for (ll i = 1; i <= 9; i++) q.push(i);

	for (ll i = 1; i <= K; i++) {
		ll front = q.front();
		q.pop();

		if (i == K) cout << front << endl;


		if ((front % 10) == 9) {
			ll a = 10 * front + (front % 10 - 1);
			ll b = 10 * front + front % 10;
			q.push(a); q.push(b);
		}
		else if ((front % 10) == 0) {
			ll a = 10 * front + front % 10;
			ll b = 10 * front + (front % 10 + 1);
			q.push(a); q.push(b);
		}
		else {
			ll a = 10 * front + (front % 10 - 1);
			ll b = 10 * front + front % 10;
			ll c = 10 * front + (front % 10 + 1);
			q.push(a); q.push(b); q.push(c);
		}
	}

	return 0;

}
