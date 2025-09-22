def priority_preemptive_scheduling():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        pr = int(input("Enter Priority (lower = higher priority): "))
        processes.append([pid, at, bt, pr])

    # Sort initially by Arrival Time
    processes.sort(key=lambda x: x[1])

    remaining_bt = [p[2] for p in processes]
    completion_time = [0] * n
    start_time = [-1] * n
    completed = [False] * n

    current_time = 0
    completed_count = 0

    while completed_count < n:
        # Find all available processes
        ready = []
        for i in range(n):
            arrival_time = processes[i][1]
            if arrival_time <= current_time and not completed[i]:
                ready.append(i)

        if not ready:
            # If no process ready, jump to next arrival
            next_arrival_times = []
            for i in range(n):
                if not completed[i]:
                    next_arrival_times.append(processes[i][1])
            current_time = min(next_arrival_times)
            continue

        # Pick process with highest priority (lowest number)
        idx = min(ready, key=lambda i: processes[i][3])

        # Pick process with highest priority (largest number now)
        # idx = max(ready, key=lambda i: processes[i][3])


        # Mark start time if first time running
        if start_time[idx] == -1:
            start_time[idx] = current_time

        # Run process for 1 unit
        remaining_bt[idx] -= 1
        current_time += 1

        # If process finished
        if remaining_bt[idx] == 0:
            completed[idx] = True
            completion_time[idx] = current_time
            completed_count += 1

    # Build result
    result = []
    total_tat = total_wt = total_rt = 0
    for i in range(n):
        pid, at, bt, pr = processes[i]
        ct = completion_time[i]
        st = start_time[i]
        tat = ct - at
        wt = tat - bt
        rt = st - at

        result.append([pid, at, bt, pr, st, ct, tat, wt, rt])
        total_tat += tat
        total_wt += wt
        total_rt += rt

    # Print
    print("\n--- Preemptive Priority Scheduling Result ---")
    print("PID\tAT\tBT\tPR\tST\tCT\tTAT\tWT\tRT")
    for row in result:
        print("\t".join(str(x) for x in row))

    print("\nAverage TAT = {:.2f}".format(total_tat / n))
    print("Average WT  = {:.2f}".format(total_wt / n))
    print("Average RT  = {:.2f}".format(total_rt / n))

priority_preemptive_scheduling()