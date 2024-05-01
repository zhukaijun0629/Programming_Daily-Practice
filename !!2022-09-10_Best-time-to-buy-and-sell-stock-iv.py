'''
188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

from typing import List
import heapq


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        current_hand = []
        profits = []
        prices.append(0)
        
        for p in prices:
            if not current_hand:
                current_hand.append(p)
            elif len(current_hand) == 1:
                self.handleBuy(p, current_hand)
                print("after handleBuy", current_hand)
            elif len(current_hand) == 2:
                self.handleSell(p, current_hand, profits)
                print("after handleSell", current_hand)

        return sum(heapq.nlargest(k, profits))

            
    def handleBuy(self, p: int, current_hand: List[int]):
        if p <= current_hand[0]:
            current_hand[0] = p
        else:
            current_hand.append(p)
        return

    def handleSell(self, p: int, current_hand: List[int], profits: List[int]):
        if p >= current_hand[1]:
            current_hand[1] = p
        else:
            profits.append(current_hand[1]-current_hand[0])
            current_hand.pop()
            current_hand[0] = p


print(Solution().maxProfit(2,[6,1,3,2,4,7]))
