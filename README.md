# Sorting Algorithm Performance Visualization Project

This project visualizes and compares the performance of different sorting algorithms using two concurrency techniques: **forking** and **threading**. The comparisons are based on timing data collected over multiple trials, and the results are displayed using interactive Plotly graphs.

## Requirements

- Python 3.x
- pandas
- plotly

Ensure you have the CSV files (`BubbleFork.csv`, `BubbleThread.csv`, etc.) in the same directory as the script.

## Sorting Algorithms Covered

The following algorithms are analyzed:

1. **Bubble Sort**
2. **Comb Sort**
3. **Insertion Sort**
4. **Selection Sort**
5. **Shell Sort**

Each section reads performance data for both fork-based and thread-based implementations and plots them for comparison.

## Visualizations

Each algorithm has its own visualization. The x-axis represents the trial number, while the y-axis represents the execution time in seconds.

### Bubble Sort
df_usgsn03 = pd.read_csv('BubbleFork.csv', sep=',')
df_usgsn04 = pd.read_csv('BubbleThread.csv', sep=',')
# Visualization logic ...

### Comb Sort
df_usgsn03 = pd.read_csv('CombFork.csv', sep=',')
df_usgsn04 = pd.read_csv('CombThread.csv', sep=',')
# Visualization logic ...

### Insertion Sort
df_usgsn03 = pd.read_csv('InsertionFork.csv', sep=',')
df_usgsn04 = pd.read_csv('InsertionThread.csv', sep=',')
# Visualization logic ...

### Selection Sort
df_usgsn03 = pd.read_csv('SelectionFork.csv', sep=',')
df_usgsn04 = pd.read_csv('SelectionThread.csv', sep=',')
# Visualization logic ...

### Shell Sort
df_usgsn03 = pd.read_csv('ShellFork.csv', sep=',')
df_usgsn04 = pd.read_csv('ShellThread.csv', sep=',')
# Visualization logic ...


Output
Each plot contains two lines:

Fork: execution time using process forking

Thread: execution time using multithreading

This allows for a visual comparison of how each method performs under different algorithms and trial runs.


