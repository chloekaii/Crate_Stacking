# Crate Stacking
Solving the Towers of Hanoi problem recursively.

## Algorithm Design:
The crate stacking algorithm has the following steps:
- Base Case:
  - If n == 1, move the crate from A to C. Write the output to output.txt.
- Recursive Case:
  - Move the top n-1 crates from A to B, using C as a ‘helper’ tower so that heavier crates are never moved on top of lighter crates. Write the output to output.txt.
  - Move the largest crate n from the A to C. Write the output to output.txt.
  - Move the n-1 crates from B to C, using A as a ‘helper’ tower so that heavier crates are never moved on top of lighter crates. Write the output to output.txt.
  This follows the constraints of the problem, because it ensures that only one crate is moved at a time and only lighter crates are placed on top of heavier crates.

## Data Structures/Variables Used:
- n (integer): Represents the number of crates that need to be moved from one tower to another. This variable determines the size of the problem being solved (e.g., how many crates to move). With each recursive call, n decreases by 1 until it reaches 1, which is the base case.
- A, B, C (strings): These variables represent the labels of the racks involved in the crate-moving process. A is the source tower. B is the helper tower. C is the destination tower.
- file (file object): This is a file object that points to an open file. The file object is used to write the crate-moving steps to the file.
## Time Complexity Analysis:
The recurrence equation of the algorithm is T(n)= T(n-1) + T(n-1) + 1, which simplifies to 2T(n−1)+1. We know this because first you make 2 recursive calls within the initial call to the function. These recursive calls will continue to be called until we reach the base case, where n == 1. Therefore, there will be a total of 2^n recursive calls made. This means that the Big-O notation is O(2^n).
If we want to solve this mathematically, here are the steps:
- T(n) = 2T(n - 1) + 1
- T(n) = 2(2T(n − 2) + 1 + 1
- T(n) = 4T(n − 2) + 2 + 1
- T(n) = 8T(n − 3) + 4 + 2 + 1
- From here, we can see that there is a pattern emerging:
- T(n) = 2^kT(n - k) + c
- Then, if we set k = n - 1 (since on the nth iteration the base case will be reached):
- T(n) = 2^(n − 1)T + c
- T(n) = 2^n - 1 (The sum of the series would be 2^n - 1).
- This means that the Big-O notation is O(2^n), which is exponential.
