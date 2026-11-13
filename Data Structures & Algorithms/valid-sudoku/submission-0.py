from collections import defaultdict


class Solution:


    def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] ==  ".":
                    continue

                element = board[row][col]
                if element in rows[row]:
                    return False
                if element in cols[col]:
                    return False
                if element in squares[(row//3, col//3)]:
                    return False
                
                rows[row].add(element)
                cols[col].add(element)
                squares[(row//3, col//3)].add(element)
        
        return True
