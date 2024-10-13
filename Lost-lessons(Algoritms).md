# ✌
Here's the C code for Bubble Sort, Selection Sort, and Insertion Sort:

### 1. **Bubble Sort**:
```c
#include <stdio.h>

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}
```

### 2. **Selection Sort**:
```c
#include <stdio.h>

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        // Find the minimum element in unsorted array
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        // Swap the found minimum element with the first element
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selection_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}
```

### 3. **Insertion Sort**:
```c
#include <stdio.h>

void insertion_sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}
```






Algorithm analysis techniques help evaluate the performance, efficiency, and behavior of algorithms. These techniques provide a mathematical framework to measure the time and space complexities of algorithms. 

---

### **1. Worst-Case Analysis**
- **Definition:**  
  This technique evaluates the maximum time or space an algorithm takes across all possible inputs of a given size.
  
- **When to use:**  
  When you want to guarantee that your algorithm will not take more than a certain amount of time or space, regardless of the input.
  
- **Example:**  
  In **Quick Sort**, the worst-case time complexity is O(n²), which happens when the pivot selection is poor (e.g., always picking the smallest or largest element).

---

### **2. Best-Case Analysis**
- **Definition:**  
  This measures the least amount of time or space an algorithm will use for the most favorable input of a given size.
  
- **When to use:**  
  To understand how fast the algorithm could perform in an ideal scenario.
  
- **Example:**  
  In **Insertion Sort**, the best-case time complexity is O(n), which occurs when the array is already sorted.

---

### **3. Average-Case Analysis**
- **Definition:**  
  This evaluates the expected time or space an algorithm takes on average for all possible inputs of a given size, assuming a probabilistic distribution of inputs.
  
- **When to use:**  
  When you want a realistic expectation of the algorithm’s performance under typical conditions.
  
- **Example:**  
  In **Quick Sort**, the average-case time complexity is O(n log n), which assumes random pivot selection leads to balanced partitions most of the time.

---

### **4. Amortized Analysis**
- **Definition:**  
  Amortized analysis evaluates the **average cost** of an operation over a sequence of operations, even if individual operations might be costly.
  
- **When to use:**  
  When analyzing data structures or algorithms where occasional expensive operations are compensated by cheaper ones over time.
  
- **Example:**  
  In a **dynamic array**, appending an element might require occasional resizing, but the overall cost of inserting n elements is O(n), making each insertion amortized O(1).

---

### **5. Asymptotic Analysis**
- **Definition:**  
  This technique analyzes the behavior of algorithms as the input size approaches infinity (n → ∞), focusing on the growth rate of time or space complexity.
  
- **When to use:**  
  To study the scalability of an algorithm. Asymptotic notation (Big O, Big Theta, Big Omega) is used to express this.
  
- **Example:**  
  An algorithm with time complexity O(n²) grows quadratically as the input size increases, meaning its performance degrades much faster compared to O(n log n).

---

### **6. Probabilistic Analysis**
- **Definition:**  
  This analysis involves the use of probability and random variables to analyze algorithms that rely on random input or random choices made during execution.
  
- **When to use:**  
  For randomized algorithms or when the input follows a probabilistic distribution.
  
- **Example:**  
  In **Randomized Quick Sort**, the pivot is selected randomly, and the probabilistic analysis shows that the average-case time complexity is O(n log n).

---

### **7. Online Analysis**
- **Definition:**  
  Online analysis evaluates the performance of algorithms that process input piece by piece, without knowing the entire input in advance.
  
- **When to use:**  
  For problems where data arrives in real-time and decisions must be made without knowledge of future inputs.
  
- **Example:**  
  In **online scheduling algorithms**, jobs arrive over time, and scheduling decisions must be made immediately without seeing future jobs.

---

### **8. Empirical Analysis**
- **Definition:**  
  This technique involves running an algorithm on sample inputs and measuring its performance in practice, rather than just theoretically.
  
- **When to use:**  
  When actual performance and practical considerations (like hardware, system architecture, and dataset characteristics) need to be considered.
  
- **Example:**  
  Testing **sorting algorithms** on real-world datasets (e.g., Tim Sort performs better on real-world data due to its adaptive nature).

---

### **9. Recursive Analysis**
- **Definition:**  
  This technique is used to analyze algorithms that solve problems recursively. The analysis is often done using **recurrence relations** that describe the algorithm’s time complexity.
  
- **When to use:**  
  When analyzing recursive algorithms, especially divide-and-conquer algorithms.
  
- **Example:**  
  The time complexity of **Merge Sort** can be expressed as the recurrence relation T(n) = 2T(n/2) + O(n), which solves to O(n log n).

---

### **10. Space Complexity Analysis**
- **Definition:**  
  This measures the amount of memory an algorithm needs to run, apart from the input data. It evaluates both the stack/heap memory used and temporary storage allocated.
  
- **When to use:**  
  When memory is a constraint or when analyzing algorithms with high memory usage.
  
- **Example:**  
  **Merge Sort** requires O(n) extra space for the auxiliary arrays used during merging, while **Heap Sort** is in-place, requiring only O(1) extra space.

---

### **11. Competitive Analysis**
- **Definition:**  
  This analysis compares the performance of an online algorithm to an optimal offline algorithm that has complete information about the entire input sequence in advance.
  
- **When to use:**  
  In online algorithms, where decisions are made without knowing the future.
  
- **Example:**  
  In the **ski-rental problem**, competitive analysis helps determine when to buy skis rather than renting, comparing the online decision to the optimal offline solution.

---

### **12. Approximation Analysis**
- **Definition:**  
  This is used to analyze the performance of **approximation algorithms** for NP-hard problems, measuring how close the solution is to the optimal one.
  
- **When to use:**  
  When analyzing algorithms that provide near-optimal solutions in polynomial time for problems where exact solutions are computationally expensive.
  
- **Example:**  
  For the **Traveling Salesman Problem (TSP)**, approximation algorithms aim to find a tour whose cost is within a known factor (e.g., 1.5 times) of the optimal tour.

---

### **13. Back-of-the-Envelope Analysis**
- **Definition:**  
  This informal technique involves rough calculations to estimate the time and space complexity of an algorithm without detailed analysis.
  
- **When to use:**  
  In early stages of algorithm design to get a quick idea of performance.
  
- **Example:**  
  Estimating that a sorting algorithm takes about O(n log n) time based on the number of comparisons required without performing a full derivation.

---

### **14. Parameterized Complexity Analysis**
- **Definition:**  
  This analysis focuses on identifying specific parameters of the input (such as the size of a particular subset) that influence the complexity, rather than just the overall input size.
  
- **When to use:**  
  When certain characteristics of the input can dramatically affect the algorithm’s performance.
  
- **Example:**  
  In the **k-clique problem**, the time complexity is parameterized by k, with an algorithm's complexity being exponential in k but polynomial in the overall input size.

---

### **15. Smoothed Analysis**
- **Definition:**  
  This technique combines worst-case and average-case analysis to study how the performance of an algorithm changes when small random noise is added to worst-case inputs.
  
- **When to use:**  
  To understand the practical performance of algorithms that have bad worst-case performance but perform well in practice.
  
- **Example:**  
  In **Simplex Algorithm** for linear programming, the worst-case time complexity is exponential, but smoothed analysis shows that the algorithm performs well on most inputs with small random perturbations.

---

These techniques provide a comprehensive framework for analyzing algorithms in various contexts, ensuring that both theoretical and practical aspects of performance are understood.


Here are *unique and lesser-known terms* related to *algorithms*:

### 1. *Boyer-Moore Algorithm*
   - *Definition*: A string-searching algorithm that skips sections of the text to reduce the number of comparisons. It compares the pattern to the text from right to left.
   - *Application*: Efficient for large text searches, used in text editors and search engines.

### 2. *Karp-Rabin Algorithm*
   - *Definition*: A string-searching algorithm that uses hashing to find any substring of a text in a given pattern.
   - *Application*: Used in searching for patterns in large texts with less computational complexity.

### 3. *Hopcroft-Karp Algorithm*
   - *Definition*: An algorithm used to find the maximum matching in bipartite graphs in O(E√V) time.
   - *Application*: Important in graph theory, used in scheduling and resource allocation problems.

### 4. *Z Algorithm*
   - *Definition*: A linear-time algorithm that computes the Z-array, which describes the longest substring starting from a given index that matches a prefix of the string.
   - *Application*: Used in pattern matching and string searching.

### 5. *Cycle Detection (Floyd’s Tortoise and Hare Algorithm)*
   - *Definition*: A two-pointer algorithm to detect cycles in a sequence, such as a linked list, in constant space.
   - *Application*: Used in graph traversal, memory management, and data structures like linked lists.

### 6. *Strassen's Algorithm*
   - *Definition*: An algorithm for matrix multiplication that improves the standard time complexity from O(n³) to approximately O(n².81).
   - *Application*: Used in scientific computing, graphics, and cryptography where matrix multiplication is required.

### 7. *Quickselect*
   - *Definition*: A selection algorithm to find the k-th smallest (or largest) element in an unordered list. It works similar to QuickSort but only sorts one partition.
   - *Application*: Used in finding medians and quantiles in data sets.

### 8. *Edmonds-Karp Algorithm*
   - *Definition*: An implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network. It uses BFS to find augmenting paths.
   - *Application*: Used in network flow problems, such as traffic, pipelines, and data routing.

### 9. *Tarjan's Algorithm*
   - *Definition*: A depth-first search algorithm that finds all strongly connected components in a directed graph in linear time.
   - *Application*: Used in detecting cycles in graphs and decomposing graphs.

### 10. *Sieve of Atkin*
   - *Definition*: A modern, more efficient algorithm than the Sieve of Eratosthenes for finding all prime numbers up to a specified integer.
   - *Application*: Used in cryptography and prime number calculations.

### 11. *Gabow's Algorithm*
   - *Definition*: An algorithm for finding the strongly connected components of a directed graph.
   - *Application*: Used in network analysis and understanding the structure of graphs.

### 12. *Dinic's Algorithm*
   - *Definition*: A fast algorithm for computing maximum flow in a network. It constructs level graphs and blocks flow across the network iteratively.
   - *Application*: Used in network flow optimization, such as Internet traffic, and bipartite matching.

### 13. *Push-Relabel Algorithm (Goldberg-Tarjan)*
   - *Definition*: A network flow algorithm that maintains a "preflow" and adjusts it to a maximum flow by pushing excess flow from nodes.
   - *Application*: Used in flow networks for solving transportation and optimization problems.

### 14. *Knuth-Morris-Pratt (KMP) Algorithm*
   - *Definition*: A string-searching algorithm that uses a preprocessing table to search for patterns efficiently, avoiding unnecessary comparisons.
   - *Application*: Used in text-editing tools and DNA sequence analysis.

### 15. *Bentley-Ottmann Algorithm*
   - *Definition*: A computational geometry algorithm to find all intersections of line segments in the plane.
   - *Application*: Used in computer graphics and CAD software for line segment intersection problems.

### 16. *Aho-Corasick Algorithm*
   - *Definition*: A string-searching algorithm that matches multiple patterns simultaneously using a finite state machine.
   - *Application*: Used in network intrusion detection systems and text search engines for multiple pattern matching.

### 17. *Suffix Tree Algorithm*
   - *Definition*: An algorithm that constructs a suffix tree from a given string, allowing fast pattern matching, substring search, and many other operations.
   - *Application*: Used in text indexing, string matching, and bioinformatics for DNA sequence analysis.

### 18. *Chandy-Lamport Algorithm*
   - *Definition*: A snapshot algorithm for distributed systems that records a global state without disrupting the ongoing computation.
   - *Application*: Used in distributed computing for detecting deadlocks and analyzing global states.

### 19. *Kosaraju's Algorithm*
   - *Definition*: An algorithm to find the strongly connected components of a directed graph by performing two depth-first searches.
   - *Application*: Used in understanding the structure of complex graphs and detecting cycles.

### 20. *Schönhage-Strassen Algorithm*
   - *Definition*: An algorithm for fast multiplication of large integers, reducing the time complexity from O(n²) to O(n log n log log n).
   - *Application*: Used in cryptography, computational number theory, and arbitrary-precision arithmetic.

### 21. *SPFA Algorithm (Shortest Path Faster Algorithm)*
   - *Definition*: An improvement over the Bellman-Ford algorithm for solving the shortest path problem in a weighted graph.
   - *Application*: Used in routing algorithms and network flow optimizations.

### 22. *Huffman Encoding Algorithm*
   - *Definition*: An algorithm used to compress data by assigning variable-length codes to input characters based on their frequency.
   - *Application*: Used in file compression formats like ZIP, JPEG, and MP3.

### 23. *Dancing Links Algorithm (DLX)*
   - *Definition*: A backtracking algorithm used to solve the exact cover problem, such as in Sudoku solvers. It works by dynamically linking and unlinking nodes in a sparse matrix.
   - *Application*: Used in puzzles, constraint satisfaction problems, and combinatorial optimization.

### 24. *Brent’s Algorithm*
   - *Definition*: An algorithm for finding cycles in iterated function sequences using constant space. It is a refinement of Floyd’s cycle-finding algorithm.
   - *Application*: Used in detecting cycles in algorithms that iterate over sequences, like random number generators.

### 25. *Ford-Fulkerson Algorithm*
   - *Definition*: A greedy algorithm that computes the maximum flow in a flow network by repeatedly finding augmenting paths in the residual graph.
   - *Application*: Used in network optimization, such as traffic routing, telecommunications, and water flow systems.

### 26. *Freivalds' Algorithm*
   - *Definition*: A probabilistic algorithm used to verify the correctness of matrix multiplication in logarithmic time.
   - *Application*: Used in randomized algorithms and complexity theory for verifying matrix operations.

### 27. *Welzl’s Algorithm*
   - *Definition*: An algorithm for finding the smallest enclosing circle (or sphere) for a set of points in linear time.
   - *Application*: Used in computational geometry, computer graphics, and clustering problems.

### 28. *Boruvka’s Algorithm*
   - *Definition*: One of the first algorithms for finding a minimum spanning tree in a graph, working by finding the shortest edge for each component.
   - *Application*: Used in network design, clustering, and constructing road maps.

### 29. *Viterbi Algorithm*
   - *Definition*: A dynamic programming algorithm used to find the most likely sequence of hidden states in a hidden Markov model (HMM).
   - *Application*: Used in speech recognition, bioinformatics, and error correction.

### 30. *Moore's Voting Algorithm*
   - *Definition*: A linear time algorithm used to find the majority element in an array, assuming such an element exists.
   - *Application*: Used in data analytics and online algorithms where real-time decision making is required.

### 31. *Backtracking*
   - *Definition*: A general algorithmic technique that incrementally builds a solution and abandons a solution as soon as it determines the current path cannot lead to a valid solution.
   - *Application*: Used in solving combinatorial problems, puzzles like Sudoku, and constraint satisfaction problems.

### 32. *Simulated Annealing*
   - *Definition*: A probabilistic technique for approximating the global optimum of a given function. It works by allowing moves to worse solutions to escape local minima.
   - *Application*: Used in optimization problems, such as traveling salesman and circuit design.

### 33. *Beam Search*
   - *Definition*: A heuristic search algorithm that explores a graph by expanding the most promising nodes, limiting the number of nodes expanded at each level.
   - *Application*: Used in natural language processing, speech recognition, and machine translation.

### 34. *Floyd-Warshall Algorithm*
   - *Definition*: An all-pairs shortest path algorithm that finds shortest paths between all pairs of vertices in a weighted graph.
   - *Application*: Used in network routing, transitive closure, and finding shortest paths in dense graphs.



### 35. *Arnoldi Iteration*
   - *Definition*: An algorithm used to find a few eigenvalues and eigenvectors of large sparse matrices.
   - *Application*: Used in scientific computing and solving large systems of linear equations.

### Conclusion:
Algorithms cover a wide variety of applications, from sorting and searching to optimization, graph theory, and geometry. Each algorithm is suited to specific types of problems, and understanding their complexities, benefits, and limitations helps in selecting the right approach for different computational challenges.
