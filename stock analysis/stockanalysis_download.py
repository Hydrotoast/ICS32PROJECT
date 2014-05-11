###stockanalysis_downloadquotes.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065
##Project #2: Outside the Wall

import http.client
import urllib.request
import urllib.error


def download_stock_data()-> [[str]]:
    url = _pick_url()
    if len(url) == 0:
        return
    else:
        downloaded_data = _download_url_to_python(url)
        return _split_line_to_list(downloaded_data)
    

def _pick_url() -> str:
    print('Choose a URL to download (Press Enter or Return to quit)')
    return input('URL: ').strip()


def _download_url_to_python(url_to_download: str) -> str:
    with urllib.request.urlopen(url_to_download) as response:
        return response.read().decode('utf-8').strip()


def _split_line_to_list(downloaded_data: str)-> [[str]]:
    return[column.split(',')for column in downloaded_data.split('\n')]
