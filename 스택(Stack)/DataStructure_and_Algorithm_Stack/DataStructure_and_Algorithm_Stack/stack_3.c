/*���ÿ��� �����͸� �Լ��� �Ű������� �����ϴ� ���*/

#include<stdio.h>
#include<stdlib.h>

#define MAX_STACK_SIZE 100

typedef int element;

typedef struct StackType {	//������ ����ü�� ����
	element data[MAX_STACK_SIZE];
	int top;
}StackType;

//���� �ʱ�ȭ �Լ�
void init_stack(StackType* s) {
	s->top = -1;	//top == -1 �̸� ������ ����ִٴ� �ǹ��̴�.
}

//���� ���� ���� �Լ�
int is_empty(StackType* s) {
	return (s->top == -1);
}

//��ȭ ���� ���� �Լ�
int is_full(StackType* s) {
	return(s->top == MAX_STACK_SIZE - 1);
}

//�����Լ�
void push(StackType* s, element item) {
	if (is_full(s)) {
		fprintf(stderr, "Stack overflow:(\n");
		return;
	}
	else
		s->data[++(s->top)] = item;
}

//�����Լ�(����)
element pop(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "Stack underflow:(\n");
		exit(1);
	}
	else
		return s->data[(s->top)--];		//���� ������ �ʵ忡 �ִ� ������� �ִ� ���� ������ �����ֱ�
}

//��ũ�Լ�
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

	init_stack(&s);	//���� �ʱ�ȭ
	push(&s, 1);
	push(&s, 2);
	push(&s, 3);
	push(&s, 4);
	push(&s, 5);
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("%d\n", pop(&s));
	printf("\n������ �� ���� �ִ� data : %d\n", peek(&s));
	/*
	��� : 5 4 3 2
	������ �� ���� �ִ� data : 1
	*/
	return 0;
}