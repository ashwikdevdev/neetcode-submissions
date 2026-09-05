class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        out: int = 1
        for i in range(len(board)):
            out = out*int(self.validrow(board[i]))
            print(out)
        
        rowList = self.makeRows(board)
        for i in range(len(rowList)-1):
            out = out*int(self.validrow(rowList[i]))

        return bool(out)

    def validrow(self, row: List[str]) -> bool:
        uniquedigits = set()
        count = 0
        for i in row:
            if i != '.':
                uniquedigits.add(i)  
                count += 1
            else:
                continue
        return len(uniquedigits) == count
    
    def makeRows (self, board: List[List[str]]) -> List[List[str]]:
        rowList=[[]]
        for i in range(len(board[0])):  
            row = []
            for j in range(len(board)):  
                row.append(board[j][i])  
            rowList.append(row)

        for r in range(0,9,3):
            for c in range(0,9,3):
                row = []
                for i in range(3):
                    for j in range(3):
                        row.append(board[r+i][c+j])
                rowList.append(row)
        return rowList
