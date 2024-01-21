### 디스크 컨트롤러

---

성공 코드

```
from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    num = len(jobs)
    waiting = [] # (소요시간, 요청시점)
    count = [] # 각 작업이 몇초 걸렸는지
    now = 0 #현재 시각

    while len(count) != num : 
        while jobs and now >= jobs[0][0] : 
            top = jobs.pop(0)
            heappush(waiting, (top[1], top[0]))

        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heappush(waiting, (top[1], top[0]))


        x,y = heappop(waiting)
        now += x 
        count.append(now-y)

    return sum(count)//num

```

사용 개념

- 힙 정렬
- heapq 외부 라이브러리 사용
---

실패 코드

```
import heapq


def solution(jobs):
    answer = []
    ing = -1
    queue = []
    time = 0
    jobs.sort()
    cur_job = []
    for i in jobs:
        heapq.heappush(queue, [i[1], i[0]])
    while True:
        if ing == -1 and queue and time >= queue[0][1]:
            ing = 0
            cur_job.append(heapq.heappop(queue))
        time += 1
        if ing != -1:
            ing += 1
        if cur_job:
            if ing == cur_job[0][0]:
                answer.append(time - cur_job[0][1])
                cur_job.pop(0)
                ing = -1
        if not cur_job and not queue:
            break
    print(int(sum(answer)/len(answer)))
    return int(sum(answer)/len(answer))

```

사용 개념

- 시간 복잡도 에러를 해결
- 하지만 원인을 알지 못하겠음
- 일부 테스트 케이스는 통과
- 일부 테으슽 케이스는 불통
- 원인 분석이 힘듦


