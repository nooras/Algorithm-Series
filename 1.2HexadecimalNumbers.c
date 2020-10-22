// https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/

// Date : 22/10/2020

#include <stdio.h>
int sumOfHex(int n){
	int sum = 0;
	while(n){
		sum+=n%16;
		n/=16;
	}
	return sum;
}
int gcd(int a, int b){
	if(a%b==0)return b;
	return gcd(b,a%b);
}
int isGreatGcd(int a, int b){
	if(gcd(a,b)>1)return 1;
	else return 0;
}
int main(){
	int T;
	scanf("%d",&T);
	int sumHex[100001];
	sumHex[0]=0;
	for(int i=1;i<=100000;i++){
		sumHex[i]=sumHex[i-1] + isGreatGcd(i, sumOfHex(i));
	}
	while(T--){
		int L,R;
		scanf("%d %d",&L,&R);
		int res = sumHex[R]-sumHex[L-1];
		printf("%d\n",res);
	}
	return 0;
}
