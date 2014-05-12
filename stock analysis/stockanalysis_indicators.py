###stockanalysis_indicators.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065
##Project #2: Outside the Wall

import math
import stockanalysis_download

class SimpleMovingAverageIndicator:
    def __init__(self, number_of_days: int):
        self._number_of_days = number_of_days
        
    def execute(self, nested_data_list: list)-> list:
        indicator_list = []
        for row_number in range(len(nested_data_list)-1,-1,-1):
            indicator_value = 0
            count = self._number_of_days
            for day in range(self._number_of_days):
                indicator_value += float(nested_data_list[row_number-day][-3])
                count -= 1
                if count == 0:
                    indicator_list.append(round(indicator_value/self._number_of_days,2))
        return indicator_list[0:len(nested_data_list)-self._number_of_days+1]

