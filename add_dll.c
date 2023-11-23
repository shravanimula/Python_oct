#include<stdio.h>
#include<stdlib.h>
struct st {
	int data;
	struct st *prev,*link;
};
struct st *add_last(struct st *);
void display(struct st *);
int main()
{
	int choice;
	struct st *head=NULL;
	while(1)
	{
		printf("1.add_lat 2.display 3.exit\n");
		printf("enter ur choice:\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:head=add_last(head);
			       break;
			case 2:display(head);
			       break;
			case 3:exit(0);
		}
	}
}
struct st *add_last(struct st *ptr)
{
	struct st *newnode=NULL,*temp=NULL;
	newnode=(struct st *)malloc(sizeof(struct st));
	if(newnode==NULL)
	{
		printf("node not created\n");
	}
	else
	{
		printf("enter the data:\n");
		scanf("%d",&newnode->data);
		newnode->link=NULL;
		newnode->prev=NULL;
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
			newnode->prev=temp;
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
