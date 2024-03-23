/*스택을 전역변수로 구현한 방법*/
#include<stdio.h>	
#include<stdlib.h>

#define MAX_STACK_SIZE 100	//스택의 최대 크기
typedef int element;	//데이터의 자료형
element stack[MAX_STACK_SIZE];	//1차원 배열
int top = -1;

//공백 상태 검출 함수
int is_empty() {
	return (top == -1);
}

//포화 상태 검출 함수
int is_full() {
	return (top == (MAX_STACK_SIZE - 1));
}

//삽입 함수
void push(element item) {
	if (is_full()) {
		fprintf(stderr, "Stack overflow:(\n");
		return;
	}
	else stack[++top] = item;
}

//삭제함수
element pop() {
	if (is_empty()) {
		fprintf(stderr, "Stack underflow:(\n");
		exit(1);
	}
	else return stack[top--];
}

element peek() {
	if (is_empty()) {
		fprintf(stderr, "Stack is empty:(\n");
		exit(1);
	}
	else return stack[top];
}

int main(void) {
	push(1);
	push(2);
	push(3);
	push(4);
	printf("%d\n", pop());
	printf("%d\n", pop());
	printf("%d\n", pop());
	return 0;
}