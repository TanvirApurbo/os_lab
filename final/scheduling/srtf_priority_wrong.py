def srtf_priority_scheduling():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        pr = int(input("Enter Priority (higher = higher priority): "))
        processes.append([pid, at, bt, pr])

    # Sort initially by Arrival Time
    processes.sort(key=lambda x: x[1])

    # Track info
    remaining_bt = [p[2] for p in processes]  # remaining burst times
    completed = [False] * n
    start_time = [-1] * n
    completion_time = [0] * n

    current_time = 0
    completed_count = 0

    while completed_count < n:
        # Find all available processes
        ready = []
        for i in range(n):
            if processes[i][1] <= current_time and not completed[i]:
                ready.append(i)

        if not ready:
            # If no process ready, jump to next arrival
            next_arrivals = [processes[i][1] for i in range(n) if not completed[i]]
            current_time = min(next_arrivals)
            continue

        # Pick process: highest priority, then shortest remaining BT
        idx = max(ready, key=lambda i: (processes[i][3], -remaining_bt[i]))

        # Mark start time if first run
        if start_time[idx] == -1:
            start_time[idx] = current_time

        # Run process for 1 unit
        remaining_bt[idx] -= 1
        current_time += 1

        # If finished
        if remaining_bt[idx] == 0:
            completed[idx] = True
            completion_time[idx] = current_time
            completed_count += 1

    # Build result table
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

    # Print results
    print("\n--- SRTF + Priority Scheduling Result ---")
    print("PID\tAT\tBT\tPR\tST\tCT\tTAT\tWT\tRT")
    for row in result:
        print("\t".join(str(x) for x in row))

    print("\nAverage TAT = {:.2f}".format(total_tat / n))
    print("Average WT  = {:.2f}".format(total_wt / n))
    print("Average RT  = {:.2f}".format(total_rt / n))


srtf_priority_scheduling()
