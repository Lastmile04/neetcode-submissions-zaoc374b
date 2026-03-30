class minHeap{
    constructor(){
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        let index = this.heap.length - 1;

        while (index > 0) {
            let parentIdx = Math.floor((index - 1) / 2);

            if (this.heap[parentIdx] <= this.heap[index]) break;

            // swap in array
            [this.heap[parentIdx], this.heap[index]] =
            [this.heap[index], this.heap[parentIdx]];

            index = parentIdx;
        }
    }

    pop(){
        // remove root + heapify down
        if (this.heap.length === 1) return this.heap.pop();

        let root = this.heap[0];
        this.heap[0] = this.heap.pop();
        let index = 0;

        while (true) {
            let left = 2 * index + 1;
            let right = 2 * index + 2;

            let smallest = index;

            // ❓ compare with left
            if(left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
            // ❓ compare with right
            if( right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === index) break;

            // ❓ swap
            [this.heap[index], this.heap[smallest]] =
            [this.heap[smallest], this.heap[index]];

            index = smallest;
        }

        return root;
    } 

    peek(){
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
        // iterate through nums
        // push into heap
        // if size is greater than k -> pop
        // peek for solution
        let heap = new minHeap();
        for(let i = 0; i<nums.length; i++){
            heap.push(nums[i]);
            if(heap.heap.length > k) heap.pop();
        }
        return heap.peek()
    }
}
