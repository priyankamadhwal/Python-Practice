def printTable(table):
     # Find maximum column widths
     colWidth  = [max([len(x) for x in innList]) for innList in table]

     # No. of rows and columns
     nRow, nCol = len(table[0]), len(table)

     # Transpose table
     table = list(zip(*table))

     # Print the table
     for i in range(nRow):
        for j in range(nCol):
             print(table[i][j].rjust(colWidth[j]), end=' ')
        print()
             

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
