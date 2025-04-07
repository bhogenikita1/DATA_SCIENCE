
'''
Alex wants to buy exactly N bananas from two vendors.
Each vendor sells bananas in fixed-sized bunches.
Alex can only purchase full bunches and not individual bananas.
He needs your help to determine the minimum cost required to buy exaclty N bananas

'''

no_banana=int(input("Enter no. of banana to be purchaesd: "))
lot1=int(input("What is the size of lot1 that vendor 1 provides: "))
price1=int(input("What is the price of lot1: "))
lot2=int(input("What is the size of lot2 that vendor 2 provides: "))
price2=int(input("What is the price of lot2: "))

def min_cost(no_banana,lot1,price1,lot2,price2):
    lot_a=no_banana//lot1
    print(f'lot a:{lot_a}')
    lot_b=no_banana//lot2
    print(f'lot b:{lot_b}')
    cost_a=lot_a*price1
    print(f'cost_a: {cost_a}')
    cost_b=lot_b*price2
    print(f'cost_b: {cost_b}')
    return min(cost_a, cost_b)

min_cost(no_banana, lot1, price1, lot2, price2)   

#___________________________________________________________________


#Bubble Sort
'''


Steps of Bubble Sort:

Start from the first element and compare it with the next element.
If the first element is greater than the next, swap them.
Move to the next pair and repeat step 2 for the entire array.
The largest element moves to its correct position at the end of the
Repeat the process for the remaining unsorted elements until the en

Sorting [5, 3, 8, 4, 2]

Example Walkthrough

Given Array
[5,3,8,4,2] (n=5)

Pass 1 (Move the largest to the end):
    
Compare 5 and 3 → Swap → [3, 5, 8, 4, 2]
Compare 5 and 8 → No swap
Compare 8 and 4 → Swap → [3, 5, 4, 8, 2]
Compare 8 and 2 → Swap [3, 5, 4, 2, 8]

Pass 2 (Move the second-largest to the correct position):

Compare 3 and 5 → No swap
Compare 5 and 4 → Swap → [3, 4, 5, 2, 8]
Compare 5 and 2 → Swap [3, 4, 2, 5, 8]

Pass 3:

Compare 3 and 4 → No swap
Given array:

[5, 3, 8, 4, 2] (n = 5)
Pass 1: Moves largest element to index n-1
Pass 2: Moves second-largest to index n-2
Pass 3: Moves third-largest to index n-3
Pass 4: Moves fourth-largest to index n-4
Pass 5 (not needed): All elements are sorted
Since the last element is automatically placed correctly in th

__Why range(n-i-1) for the Inner Loop?**
After i passes, the last i elements are already sorted.
We don't need to check them again.
So, we run the inner loop only up to n-i-1.
This reduces unnecessary comparisons and improves efficiency.


'''
def bubble_sort(lst):
    n=len(lst)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[5,3,8,4,2]
bubble_sort(lst)            













 
