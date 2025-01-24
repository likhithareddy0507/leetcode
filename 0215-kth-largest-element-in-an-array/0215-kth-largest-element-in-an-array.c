#include <stdlib.h>

// Helper function to swap two integers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to heapify a min-heap
void heapify(int heap[], int size, int i) {
    int smallest = i;       // Initialize the root as the smallest
    int left = 2 * i + 1;   // Left child index
    int right = 2 * i + 2;  // Right child index

    // Check if left child exists and is smaller
    if (left < size && heap[left] < heap[smallest]) {
        smallest = left;
    }

    // Check if right child exists and is smaller
    if (right < size && heap[right] < heap[smallest]) {
        smallest = right;
    }

    // If the smallest is not the root, swap and recursively heapify
    if (smallest != i) {
        swap(&heap[i], &heap[smallest]);
        heapify(heap, size, smallest);
    }
}

// Function to find the kth largest element using a min-heap
int findKthLargest(int* nums, int numsSize, int k) {
    // Create a min-heap with the first k elements
    int* heap = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; i++) {
        heap[i] = nums[i];
    }

    // Build the initial min-heap
    for (int i = k / 2 - 1; i >= 0; i--) {
        heapify(heap, k, i);
    }

    // Process the remaining elements in the array
    for (int i = k; i < numsSize; i++) {
        if (nums[i] > heap[0]) {  // If the current element is larger than the heap's root
            heap[0] = nums[i];    // Replace the root
            heapify(heap, k, 0);  // Restore the heap property
        }
    }

    // The root of the heap is the kth largest element
    int result = heap[0];
    free(heap);  // Free allocated memory
    return result;
}