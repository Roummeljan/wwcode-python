""" The Challenge
Author:
Description: Aling Nena�s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""
bill = input('How much is your total bill?')
payment = input('How much is your payment?')

Change = int(payment)- int(bill)

print('HI! Your Change is '+str(Change))