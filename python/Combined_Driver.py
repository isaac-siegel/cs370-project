import Driver_Seq
import Driver_SharedMemory

# NOTE: BE SURE TO DISABLE EACH DRIVER'S SELF EXECUTION BEFORE RUNNING THIS
# NOTE: MPI cannot be run from this file, as it needs cmd line args

print("Running Seq")
delta_time_Seq = Driver_Seq.primary_driver_logic()
print("Seq Time: "+ str(delta_time_Seq) + " secs")

print("Running Shared Memory")
delta_time_SharedMemory = Driver_SharedMemory.primary_driver_logic()
print("Shared Memory Time: "+ str(delta_time_SharedMemory) + " secs")


print("\n\n\n==========RESULTS==========")
print("Seq Time: "+ str(delta_time_Seq) + " secs")
print("Shared Memory Time: "+ str(delta_time_SharedMemory) + " secs")

speedup_SharedMemory = (delta_time_Seq - delta_time_SharedMemory) / delta_time_Seq

print("Speedup using MPI: " + str(speedup_SharedMemory) + "%" )


