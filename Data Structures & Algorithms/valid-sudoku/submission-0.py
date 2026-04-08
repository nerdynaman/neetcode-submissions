class Solution:
    def getBoxIndex(self, rowNum: int, colNum: int) -> int:
        return ((rowNum//3)*3) + (colNum//3)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashSetArr = [set() for i in range(9)]
        columnHashSetArr = [set() for i in range(9)]
        boxHashSetArr = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowHashSetArr[row]:
                    return False
                else:
                    rowHashSetArr[row].add(board[row][col])
                if board[row][col] in columnHashSetArr[col]:
                    return False
                else:
                    columnHashSetArr[col].add(board[row][col])

                if board[row][col] in boxHashSetArr[self.getBoxIndex(row,col)]:
                    return False
                else:
                    boxHashSetArr[self.getBoxIndex(row,col)].add(board[row][col])
        return True

