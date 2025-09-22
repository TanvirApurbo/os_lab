def fcfs_scheduling():
    n = int(input("Enter number of processes: "))

    processes = []
    for i in range(n):
        pid = input(f"\nEnter Process ID for P{i+1}: ")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append([pid, at, bt])

    # Sort processes by Arrival Time (AT)
    processes.sort(key=lambda x: x[1])

    # To store result: PID, AT, BT, ST, CT, TAT, WT, RT
    result = []
    current_time = 0

    for i in range(n):
        pid, at, bt = processes[i]

        # Start Time (ST): max of current time or arrival time
        st = max(current_time, at)
      
        ct = st + bt
       
        tat = ct - at
       
        wt = tat - bt
     
        rt = st - at

        # Update current time
        current_time = ct

        result.append([pid, at, bt, st, ct, tat, wt, rt])

   
    print("\n--- FCFS Scheduling Result ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    total_tat = total_wt = total_rt = 0

    for row in result:
        print("\t".join(str(x) for x in row))
        total_tat += row[5]
        total_wt += row[6]
        total_rt += row[7]

   
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n

    print("\nAverage TAT = {:.2f}".format(avg_tat))
    print("Average WT  = {:.2f}".format(avg_wt))
    print("Average RT  = {:.2f}".format(avg_rt))

fcfs_scheduling()
