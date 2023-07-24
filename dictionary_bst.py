import re
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

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


            
    def find_predecessor(self, value): #O(LOGN)
        # Start traversal from the root
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

    def find_successor(self, value): #O(LOGN)
        # Start traversal from the root
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

    def balance_bst(self , sorted_values):
        self.root = self._construct_balanced_bst(sorted_values, 0, len(sorted_values) - 1)
    
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
    
    bst = BinarySearchTree()
   
    def remove_newlines(input_string):
       cleaned_string = input_string.replace('\n', '')
       return cleaned_string
    
    
    def add_word(word): #O(LOGN)
        bst.insert(word)
     
    def get_word(word): #O(LOGN)
        node = bst.search(word) 
        if node == None:
            pred = bst.find_predecessor(word)
            pre_pred = bst.find_predecessor(pred)
            succ = bst.find_successor(word)
            post_succ = bst.find_successor(succ)
            return [pre_pred,pred,succ,post_succ]
        else:
            return word
    
    with open('dictionary.txt', mode='r' ,encoding='ANSI') as f:
        dictionary = list(f.readlines())
        n = len(dictionary)
        for i in range (0 , n):
            dictionary[i] = remove_newlines(dictionary[i])
        dictionary.sort()
        bst.balance_bst(dictionary)
        del n,dictionary
    del f
    print(get_word("ƒpoque"))
    print(get_word("wide"))
    print(get_word('bot'))
    print(get_word("wessam"))
    add_word("wessam")
    print(get_word("wessam"))

