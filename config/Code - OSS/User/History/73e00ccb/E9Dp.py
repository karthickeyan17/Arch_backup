import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

cookies = {
    'csrftoken': 'SlEdJr4ui152zQ25bSdAUHwwNhieMLI8Ub2T8BRNxVpeDargrZQ2Vn3eFRByGhJp',
    '_ga': 'GA1.1.1376505412.1719914528',
    'gr_user_id': '25c57d33-80c3-434a-9c29-a197a4c7b89c',
    '_ga_CDRWKZTDEX': 'GS1.1.1721649753.35.1.1721650342.51.0.0',
    '87b5a3c3f1a55520_gr_last_sent_cs1': 'karthickeyan_S',
    '__stripe_mid': '2c1de793-6979-4485-8668-ec687b7b90a783f323',
    '__gads': 'ID=06284a2429e43843:T=1720032639:RT=1720032639:S=ALNI_MbEIA66J6UhlMhe9ryVXo6gmkKvtw',
    '__gpi': 'UID=00000e63bd49c425:T=1720032639:RT=1720032639:S=ALNI_MZeJmOCCCzjwZwpb4gPTPLCuLKUiw',
    '__eoi': 'ID=e306d56c305ac638:T=1720032639:RT=1720032639:S=AA-Afjb4r89qE5nmJSeJRqtvY1Yq',
    'FCNEC': '%5B%5B%22AKsRol9ONQJVfb-4V3OcGFkceklsQfw72UYLikcRJsv5Fw5W7Lo7S21s73wkr_6ihwqPEpOGNx0YqY8qNNgG0WAgUVF8ePZz4G7EdGJcRdaoxePQ94Qz_lY6OINwtpZwUZwrW3pJXqygPDPd6E0y3RMZSjaIXgGGiA%3D%3D%22%5D%5D',
    '87b5a3c3f1a55520_gr_cs1': 'karthickeyan_S',
    'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTAwMzgzOTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjRmZThhOWE3NThkM2I2NzcwMjM2ZmU2Y2U0OTUxZWU4MDA3MzgxZjJlOTk0N2ZiOThhYmE1Y2E4YTc0MzU2ZGIiLCJpZCI6MTAwMzgzOTIsImVtYWlsIjoic2thcnRoaWNrZXlhbjcwN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImthcnRoaWNrZXlhbl9TIiwidXNlcl9zbHVnIjoia2FydGhpY2tleWFuX1MiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY4ODgwMTg5OS5wbmciLCJyZWZyZXNoZWRfYXQiOjE3MjQ2NjY2NzIsImlwIjoiMTAzLjE5Ni4yOC4xNzkiLCJpZGVudGl0eSI6IjY3NjM5NDNiMWE0MWE1ZTZlZDQ3MmQ3NDYwNWY0YTVkIiwiZGV2aWNlX3dpdGhfaXAiOlsiM2JlNTI0MmMyOTE0NTVmMzNlM2VhZmFkYThjYmJkNTUiLCIxMDMuMTk2LjI4LjE3OSJdLCJzZXNzaW9uX2lkIjo2ODM2OTIyOSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.W1rjeaURN3PooelkpPeZT3IUGqXvx3rwo2aoSGxotOE',
    'cf_clearance': 'AxdbVAt5kdXuIUUsr8hbIQb22hVEht8UyxztynV75CY-1724408747-1.2.1.1-bBbtLFm4L7TIIh4pQRo0zNME14WeKZcMOwQFS4nwBciIPHG1a1.pQOxz0hEfIN2wiSMEhG4KaiqJQC_pLvKKIeWSc9NLS_ldtyNX34g4xhWp50EDE7.vSypaWhlGqnRnQ1oHeBo70lrvDqlRQ8og8pgRM1ad43aZaYgT0_QrMLp_gMS54sg5QOPbHaGaUezmtFEtV.6MwNJjQyjjUUcUj4V16TNgIXa04zsiOqWo1fH0CFaI89I8sUJSNcdvHDDUvcMZElitgY2Z2VIhWXBTAeSb2Ro8EuxLcr1WUdc75YyVvIcnKxf3t.UlnBPaUTSJ9CVWfuN_IFzYx12QpxdwO_FQI4Ahb5mpWJvN8eDYFx_xzR1JF.avuB7g_WJG9piV',
    '_dd_s': 'rum=0&expire=1724687387927',
    'ip_check': '(false, "103.196.28.179")',
    'INGRESSCOOKIE': 'c7e16100a4bdbd983368370c0783670d|8e0876c7c1464cc0ac96bc2edceabd27',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://leetcode.com/',
    'Connection': 'keep-alive',
    # 'Cookie': 'csrftoken=SlEdJr4ui152zQ25bSdAUHwwNhieMLI8Ub2T8BRNxVpeDargrZQ2Vn3eFRByGhJp; _ga=GA1.1.1376505412.1719914528; gr_user_id=25c57d33-80c3-434a-9c29-a197a4c7b89c; _ga_CDRWKZTDEX=GS1.1.1721649753.35.1.1721650342.51.0.0; 87b5a3c3f1a55520_gr_last_sent_cs1=karthickeyan_S; __stripe_mid=2c1de793-6979-4485-8668-ec687b7b90a783f323; __gads=ID=06284a2429e43843:T=1720032639:RT=1720032639:S=ALNI_MbEIA66J6UhlMhe9ryVXo6gmkKvtw; __gpi=UID=00000e63bd49c425:T=1720032639:RT=1720032639:S=ALNI_MZeJmOCCCzjwZwpb4gPTPLCuLKUiw; __eoi=ID=e306d56c305ac638:T=1720032639:RT=1720032639:S=AA-Afjb4r89qE5nmJSeJRqtvY1Yq; FCNEC=%5B%5B%22AKsRol9ONQJVfb-4V3OcGFkceklsQfw72UYLikcRJsv5Fw5W7Lo7S21s73wkr_6ihwqPEpOGNx0YqY8qNNgG0WAgUVF8ePZz4G7EdGJcRdaoxePQ94Qz_lY6OINwtpZwUZwrW3pJXqygPDPd6E0y3RMZSjaIXgGGiA%3D%3D%22%5D%5D; 87b5a3c3f1a55520_gr_cs1=karthickeyan_S; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTAwMzgzOTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjRmZThhOWE3NThkM2I2NzcwMjM2ZmU2Y2U0OTUxZWU4MDA3MzgxZjJlOTk0N2ZiOThhYmE1Y2E4YTc0MzU2ZGIiLCJpZCI6MTAwMzgzOTIsImVtYWlsIjoic2thcnRoaWNrZXlhbjcwN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImthcnRoaWNrZXlhbl9TIiwidXNlcl9zbHVnIjoia2FydGhpY2tleWFuX1MiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY4ODgwMTg5OS5wbmciLCJyZWZyZXNoZWRfYXQiOjE3MjQ2NjY2NzIsImlwIjoiMTAzLjE5Ni4yOC4xNzkiLCJpZGVudGl0eSI6IjY3NjM5NDNiMWE0MWE1ZTZlZDQ3MmQ3NDYwNWY0YTVkIiwiZGV2aWNlX3dpdGhfaXAiOlsiM2JlNTI0MmMyOTE0NTVmMzNlM2VhZmFkYThjYmJkNTUiLCIxMDMuMTk2LjI4LjE3OSJdLCJzZXNzaW9uX2lkIjo2ODM2OTIyOSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.W1rjeaURN3PooelkpPeZT3IUGqXvx3rwo2aoSGxotOE; cf_clearance=AxdbVAt5kdXuIUUsr8hbIQb22hVEht8UyxztynV75CY-1724408747-1.2.1.1-bBbtLFm4L7TIIh4pQRo0zNME14WeKZcMOwQFS4nwBciIPHG1a1.pQOxz0hEfIN2wiSMEhG4KaiqJQC_pLvKKIeWSc9NLS_ldtyNX34g4xhWp50EDE7.vSypaWhlGqnRnQ1oHeBo70lrvDqlRQ8og8pgRM1ad43aZaYgT0_QrMLp_gMS54sg5QOPbHaGaUezmtFEtV.6MwNJjQyjjUUcUj4V16TNgIXa04zsiOqWo1fH0CFaI89I8sUJSNcdvHDDUvcMZElitgY2Z2VIhWXBTAeSb2Ro8EuxLcr1WUdc75YyVvIcnKxf3t.UlnBPaUTSJ9CVWfuN_IFzYx12QpxdwO_FQI4Ahb5mpWJvN8eDYFx_xzR1JF.avuB7g_WJG9piV; _dd_s=rum=0&expire=1724687387927; ip_check=(false, "103.196.28.179"); INGRESSCOOKIE=c7e16100a4bdbd983368370c0783670d|8e0876c7c1464cc0ac96bc2edceabd27',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://leetcode.com/progress/', cookies=cookies, headers=headers)