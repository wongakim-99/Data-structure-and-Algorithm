/*스택의 요소를 구조체로 하기*/

#include<stdio.h>	
#include<stdlib.h>
#define MAX_STACK_SIZE 100
#define MAX_STRING 100

typedef struct element {
	int student_no;
	char name[MAX_STRING];
	char address[MAX_STRING];
}element;

element stack[MAX_STACK_SIZE];
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
		fprintf(stderr, "Stack overflow :(\n");
		return;
	}
	else stack[++top] = item;
}

//삭제 함수
element pop() {
	if (is_empty()) {
		fprintf(stderr, "Stack underflow :(\n");
		exit(1);
	}
	else return stack[top--];
}

//피크 함수
element peek() {
	if (is_empty()) {
		fprintf(stderr, "Stack is empty :(\n");
		exit(1);
	}
	else return stack[top];
}

int main(void) {
	element ie = {
		202021000,
		"Kim",
		"Bundang"
	};
	element oe;

	push(ie);
	oe = pop();

	printf("학번 : %d\n", oe.student_no);
	printf("이름 : %s\n", oe.name);
	printf("주소 : %s\n", oe.address);
	return 0;
}