	Basically it's when a function calls itself over and over to solve a problem.

Every recursive function has two parts: the *base case*, and the *recursive case*. The recursive case is when the function calls itself, the base case is when the function doesn't call itself again, so it doesn't go into an infinite loop.


## The stack
Stacks are a data structure that function as an array or list in which you can **push** an item to the top, and **pop** an item (remove the topmost item and read it). This is a LIFO system (last in first out.)

Your computer uses a stack internally called the call stack. This means if you call a function within another function it gets pushed to the stack, executed, then the program returns to the stack to retrieve the next item.

## In Practice
Recursion, especially in Python, has a lot of overhead. Even though in theory it should have the same time complexity as looping over an array, in practice this is rarely the case. I learned this in **Leetcode 56: Merge Intervals**