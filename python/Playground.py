from mpi4py import MPI
from Point import Point
from TerrainMap import TerrainMap
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


# if rank == 0:
#     data = [Point(rank, 42) for i in range(size*2)]
# else:
#     data = None

# data = comm.scatter(data, root=0)

# if rank == 0:
#     pass
# else:
#     for point in data:
#         print(point)
terrain_map = TerrainMap("test.map")



terrain_map = comm.bcast(terrain_map, root=0)

print(terrain_map)
# data = [Point(rank, 42) for i in range(size*2)]


# collected = comm.gather(data, root=0)
#
# if rank == 0:
#     collected = [item for sublist in collected for item in sublist]
#     print(len(collected))
#     for point in collected:
    #     print(len(point))
