# ======================================================= 
# counter.py is a program checking whether numbers are even
# or odd within the range of 0-10
# ------------------------------------
# @author C.H. 
# @since: 18/04/2023 
# @version 1.0   
# =======================================================

import unittest

runtest = 1

def even_or_odd(counter):                               
    # for counter in range (10):
        if(counter % 2) == 0:    
            # print(counter)            
            function_value = 'is even' 
            # print(function_value)                          
        else:                
            # print(counter)
            function_value = 'is odd'
            # print(function_value)                   

        if runtest == 1:
            return function_value

if runtest == 0:
    even_or_odd(1)

class test_counter(unittest.TestCase):

    def test_counter_success(self): 
        testnum = 2               
        actual = even_or_odd(testnum)
        expected = 'is odd'      
        try:
            assert actual == expected 
            print('Test successful! ' + 'Number ' + str(testnum) + ' ' + expected)       
        except:
            print('Error in test result! ' + 'Number ' + str(testnum) + ' ' + actual)            

# Run test with command: python -m unittest test_counter.py
