#include <stdlib.h>
#include <stdio.h>

int partition(int array[], int start, int end);
void quick_sort(int array[], int start, int end);
void swap(int *a, int *b);
void print_arr(int array[], int size);

int main() {

    int size;
    printf("What's the array size: ");
    scanf("%d", &size);
    
    int array[size];

    for(int i=0; i<size; i++){
        printf("Enter element %d : ",i+1);
        scanf("%d", &array[i]);
    }

    printf("\nBefore sort, array is: ");
    print_arr(array, size);
    quick_sort(array, 0, size-1);
    printf("\nAfter sort, array is: ");
    print_arr(array, size);

    return 0;
}

int partition(int array[], int start, int end){
    
    int pivot = array[end]; //pivot elt
    int i = start - 1;

    for (int j = start; j <= end-1; j++) {
        //if current elt is smaller than pivot, increment the index
        if (array[j] <= pivot) {
            i++;
            swap(&array[i], &array[j]);
        }
    }

    //place pivot in i+1th position when done
    swap(&array[i+1], &array[end]);

    return i+1;
}


void quick_sort(int array[], int start, int end){
    if (start < end) {
        int part_index = partition(array, start, end);
        quick_sort(array, start, part_index-1);
        quick_sort(array, part_index+1, end);
    }

}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void print_arr(int array[], int size) {
    for (int i = 0; i < size; i++) printf(" %d", array[i]);
    printf("\n");
}