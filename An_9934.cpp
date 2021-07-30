#include <iostream>
#include <math.h>
using namespace std;

typedef struct _node {
	int count;
	struct _node* next;
}node;

int tree[2000];
node *result[10];

void init() {
	for (int i = 0; i < 10; i++)
		result[i] = NULL;
}//초기화

void recur(int count, int start, int end) {
	if (start != end) {//만약 start end가 다르면 계속 recur
		node* t;
		t = (node*)calloc(1, sizeof(node));
		t->count = tree[(start + end) / 2];
		t->next = result[count];
		result[count] = t;
		recur(count + 1, (start + end) / 2 + 1, end);
		recur(count + 1, start, (start + end) / 2 - 1);
	}
	else {//같으면 list에 넣어주고 종료
		node* t;
		t = (node*)calloc(1, sizeof(node));
		t->count = tree[start];
		t->next = result[count];
		result[count] = t;
	}
}

void print(int num) {//출력
	for (int i = 0; i < num; i++) {
		for (node* t = result[i]; t; t = t->next)
			cout << t->count << " ";
		cout << "\n";
	}
}

int main() {
	int num;
	cin >> num;
	for (int i = 0; i < pow(2, num) - 1; i++)
		cin >> tree[i];
	init();
	recur(0, 0, pow(2, num) - 2);
	print(num);
}
//43분