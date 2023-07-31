"""
Title: Fermat's Last Theorem Near Misses Finder
File Name: fermat_near_misses.py
External Files: None
Created External Files: None
Programmers:
1.	Vamshi Reddy Musku
2.	Venkata Ramana Patnam
Email Addresses:
- vamshireddymusku1@lewisu.edu
- venkataramanapatna@lewisu.edu

Course: SU23-CPSC-60500-002 - Software Engineering
Date: Monday, July 31, 2023
Explanation:
A Python application called the Fermat's Last Theorem Near Misses Finder enables an interactive user to look for "near misses" in the equation xn + yn = zn of the form (x, y, z, n, k). In order to narrow the search window for the positive integer values of x, y, and z, the software asks the user to enter the values of n (where 2 n 12) and k (where k > 10). A near miss is described as a reasonably minor deviation from zn of (xn + yn).
A binary search technique is employed by the software to systematically locate x, y, and z combinations that are "almost right." It calculates (xn + yn) for each conceivable x, y combination and then searches for whole integers z and (z + 1) that "bracket" (xn + yn) such that zn (xn + yn) (z + 1)n. The "miss" is then chosen as the smaller of these two values: [(z + 1)n - (x + y + n)] or [(z + n) - zn]. By dividing the miss by (xn + yn), one may get the relative magnitude of the miss.
The application shows the appropriate x, y, z, real miss, and relative miss on the screen along with the least relative miss that has been discovered thus far. When all combinations have been tried, the software displays the output with the least potential miss as the final result.

Resources Used:
Klarreich, E. (2006). Springfield theory: Mathematical references abound on the simpsons. Science News, 169(23), 360-360.

Harvard Mathematics Department – link: https://people.math.harvard.edu/~elkies/ferm.html#:~:text=Tables%20of%20Fermat%20%E2%80%9Cnear%2Dmisses,n%20in%20%5B4%2C20%5D&text=r%20%3D%20n%20zn%E2%88%923%20%2F,a%20500MHz%20machine%20running%20GP. 
"""

import sys

def calculate_miss(x, y, z, n):
    # Calculate (x^n + y^n) and z^n
    xn_yn = x ** n + y ** n
    zn = z ** n
    znp1 = (z + 1) ** n

    # Calculate the two potential misses
    miss_xn_yn_zn = abs(xn_yn - zn)
    miss_xn_yn_zn_plus_1 = abs(znp1 - xn_yn)

    # Return the minimum miss and relative miss
    return min(miss_xn_yn_zn, miss_xn_yn_zn_plus_1), min(miss_xn_yn_zn, miss_xn_yn_zn_plus_1) / xn_yn * 100


def binary_search_near_misses(n, k):
    min_relative_miss = float('inf')
    min_x, min_y, min_z, min_miss = 0, 0, 0, 0

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            low, high = 1, k
            while low <= high:
                mid = (low + high) // 2
                miss, relative_miss = calculate_miss(x, y, mid, n)
                if relative_miss < min_relative_miss:
                    # Update the smallest relative miss and corresponding values
                    min_relative_miss = relative_miss
                    min_x, min_y, min_z, min_miss = x, y, mid, miss
                if calculate_miss(x, y, mid + 1, n)[1] < calculate_miss(x, y, mid, n)[1]:
                    low = mid + 1
                else:
                    high = mid - 1

    # Print the final results
    print("-------------------------------------------------")
    print(f"Smallest relative miss: {min_relative_miss:.2f}%")
    print(f"for x: {min_x}, y: {min_y}, z: {min_z}, n: {n}, and k: {k}")
    print(f"Actual Miss: {min_miss}")
    print(f"Relative Miss: {min_relative_miss:.2f}%")
    print("-------------------------------------------------")


def main():
    try:
        # Welcome message and user input for n and k
        print("Welcome to the Fermat's Last Theorem Near Misses Finder!")
        print("-------------------------------------------------------")
        
        n = int(input("Enter the value of n (2 < n < 12): "))
        k = int(input("Enter the value of k (k > 10): "))

        if not (2 < n < 12 and k > 10):
            raise ValueError("Invalid input. Please make sure 2 < n < 12 and k > 10.")
        
        if k > sys.maxsize ** (1 / n):  # Check for potential overflow
            raise ValueError(f"k should be less than {sys.maxsize ** (1 / n)} to avoid overflow.")

        # Find the near misses using binary search and print the results
        binary_search_near_misses(n, k)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
