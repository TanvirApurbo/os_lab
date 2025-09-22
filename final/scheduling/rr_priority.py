from collections import deque

def round_robin_group(processes, tq, start_time):
    """
    Run Round Robin on a group of processes (all same priority).
    processes = [[pid, at, bt]]
    Returns result list and the final time after finishing the group.
    """
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # sort by arrival time

    remaining_bt = [p[2] for p in processes]
    completion_time = [0] * n
    start_times = [-1] * n
    completed = [False] * n
    ready_queue = deque()
    visited = [False] * n

    current_time = start_time
    completed_count = 0

    # Add first ready process
    for i in range(n):
        if processes[i][1] <= current_time:
            ready_queue.append(i)
            visited[i] = True
            break

    while completed_count < n:
        if not ready_queue:
            # If no process ready, jump to next arrival
            for i in range(n):
                if not completed[i]:
                    current_time = processes[i][1]
                    ready_queue.append(i)
                    visited[i] = True
                    break

        idx = ready_queue.popleft()
        pid, at, bt = processes[idx]

        if start_times[idx] == -1:
            start_times[idx] = max(current_time, at)

        run_time = min(tq, remaining_bt[idx])
        current_time = max(current_time, at) + run_time
        remaining_bt[idx] -= run_time

        # Add new arrivals
        for i in range(n):
            if (not visited[i]) and (processes[i][1] <= current_time) and (not completed[i]):
                ready_queue.append(i)
                visited[i] = True

        if remaining_bt[idx] == 0:
            completed[idx] = True
            completion_time[idx] = current_time
            completed_count += 1
        else:
            ready_queue.append(idx)

    # Build results
    results = []
    for i in range(n):
        pid, at, bt = processes[i]
        st = start_times[i]
        ct = completion_time[i]
        tat = ct - at
        wt = tat - bt
        rt = st - at
        results.append([pid, at, bt, st, ct, tat, wt, rt])

    return results, current_time


def priority_round_robin():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        pr = int(input("Enter Priority (lower = higher priority): "))
        processes.append([pid, at, bt, pr])

    tq = int(input("\nEnter Time Quantum: "))

    # Group by priority
    priority_groups = {}
    for p in processes:
        pid, at, bt, pr = p
        if pr not in priority_groups:
            priority_groups[pr] = []
        priority_groups[pr].append([pid, at, bt])

    # Sort groups by priority (lower number = higher priority)
    sorted_priorities = sorted(priority_groups.keys())

    current_time = 0
    final_results = []

    for pr in sorted_priorities:
        group = priority_groups[pr]
        results, current_time = round_robin_group(group, tq, current_time)
        # Add priority info back to result
        for row in results:
            final_results.append([row[0], row[1], row[2], pr] + row[3:])

    # Print result table
    print("\n--- Priority + Round Robin Scheduling Result ---")
    print("PID\tAT\tBT\tPR\tST\tCT\tTAT\tWT\tRT")

    total_tat = total_wt = total_rt = 0
    for row in final_results:
        print("\t".join(str(x) for x in row))
        total_tat += row[6]
        total_wt += row[7]
        total_rt += row[8]

    print("\nAverage TAT = {:.2f}".format(total_tat / n))
    print("Average WT  = {:.2f}".format(total_wt / n))
    print("Average RT  = {:.2f}".format(total_rt / n))


priority_round_robin()