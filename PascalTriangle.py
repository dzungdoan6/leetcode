from typing import List
def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]

    results = [[1], [1,1]]
    
    for i in range(2, numRows):
        curr_row = results[i-1]
        new_row = list()
        for k in range(len(curr_row)+1):
            if k == 0 or k == len(curr_row):
                new_row.append(1)
            else:
                new_row.append(curr_row[k-1] + curr_row[k])
        results.append(new_row)
    return results

numRows = 5
print(generate(numRows))

numRows = 1
print(generate(numRows))