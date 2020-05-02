import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private boolean[][] grid;
    private final WeightedQuickUnionUF ufObject;
    private final int virtualTop, virtualBottom, gridSize;
    private int openCount;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("N should be greater than 0");
        }
        grid = new boolean[n][n];
        gridSize = n;
        ufObject = new WeightedQuickUnionUF(n * n + 2);
        virtualTop = 0;
        virtualBottom = n * n + 1;
        openCount = 0;
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (!isOpen(row, col)) {
            grid[row - 1][col - 1] = true;
            openCount++;
            int index = getIndex(row, col);
            if (row == 1) {
                ufObject.union(virtualTop, index);
            } else if (row == gridSize) {
                ufObject.union(virtualBottom, index);
            }
            if (isOpen(row - 1, col)) {
                ufObject.union(index, getIndex(row - 1, col));
            }
            if (isOpen(row + 1, col)) {
                ufObject.union(index, getIndex(row + 1, col));
            }
            if (isOpen(row, col - 1)) {
                ufObject.union(index, getIndex(row, col - 1));
            }
            if (isOpen(row, col + 1)) {
                ufObject.union(index, getIndex(row, col + 1));
            }
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (isValidIndex(row, col)) {
            return grid[row - 1][col - 1];
        } else {
            return false;
        }
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        return isOpen(row, col) && ufObject.connected(virtualTop, getIndex(row, col));
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openCount;
    }

    // does the system percolate?
    public boolean percolates() {
        return ufObject.connected(virtualTop,  virtualBottom);
    }

    private boolean isValidIndex(int row, int col) {
        return row >= 1 && row <= gridSize && col >= 1 && col <= gridSize;
    }

    private int getIndex(int row, int col) {
        return (row - 1) * gridSize + col;
    }
}