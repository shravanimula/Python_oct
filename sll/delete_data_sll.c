#include<stdio.h>
#include<stdlib.h>
struct st{
	int data;
	struct st *link;
};
struct st *add_last(struct st *);
void display(struct st *);
struct st *del_data(struct st *);
int main()
{
	struct st *head=NULL;
	int choice;
	while(1)
	{
		printf("1.add_last  2.display  3.delete_data  4.exit\n");
		printf("enter ur choice:\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:head=add_last(head);
			       break;
			case 2:display(head);
			       break;
			case 3:head=del_data(head);
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
struct st *del_data(struct st *ptr)
{
	struct st *temp=NULL,*prev=NULL;
	int data;
	printf("enter the data:\n");
	scanf("%d",&data);
	if(ptr==NULL)
	{
		printf("list is empty\n");
	}
	else if(data==ptr->data)//data matched with first node
	{
		temp=ptr;
		ptr=ptr->link;
		free(temp);
		temp=NULL;
	}
	else
	{
		prev=ptr;
		temp=ptr->link;
		while(temp && data!=temp->data)
		{
			prev=temp;
			temp=temp->link;
		}
		if(temp==NULL)
		{//reached the end of the file
		 printf("%d is not found\n",data);
		}
		else
		{
			prev->link=temp->link;//linking after node with before node
			free(temp);
			temp=NULL;
		}
	}
	return ptr;
}
