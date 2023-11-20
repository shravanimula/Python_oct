#include<stdio.h>
#include<stdlib.h>
struct st{
	int data;
	struct st *link;
};
struct st *add_last(struct st *);
void display(struct st *);
void middle_node(struct st *);
int main()
{
	struct st *head=NULL;
	int choice;
	while(1)
	{
		printf("1.add_last  2.display  3.middle_node   4.exit\n");
		printf("enter ur choice:\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:head=add_last(head);
			       break;
			case 2:display(head);
			       break;
			case 3:middle_node(head);
			       break;
			case 4:exit(0);
		}
	}
}
struct st *add_last(struct st *ptr)
{
	struct st *newnode=NULL,*temp=NULL;
	newnode=(struct st *)malloc(sizeof(struct st));
	if(newnode==NULL)
	{
		printf("newnode is not created\n");
	}
	else
	{
		printf("enter the data\n");
		scanf("%d",&newnode->data);
		newnode->link=NULL;
		if(ptr==NULL)
		{
			ptr=newnode;
		}
		else
		{
			temp=ptr;
			while(temp->link!=NULL)
			{
				temp=temp->link;
			}
			temp->link=newnode;
		}
	}
	return ptr;
}
void display(struct st *ptr)
{
	if(ptr==NULL)
	{
		printf("list is empty\n");
	}
	else
	{
		while(ptr!=NULL)
		{
			printf("%d\n",ptr->data);
			ptr=ptr->link;
		}
	}
}

void middle_node(struct st *ptr)
{
	struct st *slow=NULL,*fast=NULL;
	if(ptr==NULL)
	{
		printf("list is empty\n");
	}
	else if(ptr->link==NULL)
	{
		printf("list is have one node\n");
	}
	else
	{
		slow=fast=ptr;
		while(slow->link!=NULL && fast->link != NULL && fast->link->link!=NULL)
		{
			slow=slow->link;
			fast=fast->link->link;
		}
		printf("middle node of list:%d\n",slow->data);
	}
}
