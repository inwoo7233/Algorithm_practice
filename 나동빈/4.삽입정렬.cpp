# include <stdio.h>

// 각 숫자를 적절한 위치에 삽입하는 방법 
// 하나씩 하나씩 위치를 정해준다고 생각하면 편하다. 
int main(void) {
	int i, j, temp;
	int array[10] = {1,10,5,8,7,6,4,3,2,9};
	
	for(i = 0; i < 9; i++) {
		j = i;
		while (array[j] > array[j + 1]) {
			temp = array[j];
			array[j] = array[j + 1];
			array[j + 1] = temp; 
			j--;
		}
	}
	
	for(i=0; i<10; i++) {
		printf("%d ",array[i]);
	}
	return 0;
} 

// O(n * n)
// 거의 정렬된 상태라면 삽입정렬이 매우 효율적이다. 
