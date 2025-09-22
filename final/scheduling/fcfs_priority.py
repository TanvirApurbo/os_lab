def findAvgTimeFCFS_Priority(n, at, bt, prio):
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    completed = [0] * n
    time = 0
    completedCount = 0
    total_wt = 0
    total_tat = 0

    print("\n--- FCFS + Priority ---")
    print("Processes\tAT\tBT\tPR\tWT\tTAT\tCT")

    while completedCount < n:
        idx = -1
        maxPriority = -1
        earliestAT = float('inf')

        # pick highest priority; tie-breaker = earliest arrival
        for i in range(n):
            if not completed[i] and at[i] <= time:
                if (prio[i] > maxPriority) or (prio[i] == maxPriority and at[i] < earliestAT):
                    maxPriority = prio[i]
                    earliestAT = at[i]
                    idx = i

        if idx != -1:
            time = max(time, at[idx])  # if CPU was idle
            ct[idx] = time + bt[idx]
            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]
            time = ct[idx]

            completed[idx] = 1
            completedCount += 1

            total_wt += wt[idx]
            total_tat += tat[idx]

            print(f"P{idx+1}\t\t{at[idx]}\t{bt[idx]}\t{prio[idx]}\t{wt[idx]}\t{tat[idx]}\t{ct[idx]}")
        else:
            time += 1

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")


def main():
    n = int(input("Enter number of processes: "))

    at, bt, prio = [], [], []

    for i in range(n):
        print(f"\nProcess {i+1}")
        at.append(int(input("Arrival Time: ")))
        bt.append(int(input("Burst Time: ")))
        prio.append(int(input("Priority (higher number = higher priority): ")))

    findAvgTimeFCFS_Priority(n, at, bt, prio)


if __name__ == "__main__":
    main()
