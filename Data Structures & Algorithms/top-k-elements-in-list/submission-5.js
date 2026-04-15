/**
 * Two aproaches i can try
 * - hashMap + minHeap
 * - hashMap + BucketSort
 */

class minHeap{
    constructor(){
        this.heap = [];
    }

    peek(){
        return this.heap[0];
    }

    size(){
        return this.heap.length;
    }

    push(val){
        this.heap.push(val);
        this.heapifyUp();
    }

    pop(){
        if(this.size() === 1) return this.heap.pop();

        const top = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();

        return top;
    }

    heapifyUp(){
        // get the position of recetly pushed element
        let i = this.heap.length-1;
        while(i > 0){
            // calculate the position of it's parent
            let parent = Math.floor((i-1)/2);
            // check if the minHeap condition isn't already fulfilled
            if (this.heap[parent][0] <= this.heap[i][0]) break;
            // swap the last element with the it's parent to meet the codition
            [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
            
            // change the parent to the swapped element so that the loop can keep going up if it needs to
            i = parent;
        }
        
    }

    heapifyDown(){
        // since the last element is assigned the new top during pop operation
        let i = 0;
        // initiate the loop 
        while(true){
            // get the left and right children position for the current top element 
            const left = 2*i+1;
            const right = 2*i+2;
            // since the parent should be the smallest, take i as the smallest position
            let smallest = i;
            // do and out of bounds check and then compare the parent-child elements
            if(left < this.size() && this.heap[left][0] < this.heap[smallest][0]){
                // update smallest
                smallest = left;
            }
            // do the same with right child
            if(right < this.size() && this.heap[right][0] < this.heap[smallest][0]){
                // update smallest
                smallest = right;
            }
            // break conditon to go out of loop
            if(smallest === i) break;

            // swap current parent with it's smallest child
            [this.heap[smallest], this.heap[i]] = [this.heap[i], this.heap[smallest]];

            // current parent 
            i = smallest;

            
        }
    }

}


class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        for(const num of nums){
            count[num] = (count[num] || 0) +1;
        }

        const heap = new minHeap;
        for(const[num, freq] of Object.entries(count)){
            heap.push([freq, num]);
            if(heap.size() > k){
                heap.pop();
            }
        }

        const res = [];
        for (let i = 0; i < k; i++){
            const [freq, num] = heap.pop();
            res.push(num);
        }
        return res;
    }
}
