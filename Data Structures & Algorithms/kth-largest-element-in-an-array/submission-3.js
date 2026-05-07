class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        this.heapifyUp();
    }

    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return min;
    }

    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    heapifyUp() {
        let idx = this.heap.length - 1;
        while (idx > 0) {
            const par = Math.floor((idx - 1) / 2);

            if (this.heap[par] <= this.heap[idx]) break;
            this.swap(par, idx);
            idx = par;
        }
    }

    heapifyDown() {
        let idx = 0;

        while (true) {
            const left = 2 * idx + 1;
            const right = 2 * idx + 2;

            let smallest = idx;

            if (left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
            if (idx === smallest) break;

            this.swap(idx, smallest);
            idx = smallest;
        }
    }

    size() {
        return this.heap.length;
    }

    peek() {
        return this.heap[0];
    }
}

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */

    findKthLargest(nums, k) {
        const heap = new MinHeap();
        for (let n = 0; n < nums.length; n++) {
            heap.push(nums[n]);
            if (heap.size() > k) heap.pop();
        }
        return heap.peek();
    }
}