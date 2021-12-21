class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
       
        if (mat.length*mat[0].length != r*c) {
            return mat;
        }
        
        int resultCol = 0, resultRow = 0;
        int[][] result = new int[r][c];
        
        for (int row = 0; row < mat.length; row++) {
            for (int col = 0; col < mat[0].length; col++) {
                result[resultRow][resultCol] = mat[row][col];
                resultCol++;
                if (resultCol == c) {
                    resultCol = 0;
                    resultRow++;
                }
            }
        }
        
        return result;
    }
}
