#include<stdio.h>
#include<stdlib.h>

//=====����ť �ڵ� ����=====
#define MAX_QUEUE_SIZE 5
typedef int element;
typedef struct QueueType {
	element data[MAX_QUEUE_SIZE];
	int front, rear;
}QueueType;

//ť �ʱ�ȭ �Լ�
void init_queue(QueueType* q) {
	q->front = q->rear = 0;
}

//���� ���� ���� �Լ�
int is_empty(QueueType* q) {
	return (q->front == q->rear);
}

//��ȭ ���� ���� �Լ�
int is_full(QueueType* q) {
	return ((q->rear + 1) & MAX_QUEUE_SIZE == q->front);
}

//���� �Լ�
void enqueue(QueueType* q, element item) {
	if (is_full(q)) {
		fprintf(stderr, "Queue is full:(\n");
		exit(1);
	}
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->data[q->rear] = item;
}

//���� �Լ�
element dequeue(QueueType* q) {
	if (is_empty(q)) {
		fprintf(stderr, "Queue is empty:(\n");
		exit(1);
	}
	q->front = (q->front + 1) % MAX_QUEUE_SIZE;
	return q->data[q->front];
}

element peek(QueueType* q) {
	if (is_empty(q)) {
		fprintf(stderr, "Queue is empty:(\n");
		exit(1);
	}
	return q->data[(q->front + 1) % MAX_QUEUE_SIZE];
}

int main() {
	QueueType queue;
	init_queue(&queue); // ť �ʱ�ȭ

	// ����ť�� �� ����
	enqueue(&queue, 10);
	enqueue(&queue, 20);
	enqueue(&queue, 30);
	enqueue(&queue, 40);

	printf("Front of the queue: %d\n", peek(&queue)); // ť�� �� �� �� Ȯ��

	// ����ť���� �� ����
	printf("Dequeued item: %d\n", dequeue(&queue));
	printf("Dequeued item: %d\n", dequeue(&queue));

	// ���ο� �� �߰�
	enqueue(&queue, 50);
	enqueue(&queue, 60);

	// ���� ť�� ���� Ȯ��
	printf("Front of the queue: %d\n", peek(&queue));
	printf("Is the queue full? %s\n", is_full(&queue) ? "Yes" : "No");
	printf("Is the queue empty? %s\n", is_empty(&queue) ? "Yes" : "No");

	return 0;
}
