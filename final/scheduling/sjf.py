def sjf_scheduling():
    # Input
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append([pid, at, bt])

    # Sort by Burst Time initially
    processes.sort(key=lambda x: x[2])

    completed = [False] * n
    result = []
    current_time = 0
    completed_count = 0

    while completed_count < n:
        executed = False
        for i in range(n):
            if not completed[i] and processes[i][1] <= current_time:
                pid, at, bt = processes[i]

                st = max(current_time, at)
                ct = st + bt
                tat = ct - at
                wt = tat - bt
                rt = st - at

                result.append([pid, at, bt, st, ct, tat, wt, rt])

                current_time = ct
                completed[i] = True
                completed_count += 1
                executed = True
                break  # restart from beginning
        if not executed:
                # Collect arrival times of incomplete processes
                remaining_arrivals = []
                for j, (pid, at, bt) in enumerate(processes):
                    if not completed[j]:
                        remaining_arrivals.append(at)

                # Jump time to the next arrival
                current_time = min(remaining_arrivals)

    # Print results
    print("\n--- SJF Scheduling (Alt Implementation) ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    total_tat = total_wt = total_rt = 0

    for row in result:
        print("\t".join(str(x) for x in row))
        total_tat += row[5]
        total_wt += row[6]
        total_rt += row[7]

    print("\nAverage TAT = {:.2f}".format(total_tat / n))
    print("Average WT  = {:.2f}".format(total_wt / n))
    print("Average RT  = {:.2f}".format(total_rt / n))

sjf_scheduling()