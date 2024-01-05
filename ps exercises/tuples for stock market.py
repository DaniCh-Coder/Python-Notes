"""
In a stock market, there is a product with its infinite stocks. 
The stock prices are given for N days, where price[i] denotes the price of the stock on the ith day.
There is a rule that a customer can buy at most i stock on the ith day.
If the customer has an amount of k amount of money initially. 
The task is to find out the maximum number of stocks a customer can buy. 
Example 1:
Input:
price = [10,7,19]
k = 45
Output: 
4
Explanation: 
A customer purchases 1 stock on day 1, 2 stocks on day 2 and 1 stock on day 3 for 10, 7 * 2 = 14 and 19 respectively. 
Hence, total amount is 10 + 14 + 19 = 43 and number of stocks purchased is 4.
"""
from functools import reduce

prices = [7,10,4]
k = 100

# Create a list of tuples, each containing the stock value and its limit
stock_values_limits, res = [(prices[i], i + 1) for i in range(len(prices))], 0
        
# Sort the stock_values_limits list based on stock value (ascending order)
stock_values_limits.sort(key=lambda x: x[0])
        
# Iterate over the sorted list
for price, limit in stock_values_limits:
    # If k becomes zero or negative, or if the price is greater than k, break the loop
    if ((k <= 0) or (price > k)):
        break
            
    # Calculate the maximum number of stocks that can be bought within the limit or based on available funds
    temp = min(limit, (k // price))
            
    # Add the number of stocks bought to the result
    res += temp
            
    # Reduce the available funds by the cost of the bought stocks
    k -= (price * temp)
        
    # Return the total number of stocks bought
    # return(res)

print(res)