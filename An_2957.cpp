#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <algorithm>
using namespace std;

typedef int(*FCMP)(const void*, const void*);

typedef struct _node { 
	int red;
	struct _node* left;
	struct _node* right;
}node; //R-B tree를 위한 구조체

typedef struct _dep {
	int dep;
	int num;
}deps; //노드의 정보를 위한 구조체

node* head; //tree를 위한 head
int c = 0;
int put[300100];

void init_tree(node** p) { //초기화 함수
	*p = (node*)calloc(1, sizeof(node));
	(*p)->left = (*p)->right = NULL;
	(*p)->red = 0;
}

int int_cmp(const void* a, const void* b) { // 숫자 비교
	return ((deps*)a)->num - ((deps*)b)->num;  // 같으면 0을 리턴
}

//RB tree 위치 회전
void* rotate(void* key, node* pivot, node* base, int width, FCMP fcmp) {
	node* child, * gchild;
	if ((fcmp(key, pivot + 1) < 0) || pivot == base) //자식 정의
		child = pivot->left;
	else
		child = pivot->right;
	if (fcmp(key, child + 1) < 0) { //L lotate
		gchild = child->left;
		child->left = gchild->right;
		gchild->right = child;
	}
	else { //R lotate
		gchild = child->right;
		child->right = gchild->left;
		gchild->left = child;
	}
	if ((fcmp(key, pivot + 1) < 0) || pivot == base) //rotate 마무리
		pivot->left = gchild;
	else
		pivot->right = gchild;
	return gchild;
}

void* rbti_insert(void* key, node* base, int* num, int width, FCMP fcmp) {
	node* t, * parent, * gparent, * ggparent;
	ggparent = gparent = parent = base;
	t = base->left;
	while (t != NULL) {
		if (fcmp(key, t + 1) == 0) return NULL;
		if (t->left && t->right && t->left->red && t->right->red) {//왼쪽 오른쪽이 모두 red
			t->red = 1;
			t->left->red = t->right->red = 0; //뒤집기
			if (parent->red) { //t의 parent가 red라면
				gparent->red = 1; //t의 gparent를 red로 바꿈
				if ((fcmp(key, gparent + 1) < 0) != (fcmp(key, parent + 1) < 0))//LR이거나 RL이면
					parent = (node*)rotate(key, gparent, base, width, fcmp);
				t = (node*)rotate(key, ggparent, base, width, fcmp);//LL이거나 RR 이면
				t->red = 0;
			}
			base->left->red = 0; //root는 무조건 black
		}
		ggparent = gparent;
		gparent = parent;
		parent = t;
		//연결관계 정립
		if (fcmp(key, t + 1) < 0) t = t->left;
		else t = t->right;
	}
	t = (node*)malloc(sizeof(node) + width);
	memcpy(t + 1, key, width);
	t->left = t->right = NULL;
	if ((fcmp(key, parent + 1) < 0) || parent == base) parent->left = t;
	else parent->right = t;
	(*num)++;
	t->red = 1;
	//새로운 값 삽입
	if (parent->red) {
		gparent->red = 1;
		if ((fcmp(key, gparent + 1) < 0) != (fcmp(key, parent + 1) < 0))
			parent = (node*)rotate(key, gparent, base, width, fcmp);
		t = (node*)rotate(key, ggparent, base, width, fcmp);
		t->red = 0;
	}
	base->left->red = 0;
	//만약 넣자마자 red red일 경우 위쪽 반복

	return t;
}

void print(void* a){ 
	printf("%d : %d", ((deps*)a)->num, ((deps*)a)->dep);
}

void print2(void* a) {
	printf(",%d\n", ((node*)a)->red);
}

void btv_list(node* p, void(*fptr)(void*), void(*fptr2)(void*))
{
	int i;
	static int x = 0;

	if (p != NULL)
	{
		x += 2; // position for displaying a node
		// a kind of inorder traverse
		btv_list(p->right, fptr, fptr2);
		for (i = 2; i < x; i++) printf("  ");
		fptr(p + 1);
		fptr2(p);
		btv_list(p->left, fptr, fptr2);
		x -= 2;
	}
}

int upp, low;

void search(node* start, FCMP fcmp, int lower, int upper, int number) {
	node* t;
	deps* key_u, *key_l, *key_n, *dp;
	key_u = (deps*)calloc(1, sizeof(deps));
	key_u->num = upper;
	key_u->dep = -1;
	key_l = (deps*)calloc(1, sizeof(deps));
	key_l->num = lower;
	key_n = (deps*)calloc(1, sizeof(deps));
	key_n->num = number;
	dp = (deps*)calloc(1, sizeof(deps));
	t = start;
	while (1) {
		if (fcmp(key_u, t + 1) == 0) {
			memcpy(dp, t + 1, sizeof(deps));
			upp = dp->dep;
			break;
		}
		if (fcmp(key_u, t + 1) < 0)
			t = t->left;
		else if(fcmp(key_u, t + 1) > 0)
			t = t->right;
	}
	t = start;
	while (1) {
		if (fcmp(key_l, t + 1) == 0) {
			memcpy(dp, t + 1, sizeof(deps));
			low = dp->dep;
			break;
		}
		if (fcmp(key_l, t + 1) < 0)
			t = t->left;
		else if (fcmp(key_l, t + 1) > 0)
			t = t->right;
	}
	t = start;
	while (1) {
		if (fcmp(key_n, t + 1) == 0) {
			c = c + max(upp, low) + 1;
			printf("%d\n", c);
			dp->dep = max(upp, low) + 1;
			dp->num = number;
			memcpy(t + 1, dp, sizeof(deps));
			break;
		}
		if (fcmp(key_n, t + 1) < 0)
			t = t->left;
		else if (fcmp(key_n, t + 1) > 0)
			t = t->right;
	}
}

int main() {
	int num = 0, count, number, cnt = 0;
	init_tree(&head);
	deps dp;

	put[cnt++] = 0;
	dp.num = 0;
	dp.dep = -1;
	rbti_insert(&dp, head, &num, sizeof(dp), int_cmp);
	put[cnt++] = 300001;
	dp.num = 300001;
	dp.dep = -1;
	rbti_insert(&dp, head, &num, sizeof(dp), int_cmp);

	scanf("%d", &count);
	for (int i = 0; i < count; i++) {
		scanf("%d", &number);
		put[cnt++] = number;
		sort(put, put + cnt);
		int lower_b = put[lower_bound(put, put + cnt, number) - put - 1];
		int upper_b = put[upper_bound(put, put + cnt, number) - put];
		dp.num = number;
		dp.dep = -1;
		rbti_insert(&dp, head, &num, sizeof(dp), int_cmp);
		search(head->left, int_cmp, lower_b, upper_b, number);
	}
	//btv_list(head->left, print, print2);
}