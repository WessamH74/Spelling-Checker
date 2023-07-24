# Node class for the Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new value into the Binary Search Tree
    # O(H) where h is the height of the tree
    def insert(self, value): 
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    break

    # Search for a value in the Binary Search Tree and return the node if found
    # O(H) where h is the height of the tree
    def search(self, value): 
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    # Find the predecessor of a given value in the Binary Search Tree
    def find_predecessor(self, value): # O(H)
        current_node = self.root
        predecessor = None

        while current_node:
            if current_node.value < value:
                # Update predecessor and move to the right subtree
                predecessor = current_node
                current_node = current_node.right
            else:
                # Move to the left subtree
                current_node = current_node.left

        return predecessor.value if predecessor is not None else None

    # Find the successor of a given value in the Binary Search Tree
    def find_successor(self, value): # O(H)
        current_node = self.root
        successor = None
        while current_node:
            if current_node.value > value:
                # Update successor and move to the left subtree
                successor = current_node
                current_node = current_node.left
            else:
                # Move to the right subtree
                current_node = current_node.right

        return successor.value if successor is not None else None

    # Balance the Binary Search Tree using sorted values
    # O(N) where n is the number of nodes
    def balance_bst(self , sorted_values):
        self.root = self._construct_balanced_bst(sorted_values, 0, len(sorted_values) - 1)
    
    # function to construct a balanced Binary Search Tree
    # O(N) where n is the number of nodes
    # Space complexity: O(Log2(N)) due to recursive stack
    def _construct_balanced_bst(self, sorted_values, start, end):
        if start > end:
            return None

        # Find the middle element and use it as the root of the current subtree
        mid = (start + end) // 2
        new_node = Node(sorted_values[mid])

        # Recursively construct the left and right subtrees
        new_node.left = self._construct_balanced_bst(sorted_values, start, mid - 1)
        new_node.right = self._construct_balanced_bst(sorted_values, mid + 1, end)

        return new_node


# Example usage:
if __name__ == "__main__":
    # Create an instance of the BinarySearchTree class
    bst = BinarySearchTree()
    
    # Function to remove newlines from an input string
    def remove_newlines(input_string):
        cleaned_string = input_string.replace('\n', '')
        return cleaned_string       

    # Function to check if a word exists in the binary search tree
    def get_word(word): # O(H)
        # Search for the word in the binary search tree
        node = bst.search(word)
        
        if node == None:
            # If the word is not found, find the nearest 4 words to it
            pred = bst.find_predecessor(word)
            pre_pred = bst.find_predecessor(pred)
            succ = bst.find_successor(word)
            post_succ = bst.find_successor(succ)
            
            # Add the word to the dictionary (binary search tree)
            bst.insert(word)
            
            return f"This word does not exist in the dictionary, the word has been added to the dictionary.\
                    \nThe nearest 4 words for this word: {[pre_pred, pred, succ, post_succ]}\n"
        else:
            return f"This word exists in the dictionary: {word}\n"
    
    with open('dictionary.txt', mode='r', encoding='ANSI') as f:
        dictionary = list(f.readlines())
        
        # Remove newlines from each word in the dictionary and store it back in the list
        n = len(dictionary)
        for i in range(0, n):
            dictionary[i] = remove_newlines(dictionary[i])
        
        # Balance the binary search tree using the sorted dictionary
        bst.balance_bst(dictionary) # O(N)
        
        # Clean up variables
        del n, dictionary
    del f

    while True:
        user_input = input('Enter a word to check if it exists in the dictionary or not: ').lower()
        print(get_word(user_input))
        print('To exit the program press CTRL + C')
