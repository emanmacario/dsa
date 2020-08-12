# Three in One: Describe how you could use a single array to implement three stacks.
# Hints: #2, #72, #38, #58

"""
Approach 1: Fixed Division
    - Can divide the array into three equal parts
        i. [0, n/3)
        ii. [n/3, 2n/3)
        iii. [2n/3, n)
    - Would need to keep track of top index value for each separate stack

Approach 2: Flexible Divisions
    - Allow stack 'blocks' to be flexible in size
    - When one stack exceeds initial capacity, grow allowable capacity and shift elements as necessary
    - Array is circular, final stack may start at end of array and wrap around to beginning
"""