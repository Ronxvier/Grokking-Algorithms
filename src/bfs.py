class queue:
    def __init__(self, arr):
        self.arr = arr

    def enqueue(self,el):
        self.arr.append(el)
    def dequeue(self):
        return self.arr.pop(0)

    def printlist(self):
        temparr = []
        for el in self.arr:
            temparr.append(el.name)
        return temparr
class node:
    def __init__ (self, name, isTarget):
        self.name = name
        self.isTarget = isTarget
graph = {}
node1 = node("node1",False)
node2 = node("node2",False)
node3 = node("node3",False)
node4 = node("node4",False)
node5 = node("node5",False)
node6 = node("node6",True)
node7 = node("node7",False)
# When you initialize nodes, the nodes their connected to are only the ones further in the graph, not their parents.
graph[node1] = queue([node2,node3])
graph[node2] = queue([node6, node7])
graph[node3] = queue([node5])
graph[node4] = queue([])
graph[node5] = queue([])
graph[node6] = queue([])
graph[node7] = queue([node4])
for key, value in graph.items():
    print(f"""
            key: {key.name}
            value: {value.printlist()}
          """)
def breadth_first_search(root):
    if root.isTarget:
        print(f"Target: {root}")
        return
    search_queue = graph[root].arr
    while search_queue:
        current = search_queue.pop(0)
        if current.isTarget:
            print(f"Target: {current.name}")
            return True
        else:
            search_queue += graph[current].arr
    print("No target found.")
    return False
breadth_first_search(node1)

