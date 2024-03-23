/*스택에서 데이터를 함수의 매개변수로 전달하는 방법*/

#include<stdio.h>
#include<stdlib.h>

#define MAX_STACK_SIZE 100

typedef int element;

typedef struct StackType {	//스택을 구조체로 정의
	element data[MAX_STACK_SIZE];
	int top;
}StackType;

//스택 초기화 함수
void init_stack(StackType* s) {
	s->top = -1;	//top == -1 이면 스택이 비어있다는 의미이다.
}

//공백 상태 검출 함수
int is_empty(StackType* s) {
	return (s->top == -1);
}

//포화 상태 검출 함수
int is_full(StackType* s) {
	return(s->top == MAX_STACK_SIZE - 1);
}

//삽입함수
void push(StackType* s, element item) {
	if (is_full(s)) {
		fprintf(stderr, "Stack overflow:(\n");
		return;
	}
	else
		s->data[++(s->top)] = item;
}

//삭제함수(검출)
element pop(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "Stack underflow:(\n");
		exit(1);
	}
	else
		return s->data[(s->top)--];		//현재 데이터 필드에 있는 꼭대기의 있는 값을 꺼내서 보여주기
}

//피크함수
element peek(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "Stack is empty!:(\n");
		exit(1);
	}
	else
		return s->data[(s->top)];
}

int main(void) {
	StackType s;

	init_stack(&s);	//스택 초기화
	push(&s, 1);
	push(&s, 2);
	push(&s, 3);
	push(&s, 4);
	push(&s, 5);
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("\n스택의 맨 위에 있는 data : %d\n", peek(&s));
	/*
	출력 : 5 4 3 2
	스택의 맨 위에 있는 data : 1
	*/
	return 0;
}