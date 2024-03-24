//���� ť ���� ���α׷�

#include<stdio.h>
#include<stdlib.h>
#define MAX_QUEUE_SIZE 5

typedef int element;

typedef struct QueueType {
	int front;
	int rear;
	element data[MAX_QUEUE_SIZE];
}QueueType;

//ť �ʱ�ȭ �Լ�
void init_queue(QueueType* q) {
	q->rear = -1;
	q->front = -1;
}

//ť ��ȭ���� ����
int is_full(QueueType* q) {
	if (q->rear == MAX_QUEUE_SIZE - 1)	//�̷��� �Ǹ� ť�� ��ȭ����
		return 1;
	else
		return 0;
}

//ť ������� ����
int is_empty(QueueType* q) {
	if (q->front == q->rear)	//front��rear�� ������ ť�� �������
		return 1;
	else
		return 0;
}

//ť �����Լ�
void enqueue(QueueType* q, int item) {
	if (is_full(q)) {
		fprintf(stderr, "Queue is full:(\n");
		exit(1);
	}
	q->data[++(q->rear)] = item;
}

//ť �����Լ�
int dequeue(QueueType* q) {
	if (is_empty(q)) {
		fprintf(stderr, "Queue is empty:(\n");
		exit(1);
	}
	int item = q->data[++(q->front)];
	return item;
}

int main(void) {
	int item = 0;
	QueueType q;
	init_queue(&q);

	enqueue(&q, 10);
	enqueue(&q, 20);
	enqueue(&q, 30);
	enqueue(&q, 40);

	printf("%d\n", dequeue(&q));
	printf("%d\n", dequeue(&q));
	printf("%d\n", dequeue(&q));

	return 0;
}