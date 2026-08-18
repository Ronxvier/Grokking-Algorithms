# Graphs
A graph models a set of connections. Like a map, or a chain of who owes who money. Nodes are the units in the list, and edges are the connections between them. Graphs are a good way to model how different things are connected to one another.

# Breadth-first search
Breadth-first search is a search algorithm for graphs, and helps answer two types of questions:

**Type 1:** Is there a path from node A to node B?
**Type 2:** What's the shortest path from node A to node B?
## Mango Example
Imagine you want mangos, and you look for a mango seller on social media. You look through each of your friends, check if they're a mango seller, if not you'll go one layer out and look for your friends friends, checking if they're a mango seller, you'll repeat this process until you find a seller.

In this case, your friends are first-degree connections, and your friends friends are second-degree connections. You'd prefer a first degree connection rather than a second degree connection.

In this example, you'd search first degree connections before second degree connections. You'd add all the first degree connections to a queue, then second degree connections, then search them as you process them through the queue. Queues are a first in first out data structure (FIFO.)
## Implementing graphs
Let's refer back to the mango example. Graphs can be represented as a Hashmap, with the key being a given person (*string*), and the value being an *array* of the people you know (who may also be in the Hashmap, with their own array of people they know.)

Detaching from the mango example, a graph is a Hashmap of nodes, with its corresponding key being the nodes it's connected to.