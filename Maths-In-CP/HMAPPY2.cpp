#include <iostream>

using namespace std;

long long int gcd(long long int x, long long int y){
	if(y == 0)
		return x;
	return gcd(y, x%y);
}

long long int lcm(long long int x, long long int y){
	return x*y/gcd(x,y);
}

int main(){
	int t;
	long long int a, b, n, k;
	cin >> t;
	while(t--){
		cin >> n >> a >> b >> k;
		long long int appy = n/a;
		long long int chef = n/b;
		long long int none = n/lcm(a,b);
		if(appy + chef - 2*none >= k)
			cout << "Win" << endl;
		else
			cout << "Lose" << endl;
	}
}
