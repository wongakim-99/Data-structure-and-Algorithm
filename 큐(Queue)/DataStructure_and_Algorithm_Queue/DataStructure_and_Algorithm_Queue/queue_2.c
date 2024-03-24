#include<stdio.h>
#include<stdlib.h>

//=====원형큐 코드 시작=====
#define MAX_QUEUE_SIZE 5
typedef int element;
typedef struct QueueType {
	element data[MAX_QUEUE_SIZE];
	int front, rear;
}QueueType;

//큐 초기화 함수
void init_queue(QueueType* q) {
	q->front = q->rear = 0;
}

//공백 상태 검출 함수
int is_empty(QueueType* q) {
	return (q->front == q->rear);
}

//포화 상태 검출 함수
int is_full(QueueType* q) {
	return ((q->rear + 1) & MAX_QUEUE_SIZE == q->front);
}

//삽입 함수
void enqueue(QueueType* q, element item) {
	if (is_full(q)) {
		fprintf(stderr, "Queue is full:(\n");
		exit(1);
	}
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->data[q->rear] = item;
}

//삭제 함수
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
	init_queue(&queue); // 큐 초기화

	// 원형큐에 값 삽입
	enqueue(&queue, 10);
	enqueue(&queue, 20);
	enqueue(&queue, 30);
	enqueue(&queue, 40);

	printf("Front of the queue: %d\n", peek(&queue)); // 큐의 맨 앞 값 확인

	// 원형큐에서 값 삭제
	printf("Dequeued item: %d\n", dequeue(&queue));
	printf("Dequeued item: %d\n", dequeue(&queue));

	// 새로운 값 추가
	enqueue(&queue, 50);
	enqueue(&queue, 60);

	// 현재 큐의 상태 확인
	printf("Front of the queue: %d\n", peek(&queue));
	printf("Is the queue full? %s\n", is_full(&queue) ? "Yes" : "No");
	printf("Is the queue empty? %s\n", is_empty(&queue) ? "Yes" : "No");

	return 0;
}
