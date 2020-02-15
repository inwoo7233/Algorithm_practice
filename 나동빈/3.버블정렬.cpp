# include <stdio.h>

// 올라가면서 하나씩 비교하고, 큰 것을 뒤쪽으로 보내는 알고리즘 
int main(void) {
	int i, j, temp;
	int array[10] = {1,10,5,8,7,6,4,3,2,9};
	
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 9 - i; j++) {
			if (array[j] > array[j + 1]) {
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
	
	for(i=0; i<10; i++) {
		printf("%d ",array[i]);
	}
	return 0;
} 

// O(n * n)
