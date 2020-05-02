import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private final double mean, stddev, confidenceFactor;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("Value of n and trials should be greater than 0");
        }
        double[] percolationThresholds = new double[trials];
        for (int i = 0; i < trials; i++) {
            Percolation percolation = new Percolation(n);
            int x;
            for (x = 0; !percolation.percolates(); x++) {
                int row, col;
                do {
                    row = 1 + StdRandom.uniform(n);
                    col = 1 + StdRandom.uniform(n);
                } while (percolation.isOpen(row, col));
                percolation.open(row, col);
            }
            percolationThresholds[i] = (double)x / (double)(n * n);
        }
        mean = StdStats.mean(percolationThresholds);
        stddev = StdStats.stddev(percolationThresholds);
        confidenceFactor = (1.96 * stddev)/Math.sqrt(trials);
    }

    // sample mean of percolation threshold
    public double mean() {
        return mean;
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return stddev;
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean - confidenceFactor;
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean + confidenceFactor;
    }

    // test client (see below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trails = Integer.parseInt(args[1]);
        PercolationStats percolationStats = new PercolationStats(n, trails);
        System.out.println("mean                    = " + percolationStats.mean());
        System.out.println("stddev                  = " + percolationStats.stddev());
        System.out.println("95% confidence interval = [" + percolationStats.confidenceLo() + ", " + percolationStats.confidenceHi() + "]");
    }

}