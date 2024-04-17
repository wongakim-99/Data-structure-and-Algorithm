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
		printf("연결할 데이터 입력 : ");
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
        printf("삭제할 데이터를 입력하세요.");
        scanf("%d", &k);

        if (k <= 0)break;

        int search = 0;
        Node* cur_prev = NULL;
        cur = head;
        while (1)
        {
            int k;
            printf("삭제할 데이터를 입력하세요. ");
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
                printf("%d를 삭제합니다.\n", k);

                if (cur == head) head = cur->next;
                else cur_prev->next = cur->next;

                free(cur);
            }
            else
            {
                printf("%d를 찾을 수 없습니다.\n", k);
            }
        }

        printf("(삭제 후) 연결리스트 현재 상태 : ");
        cur = head;
        while (cur != NULL)
        {
            printf("%d ", cur->data);
            cur = cur->next;
        }
        puts("");
    }
}