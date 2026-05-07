import platform

def traverse_sim(head_index,storage):
    output = []
    index = head_index
    while index is not None:
        val,index = storage[index]
        output.append(val)
    return output

storage = (1,('A',1),('B',2),('C',None))
result = traverse_sim(1,storage)
print(result)

