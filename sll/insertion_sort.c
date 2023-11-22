#include<stdio.h>
#define SIZE 50
void insertion_sort(int [],int);
int main()
{
	int n,array[SIZE],i;
	printf("enter the array size:");
	scanf("%d",&n);
	printf("enter the array elements:\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&array[i]);
	}
	printf("before sort the array elements are:");
	for(i=0;i<n;i++)
		printf("%d\t",array[i]);
	void(*fptr)(int [],int)=insertion_sort;
	fptr(array,n);
}
void insertion_sort(int a[],int n)
{
	int i,j,temp;
	for(i=1;i<n;i++)
	{
		temp=a[i];
		j=i-1;
		while(j>=0 && a[j]>temp)
		{
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=temp;
	}
	printf("\nafter sorting the array is:\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
}
