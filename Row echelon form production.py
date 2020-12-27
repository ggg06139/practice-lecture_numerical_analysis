mat =       [[0, 4, 5, 6, 7],                                         #편하게 보기 위하여 값을 임의로 지정하여 넣어두었습니다.
             [0, 0, 0, 2, 2],
             [1, 2, 3, 4, 5],
             [0, 0, 0, 4, 7],
             [0, 0, 0, 8, 8]]

  
def row_reduce(mat):
      ref = []                                                         #rref는 기약행사다리꼴을 의미하는 것이니 ref로 이름을 변경하는 디버깅 실시합니다.
      M_e = []
      row_idx = list(range(len(mat)))
      col_idx = len(mat[0])
      
      M = [[0 for c in range(len(mat))] for r in range(len(mat))]      #mat와 같은 형식의 5X5 행렬에서 전부 값이 0으로 만들어집니다.
      for i in range(len(M)):
          M[i][i] = 1                                                  #M[0][0] 과 같이 대각선의 성분은 1로 바뀌어 단위행렬이 됩니다.
          
      for c in range(col_idx):
          rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]   #행렬 index기준 같은 열에 0이 아닌 행의 번호들을 빠른 열부터 리스트에 저장한다. 
          if rows_with_nonzero:                                        #만약 값이 저장된다면 if문 수행
              pivot = rows_with_nonzero[0]                             #가장 처음 저장된 리스트의 수를 pivot에 저장
              row_idx.remove(pivot)                                    #pivot에 저장된 수와 맞는  row_idx의 동일한 수의 행을 지운다
              ref.append(mat[pivot])                                   #pivot에 저장된 수와 맞는 mat의 동일한 수의 행을 ref의 행으로 저장
              M_e.append(M[pivot])                                     #pivot에 저장된 수와 맞는 M의 동일한 수의 행을 M_e의 행으로 저장
              for r in rows_with_nonzero[1:]:                          #만약 rows_with_nonzero의 값 중 두 번째 값이 존재할 경우 아래 문장들을 수행합니다.
                  if r is not pivot:                                   #r이 pivot이 아니라면 아래의 산수 계산을 시행
                      multiplier = mat[r][c] / mat[pivot][c]           
                      mat[r] = [a - multiplier*b for a, b in zip(mat[r], mat[pivot])]
                      M[r] = [a - multiplier*b for a, b in zip(M[r], M[pivot])]
                      
      for r in row_idx:                                                #row_idx의 행의 항목수 만큼 반복한다.
          ref.append(mat[r])
          M_e.append(M[r])
          
      return ref, M_e

ref, M_e = row_reduce(mat)






for i in range(len(ref)):                                               #출력 시 편하게 보기 위하여 줄바꿈 시행하였습니다.
    print(ref[i])   

print('\n')

for i in range(len(M_e)):
    print(M_e[i])

