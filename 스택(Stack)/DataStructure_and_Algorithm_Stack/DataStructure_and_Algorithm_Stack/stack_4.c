/*스택을 동적 메모리 할당으로 생성하는 방법*/

#include<stdio.h>
#include<stdlib.h>

#define MAX_STACK_SIZE 100

typedef int element;
typedef struct StackType {
	element* data;	//data는 포인터로 정의
	int capacity;	//현재 크기
	int top;
}StackType;

//스택 생성 함수
//스택이 만들어질 때, 1개의 요소를 저장할 수 있는 공간을 일단 확보한다.
void init_stack(StackType* s) {
	s->top = -1;
	s->capacity = 1;
	s->data = (element*)malloc(s->capacity * sizeof(element));
}

//스택 삭제 함수
void delete_stack(StackType* s) {
	free(s->data);	//동적 메모리 할당으로 스택을 생성해주었으므로 삭제할때는 메모리 해제를 해주는 free를 해준다.
}

//공백 상태 검출 함수
int is_empty(StackType* s) {
	return (s->top == -1);
}

//포화 상태 검출 함수
int is_full(StackType* s) {
	return (s->top == s->capacity - 1);
}

//삽입함수
void push(StackType* s, element item) {
	if (is_full(s)) {
		s->capacity *= 2;
		s->data = (element*)realloc(s->data, s->capacity * sizeof(element));
	}
	s->data[++(s->top)] = item;
}

element pop(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "Stack underflow:(\n");
		exit(1);
	}
	else return s->data[(s->top)--];
}

element peek(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "Stack is empty!:(\n");
		exit(1);
	}
	return s->data[(s->top)];
}

int main(void) {
	StackType s;
	init_stack(&s);
	push(&s, 1);
	push(&s, 2);
	push(&s, 3);
	push(&s, 4);
	push(&s, 5);
	push(&s, 6);
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("\n스택의 맨 위에 있는 값 : %d\n", peek(&s));

	free(s.data);
	//delete_stack(&s);	//빠져나온 데이터는 동적 메모리 할당 해제
	return 0;
}