/*������ ���� �޸� �Ҵ����� �����ϴ� ���*/

#include<stdio.h>
#include<stdlib.h>

#define MAX_STACK_SIZE 100

typedef int element;
typedef struct StackType {
	element* data;	//data�� �����ͷ� ����
	int capacity;	//���� ũ��
	int top;
}StackType;

//���� ���� �Լ�
//������ ������� ��, 1���� ��Ҹ� ������ �� �ִ� ������ �ϴ� Ȯ���Ѵ�.
void init_stack(StackType* s) {
	s->top = -1;
	s->capacity = 1;
	s->data = (element*)malloc(s->capacity * sizeof(element));
}

//���� ���� �Լ�
void delete_stack(StackType* s) {
	free(s->data);	//���� �޸� �Ҵ����� ������ �������־����Ƿ� �����Ҷ��� �޸� ������ ���ִ� free�� ���ش�.
}

//���� ���� ���� �Լ�
int is_empty(StackType* s) {
	return (s->top == -1);
}

//��ȭ ���� ���� �Լ�
int is_full(StackType* s) {
	return (s->top == s->capacity - 1);
}

//�����Լ�
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
	printf("\n������ �� ���� �ִ� �� : %d\n", peek(&s));

	free(s.data);
	//delete_stack(&s);	//�������� �����ʹ� ���� �޸� �Ҵ� ����
	return 0;
}