## Abstract
	Arrays and linked lists are both used to store items in memory, Arrays take up contiguous memory while linked lists store entries anywhere in memory.

Linked lists are able to store items anywhere in memory as every item stores the address of the next item in the list. A bunch of random memory addresses linked together.

The issue with linked lists however is that because you are only able to navigate from the beginning to the end of the list, and have no idea where each entry is stored in memory, you can't just jump to a given entry.

This makes linked lists great if you're going to read all the items one at a time, but if you need to jump around, linked lists are terrible.

Arrays are different because you know the address for every item. For example, if your array starts at address 00, and you want the 4th item, you can jump to address 003. This makes arrays great for reading random elements as you can look up any element instantly.

Array: $O(1)$ Reading, $O(n)$ insertion
Linked List: $O(n)$ Reading, $O(1)$ insertion (at tail)

TLDR: Arrays are for random access, and linked lists are for sequential access.
