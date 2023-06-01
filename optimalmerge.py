import heapq
#input
files=[5,7,3,10,1,5]

print(files)
heap_files=list(files)

#heapify()->converting the iterable into a heap data structure.
heapq.heapify(heap_files)
total_operations=0

#Until it reaches single value

    #heapop()-> removing and returning the smallest data element from the heap.
fileA = heapq.heappop(heap_files)
fileB = heapq.heappop(heap_files)
fileC = fileA + fileB
total_operations = total_operations + fileC    
    #heappush()->inserting the data element specified in its parameters into a heap.
print(heapq.heappush(heap_files,fileC))
    #Generated new heap_files as copied from fileC

#ouput   

print(total_operations)    
    
    
