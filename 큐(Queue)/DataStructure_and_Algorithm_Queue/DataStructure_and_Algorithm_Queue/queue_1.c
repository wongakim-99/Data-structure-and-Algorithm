//선형 큐 구현 프로그램

#include<stdio.h>
#include<stdlib.h>
#define MAX_QUEUE_SIZE 5

typedef int element;

typedef struct QueueType {
	int front;
	int rear;
	element data[MAX_QUEUE_SIZE];
}QueueType;

//큐 초기화 함수
void init_queue(QueueType* q) {
	q->rear = -1;
	q->front = -1;
}

//큐 포화상태 검출
int is_full(QueueType* q) {
	if (q->rear == MAX_QUEUE_SIZE - 1)	//이렇게 되면 큐의 포화상태
		return 1;
	else
		return 0;
}

//큐 공백상태 검출
int is_empty(QueueType* q) {
	if (q->front == q->rear)	//front와rear가 같으면 큐가 공백상태
		return 1;
	else
		return 0;
}

//큐 삽입함수
void enqueue(QueueType* q, int item) {
	if (is_full(q)) {
		fprintf(stderr, "Queue is full:(\n");
		exit(1);
	}
	q->data[++(q->rear)] = item;
}

//큐 삭제함수
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