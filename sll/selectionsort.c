#include<stdio.h>
#define SIZE 50
void selection_sort(int [],int);
int main()
{
	int array[SIZE],n,i;
	printf("enter the array size:");
	scanf("%d",&n);
	printf("enter the array elements are:\n");
	for(i=0;i<n;i++)
		scanf("%d",&array[i]);
	printf("before sort the array is:\n");
	for(i=0;i<n;i++)
		printf("%d\t",array[i]);
	void(*fptr)(int [], int)=selection_sort;
	fptr(array,n);
}
void selection_sort(int a[],int n)
{
	int i,j,min,temp;
	for(i=0;i<n-1;i++)
	{
		min=i;
		for(j=i+1;j<n;j++)
		{
			if(a[j] < a[min])
			{
				min=j;
			}
		}
		if(min!=i)
		{
			temp=a[min];
			a[min]=a[i];
			a[i]=temp;
		}
	}
	printf("\nafter sorting the array is:\n");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
}
