#include<stdio.h>
#define SIZE 50
void bubble_sort(int [],int);
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
	printf("before sort the array elements are:\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",array[i]);
	}
	void(*fptr)(int [],int)=bubble_sort;
	fptr(array,n);

}
void bubble_sort(int a[],int n)
{
	int i,j,temp;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(a[j] > a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	printf("\nafter sort the array elements are:\n");
        for(i=0;i<n;i++)
                printf("%d\t",a[i]);
	printf("\n");
}
