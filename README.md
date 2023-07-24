Using this dictionary, implement a spell checker class that takes this dictionary as input, this class has three main operations:

• Store this dictionary in a suitable data structure.

• Take an input word and return the nearest 4 words if this word is not in the dictionary

• Take an input word and add this word to the dictionary

For each operation specify the time and space complexity

Note: The nearest 4 words from a word are the 2 words before and after this word in lexicographic order if they exist.

### Time complexity:
- O(H) for search, insert, and find the nearest words, where H is the height of the binary search tree
- O(N) for balancing the binary search tree and this is used only once, where N is the number of nodes(words)


### Auxiliary space complexity:
- O(N) for storing words in the list
- O(Log2(N)) for balancing binary search Tree due to recursive stack

###  space complexity:
- O(N) for storing the nodes in BST
