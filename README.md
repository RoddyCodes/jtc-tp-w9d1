# jtc-tp-w9d1
You are given a set of algorithms that need to be analyzed for their time complexity and optimized for better efficiency. Your task is to determine the Big O notation for each algorithm, identify inefficiencies, and propose optimized solutions.
1. algorithmn 
- for an unsorted array to find the target value; In the worst and average cases, the algorithm checks each element once which is O(n) time complexity. In the best case, the target value is found at the first position, resulting in O(1) time complexity. 
- there is no real optimization to this since as of now, the code is clear anc concise. The code also has to check every value regardless, unless it gets lucky on the first try; making it a (O)n time complexity. 
2. bubble_sort: takes an array and puts it into ascending order. For the original, the time complexity is O(n**2) since it had nested iterations needed. The original is in the bubble_sort.py file. The optimized version is in the better_bubble.py file. In the optimized version, the code is more concise and clear. There is already built in function for python that allows us to do this. 
