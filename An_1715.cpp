#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nheap = 0;
unsigned long int heap[200000];

void upheap(int num) {
	unsigned long int v;
	v = heap[num];
	while (num / 2 > 0 && heap[num / 2] >= v) {
		heap[num] = heap[num / 2];
		num /= 2;
	}
	heap[num] = v;
}

void downheap(int num) {
	int i;
	unsigned long int v;
	v = heap[num];
	while (num <= nheap / 2) {
		i = num << 1;
		if (i<nheap && heap[i] > heap[i + 1]) i++;
		if (v <= heap[i]) break;
		heap[num] = heap[i];
		num = i;
	}
	heap[num] = v;
}

void pq_input(unsigned long int k) {
	heap[++nheap] = k;
	upheap(nheap);
}

unsigned long int pq_output(int num) {
	unsigned long int k = heap[num];
	heap[num] = heap[nheap--];
	downheap(num);
	return k;
}

int main() {
	int cnt, number;
	unsigned long int a, b, sum = 0;
	scanf("%d", &cnt);
	for (int i = 0; i < cnt; i++) {
		scanf("%d", &number);
		pq_input(number);
	}
	while (nheap > 1) {
		a = pq_output(1);
		b = pq_output(1);
		sum += a + b;
		pq_input(a + b);
	}
	printf("%ld", sum);
}