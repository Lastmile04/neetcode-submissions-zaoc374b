class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const fMap: Map<number, number> = new Map();

        // 1. Build frequency map
        for (const n of nums) {
            fMap.set(n, (fMap.get(n) ?? 0) + 1);
        }

        const heap = new MinHeap();

        // 2. Maintain a heap of size K
        for (const [num, count] of fMap) {
            heap.push([num, count]);
            if (heap.size() > k) {
                heap.pop(); // Remove the least frequent element
            }
        }

        // 3. Extract the remaining k elements from the heap
        const result: number[] = [];
        while (heap.size() > 0) {
            const item = heap.pop();
            if (item) {
                result.push(item[0]); // item[0] is the original number
            }
        }

        return result;
    }
}

// Storing tuples of [number, count]
class MinHeap {
    private heap: [number, number][];

    constructor() {
        this.heap = [];
    }

    size(): number {
        return this.heap.length;
    }

    peek(): [number, number] | undefined {
        return this.heap[0];
    }

    push(val: [number, number]): void {
        this.heap.push(val);
        this.heapifyUp();
    }

    pop(): [number, number] | undefined {
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

            // Compare frequencies (index 1)
            if (this.heap[parentIdx][1] <= this.heap[childIdx][1]) break;

            // Swap
            [this.heap[parentIdx], this.heap[childIdx]] = [this.heap[childIdx], this.heap[parentIdx]];
            childIdx = parentIdx;
        }
    }

    private heapifyDown() {
        let parentIdx = 0;
        while (true) {
            const leftIdx = 2 * parentIdx + 1;
            const rightIdx = 2 * parentIdx + 2;
            let smallest = parentIdx;

            // Compare frequencies (index 1)
            if (
                leftIdx < this.size() &&
                this.heap[leftIdx][1] < this.heap[smallest][1]
            ) {
                smallest = leftIdx;
            }

            if (
                rightIdx < this.size() &&
                this.heap[rightIdx][1] < this.heap[smallest][1]
            ) {
                smallest = rightIdx;
            }

            if (parentIdx === smallest) break;

            // Swap
            [this.heap[parentIdx], this.heap[smallest]] = [this.heap[smallest], this.heap[parentIdx]];
            parentIdx = smallest;
        }
    }
}