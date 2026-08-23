class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first_i=0
        # last_i = len(matrix)-1

        # first_j=0
        # last_j=len(matrix[0])

        # found = False

        # while first_i<=last_i and first_j<=last_j and not found:

        #     mid_i= int((first_i + last_i)/2)
        #     mid_j= int((first_j+ last_j )/2)

        #     print("i",mid_i)
        #     print("j",mid_j)
        #     if target == matrix[mid_i][mid_j]:
        #         found = True
        #         return found
        #     else:
        #         if target>matrix[mid_i][0]:
        #             first_i=mid_i+1
        #         if target<matrix[mid_i][0]:
        #             last_i=mid_i-1
        #         if target>matrix[mid_i][mid_j]:
        #             first_j=mid_j+1
        #         if target<matrix[mid_i][mid_j]:
        #             last_j=mid_j-1
            
        # return found

        rows = len(matrix)
        cols = len(matrix[0])

        # Pretend matrix is one long sorted array
        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            # Convert fake 1D index into row and column
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

        