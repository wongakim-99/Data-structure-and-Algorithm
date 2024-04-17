#pragma warning(disable : 4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct node_ {
	int data;
	struct node_* next;
}Node;

Node* head = NULL;
Node* tail = NULL;

int main() {
	while (1) {
		int input;
		printf("������ ������ �Է� : ");
		scanf("%d", &input);

		if (input <= 0)
			break;

		Node* newnode = (Node*)malloc(sizeof(Node));

		newnode->data = input;
		newnode->next = NULL;

		if (head == NULL)head = newnode;
		else tail->next = newnode;

		tail = newnode;
	}
	printf("");
	Node* cur = head;
	while (cur != NULL) {
		printf("%d", cur->data);
		cur = cur->next;
	}
	puts("");

    while (1) {
        int k;
        printf("������ �����͸� �Է��ϼ���.");
        scanf("%d", &k);

        if (k <= 0)break;

        int search = 0;
        Node* cur_prev = NULL;
        cur = head;
        while (1)
        {
            int k;
            printf("������ �����͸� �Է��ϼ���. ");
            scanf("%d", &k);

            if (k <= 0) break;

            int search = 0;
            Node* cur_prev = NULL;
            cur = head;
            while (cur != NULL)
            {
                if (cur->data == k)
                {
                    search = 1;
                    break;
                }
                cur_prev = cur;
                cur = cur->next;
            }

            if (search == 1)
            {
                printf("%d�� �����մϴ�.\n", k);

                if (cur == head) head = cur->next;
                else cur_prev->next = cur->next;

                free(cur);
            }
            else
            {
                printf("%d�� ã�� �� �����ϴ�.\n", k);
            }
        }

        printf("(���� ��) ���Ḯ��Ʈ ���� ���� : ");
        cur = head;
        while (cur != NULL)
        {
            printf("%d ", cur->data);
            cur = cur->next;
        }
        puts("");
    }
}