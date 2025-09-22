from collections import deque

def round_robin_scheduling():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append([pid, at, bt])

    tq = int(input("\nEnter Time Quantum: "))

    # Sort by arrival time initially
    processes.sort(key=lambda x: x[1])

    # Tracking arrays
    remaining_bt = [p[2] for p in processes]
    completion_time = [0] * n
    start_time = [-1] * n
    completed = [False] * n

    ready_queue = deque()
    current_time = 0
    completed_count = 0

    # Push first process(es) to queue
    ready_queue.append(0)
    visited = [False] * n
    visited[0] = True

    while completed_count < n:
        if not ready_queue:
            # No process ready → jump to next arrival
            for i in range(n):
                if not completed[i]:
                    current_time = processes[i][1]
                    ready_queue.append(i)
                    visited[i] = True
                    break

        idx = ready_queue.popleft()
        pid, at, bt = processes[idx]

        if start_time[idx] == -1:
            start_time[idx] = max(current_time, at)

        # Run process for min(TQ, remaining BT)
        run_time = min(tq, remaining_bt[idx])
        current_time = max(current_time, at) + run_time
        remaining_bt[idx] -= run_time

        # Add new arrivals to queue
        for i in range(n):
            if (not visited[i]) and (processes[i][1] <= current_time) and (not completed[i]):
                ready_queue.append(i)
                visited[i] = True

        # If process finished
        if remaining_bt[idx] == 0:
            completed[idx] = True
            completion_time[idx] = current_time
            completed_count += 1
        else:
            # Put it back into queue
            ready_queue.append(idx)

    # Build results
    result = []
    total_tat = total_wt = total_rt = 0
    for i in range(n):
        pid, at, bt = processes[i]
        ct = completion_time[i]
        st = start_time[i]
        tat = ct - at
        wt = tat - bt
        rt = st - at

        result.append([pid, at, bt, st, ct, tat, wt, rt])
        total_tat += tat
        total_wt += wt
        total_rt += rt

    # Print table
    print("\n--- Round Robin Scheduling Result ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    for row in result:
        print("\t".join(str(x) for x in row))

    print("\nAverage TAT = {:.2f}".format(total_tat / n))
    print("Average WT  = {:.2f}".format(total_wt / n))
    print("Average RT  = {:.2f}".format(total_rt / n))


round_robin_scheduling()