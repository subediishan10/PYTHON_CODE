import heapq
#
#input
files=[2,3,4,5,6,7]


print(files)
heap_files=list(files)

#heapify():
# This function converts a regular list to a heap. 
# In the resulting heap the smallest element gets pushed to the index position 0. 
# But rest of the data elements are not necessarily sorted.
  
heapq.heapify(heap_files)
total_operations=0

#Until it reaches single value
while(len(heap_files)>1):
    #heapop()-> This function returns the smallest data element from the heap.
    fileA = heapq.heappop(heap_files)
    fileB = heapq.heappop(heap_files)
    fileC = fileA + fileB
    total_operations = total_operations + fileC
    #heappush()->This function adds an element to the heap without altering the current heap.
    heapq.heappush(heap_files,fileC)
    #Generated new heap_files as copied from fileC
    print(heap_files)

#ouput   

print(total_operations)    

    
    
