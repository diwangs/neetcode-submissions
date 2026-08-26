class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        taskQueue = [(-v, k) for (k, v) in count.items()]
        heapq.heapify(taskQueue)
        cooldownQueue = []

        count = 0
        while len(taskQueue) > 0 or len(cooldownQueue) > 0:
            if len(taskQueue) > 0:
                executedTask = heapq.heappop(taskQueue)
                
                if executedTask[0] < -1:
                    heapq.heappush(cooldownQueue, (n, executedTask[0] + 1, executedTask[1]))

            while len(cooldownQueue) > 0 and cooldownQueue[0][0] == 0:
                _, a, b = heapq.heappop(cooldownQueue)
                heapq.heappush(taskQueue, (a, b))

            cooldownQueue = [(n - 1, a, b) for (n, a, b) in cooldownQueue]
            
            count += 1

        return count
