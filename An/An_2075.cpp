#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _node {
	int cod;
	int weight;
}node;

int** num_2;
int nheap = 0;
node heap[2000];

void upheap(int num) {
	node v;
	v = heap[num];
	while (num / 2 > 0 && heap[num / 2].weight <= v.weight) {
		heap[num] = heap[num / 2];
		num /= 2;
	}
	heap[num] = v;
}

void downheap(int num) {
	int i;
	node v;
	v = heap[num];
	while (num <= nheap / 2) {
		i = num << 1;
		if (i<nheap && heap[i].weight < heap[i + 1].weight) i++;
		if (v.weight >= heap[i].weight) break;
		heap[num] = heap[i];
		num = i;
	}
	heap[num] = v;
}

int find(int num) {
	int count = 0;
	node val;
	for (int i = 0; i < num; i++) {
		heap[++nheap].weight = num_2[num - 1][i];
		heap[nheap].cod = (num - 1) * num + i;
		upheap(nheap);
	}
	while (count != num) {
		val = heap[1];
		heap[1] = heap[nheap--];
		downheap(1);
		count++;
		if (val.cod < num)
			continue;
		heap[++nheap].weight = num_2[val.cod/num - 1][val.cod%num];
		heap[nheap].cod = val.cod - num;
		upheap(nheap);
	}
	return val.weight;
}

int main() {
	int num, val, result;
	scanf("%d", &num);

	num_2 = (int**)calloc(num, sizeof(int*));
	for (int i = 0; i < num; i++)
		num_2[i] = (int*)calloc(num, sizeof(int));

	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			scanf("%d", &val);
			num_2[i][j] = val;
		}
	}

	result = find(num);
	printf("%d", result);

	for (int k = 0; k < num; k++)
		free(num_2[k]);
	free(num_2);
}