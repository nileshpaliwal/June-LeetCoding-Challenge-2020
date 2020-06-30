#Given a 2D board and a list of words from the dictionary, find all words in the board.
#
#Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# 
#
#Example:
#
#Input: 
#board = [
#  ['o','a','a','n'],
#  ['e','t','a','e'],
#  ['i','h','k','r'],
#  ['i','f','l','v']
#]
#words = ["oath","pea","eat","rain"]
#
#Output: ["eat","oath"]
# 
#
#Note:
#
#All inputs are consist of lowercase letters a-z.
#The values of words are distinct.

class Node:
    def __init__(self):
        self.children = {}  # map letter to child node
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = Node()
        for word in words:      # build a trie
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = word    # node is end of complete word

        found = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(board, root, r, c, found)
        return found

    def search(self, board, node, r, c, found):     # depth first search of board

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return

        letter = board[r][c]
        if letter not in node.children:
            return

        node = node.children[letter]
        if node.word:
            found.append(node.word)
            node.word = None    # avoid duplication of results

        board[r][c] = '*'       # temporarily flag this cell as being used
        self.search(board, node, r+1, c, found)
        self.search(board, node, r-1, c, found)
        self.search(board, node, r, c+1, found)
        self.search(board, node, r, c-1, found)
        board[r][c] = letter    # replace cell contents