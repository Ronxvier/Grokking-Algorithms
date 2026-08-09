## Abstract
Big O notation measures the amount of time that an algorithm takes to run with respect to how many entries it operates over.
## Common Big O Run Times
* **O(log n)**, also known as *log time*. Ex: Binary Search
* **O(n)**, also known as *linear time*. Ex: Simple Search
* **O(n * log n))** Ex: Fast sorting algorithm, like quick sort
* **O($n^2$)** Ex: Slow sorting algorithm, like selection sort
* **O(n!)** Ex: Very slow sorting algorithm![[Screenshot 2026-08-08 at 12.14.20 AM.png]]

**Note:** Algorithm speed isn't measured in seconds, but in growth of the number of operations. (*How quickly the run time of an algorithm increases as size increases.*)
## Traveling Salesperson Problem
Let's say there's 5 cities on the map, and a salesperson wants to travel the minimum distance while hitting up all 5 of them. In order to calculate all of the paths through the 5 cities in order to determine the one of least distance, the salesperson must perform 120 (5!) operations. This increases as the number of cities increases, and is an example of factorial time.