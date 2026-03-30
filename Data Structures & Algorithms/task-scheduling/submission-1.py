class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        
        for c in count.values():
            heapq.heappush(maxHeap, -c)
        
        time = 0
        q = deque()

        while q or maxHeap:
            # incement time per execution
            time +=1

            if not maxHeap:
                # skip to the earliest task
                time = q[0][1]
            else:
                # decrement count per execution
                # python does not have max heap so -ive is used so we increment instead of decrementing
                cnt = 1 + heapq.heappop(maxHeap)
                # if count is non zero
                if cnt:
                    q.append([cnt, time + n]) # next available time will be -> current time + idle time
            # if q is not empty and the available time of the earlies task has been met with current time
            if q and q[0][1] == time:
                # cooldown is complete move the task from cooldown to maxHeap for further execution
                heapq.heappush(maxHeap, q.popleft()[0])
        return time




