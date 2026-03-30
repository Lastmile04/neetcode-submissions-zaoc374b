class Solution {
    lastStoneWeight(stones) {
        const pq = new MaxPriorityQueue();

        for (const s of stones) pq.enqueue(s);

        while (pq.size() > 1) {
            const x = pq.dequeue();
            const y = pq.dequeue();

            if (x !== y) pq.enqueue(x - y);
        }

        return pq.size() ? pq.dequeue() : 0;
    }
}