class Solution {
    findKthLargest(nums: number[], k: number): number {
        const heap = new MinHeap<number>();
        for (const n of nums) {
            heap.push(n);
            if (heap.size() > k) heap.pop();
        }
        return heap.peek()!;
    }
}

class MinHeap<T> {
    private heap: T[];

    constructor() {
        this.heap = [];
    }

    size(): number {
        return this.heap.length;
    }

    peek(): T | undefined {
        return this.heap[0];
    }

    push(val: T): void {
        this.heap.push(val);
        this.heapifyUp();
    }

    pop(): T | undefined {
        if (this.size() === 0) return undefined;
        if (this.size() === 1) return this.heap.pop();
        
        const top = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.heapifyDown();
        return top;
    }

    private heapifyUp() {
        let childIdx = this.heap.length - 1;

        while (childIdx > 0) {
            const parentIdx = Math.floor((childIdx - 1) / 2);

            // Fix 1: Properly access array elements for comparison
            if (this.heap[parentIdx] <= this.heap[childIdx]) break;

            // Fix 2: Swap elements inside the array directly
            [this.heap[parentIdx], this.heap[childIdx]] = [this.heap[childIdx], this.heap[parentIdx]];
            childIdx = parentIdx;
        }
    }

    private heapifyDown() {
        let parentIdx = 0;

        while (true) {
            const leftChildIdx = 2 * parentIdx + 1;
            const rightChildIdx = 2 * parentIdx + 2;
            let smallestIdx = parentIdx;

            // Fix 3: Dynamic evaluation against the running smallest index
            if (
                leftChildIdx < this.size() &&
                this.heap[leftChildIdx] < this.heap[smallestIdx]
            ) {
                smallestIdx = leftChildIdx;
            }

            if (
                rightChildIdx < this.size() &&
                this.heap[rightChildIdx] < this.heap[smallestIdx]
            ) {
                smallestIdx = rightChildIdx;
            }

            if (smallestIdx === parentIdx) break;

            // Fix 4: Real array element swap
            [this.heap[parentIdx], this.heap[smallestIdx]] = [this.heap[smallestIdx], this.heap[parentIdx]];
            parentIdx = smallestIdx;
        }
    }
}