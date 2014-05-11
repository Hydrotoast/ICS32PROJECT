###stockanalysis_ui.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065
##Project #2: Outside the Wall

import time
from datetime import date

def _run_user_interface() -> None:
    ticker_symbol = 'MCF'#input('Please specify the ticker symbol of the company that you are looking for: ')
    start_date = input('Please specify the starting date of the analysis in YYYY-MM-DD format: ')
    end_date = input('Please specify the ending date of the analysis in YYYY-MM-DD format: ')
    try:
        print('works here')
        if _check_valid_start_date(start_date):
            #continute after checking the date
            print('Please specify your starting date again.')
            #some function
        if not _check_valid_end_date(start_date, end_date):
            print('Please specify your ending date again.')
            
    except:
        print('you did something wrong')
            
def _check_valid_start_date(start_date: str)-> bool:
    start_date = _format_date(start_date)
    if start_date <= date.today():
        return True
    #condition one: start date should be on today or before today's date.
    #condition two: if the date is entered in an incorrect format, ask the user to specify another. 
    #if both of these conditions are not true ask the user to specify another

def _check_valid_end_date(start_date: str, end_date: str)-> bool:
    start_date = _format_date(start_date)
    end_date = _format_date(end_date)
    if end_date <= date.today() and end_date >= start_date:
        return True


def _format_date(day: str)-> date:
    datecomponent = day.split('-')
    return date(int(datecomponent[0]),int(datecomponent[1]),int(datecomponent[2]))
    


##if __name__ == '__main__':
##   _run_user_interface()
    
