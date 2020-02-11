#include <stdio.h>

int number = 10;
int data[] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void show() {
   int i;
   for(i = 0; i < number; i++) {
      printf("%d ", data[i]);
   }
   printf("\n");
}

void quickSort(int* data, int start, int end) {
   int small = start;
   int big = start + 1;
   int find = start + 1;
   int temp;
   
	if (start >= end) {
		return;
	}   
	
	if (data[small] > data[big]) {
		temp = data[small];
		data[small] = data[big];
		data[big] = data[small];
	}
	
   while (find < end) {
		if (data[end] > data[find]) {
			temp = data[find];
	   		data[find] = data[big];
	   		data[big] = temp;
	   		small++;
	   		big++;
	   	}  	
	   	find++;
    }
	
	temp = data[big];
   	data[big] = data[end];
   	data[end] = temp;
   	
   	show();
   	
   	quickSort(data, start, small);
   	quickSort(data, big, end);
}

int main(void) {
   quickSort(data, 0, number - 1);
   show();
   return 0;
}

// 최악의 경우 O(N^2), 평균적으로는 O(N*logN)을 가진다. 
