import Driver_Seq
import Driver_SharedMemory
import math

# NOTE: BE SURE TO DISABLE EACH DRIVER'S SELF EXECUTION BEFORE RUNNING THIS
# NOTE: MPI cannot be run from this file, as it needs cmd line args

# file_names = ["20x20.map", "50x50.map", "100x100.map", "500x20.map", "1000x1000.map"]
file_names = ["20x20.map", "50x50.map", "100x100.map"]


results = ""

for file_name in file_names:
    # results += "\nRunning Seq"
    delta_time_Seq = Driver_Seq.primary_driver_logic(file_name)
    # results += "\nSeq Time: "+ str(delta_time_Seq) + " secs"
    #
    # results += "\nRunning Shared Memory"
    delta_time_SharedMemory = Driver_SharedMemory.primary_driver_logic(file_name)
    # results += "\nShared Memory Time: "+ str(delta_time_SharedMemory) + " secs"

    results +="\n\n\n==========RESULTS for " + file_name +"=========="
    results +="\nSeq Time: "+ str(delta_time_Seq) + " secs"
    results +="\nShared Memory Time: "+ str(delta_time_SharedMemory) + " secs"

    speedup_SharedMemory = math.floor(100 * (delta_time_Seq - delta_time_SharedMemory) / delta_time_Seq)

    results += "\nSpeedup using MPI: " + str(speedup_SharedMemory) + "%"


print()
print()
print()
print(results)