class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxPQ = new MaxPriorityQueue();

        for(const stone of stones){
            maxPQ.enqueue(stone);
        }

        while(maxPQ.size() > 1){
           const x = maxPQ.dequeue();
            const y = maxPQ.dequeue();

        if (x !== y) maxPQ.enqueue(x-y);

        }

        return maxPQ.size() === 1? maxPQ.dequeue() : 0;
    }
}
