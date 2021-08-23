import requests
import bs4
import re
import rakudaCommand
errorMessage_array = list()

def getErrorMessage():
    global errorMessage_array
    if errorMessage_array is not None:
        return errorMessage_array
def clearErrorMessage():
    global errorMessage_array
    errorMessage_array =list()

def get_price(page_url,oder_num):
    if("https://www.switch-science.com/" in page_url):#switchsience用
        try:
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            selected_html = soup.select(".table-bordered-rect tr td span.price")
            selected_html = str(selected_html[0])
            selected_html = selected_html.replace(',', '')
            selected_html = selected_html.replace('\n', '')
            selected_html = selected_html.replace(' ', '')
            selected_html = selected_html.replace('<spanclass="price">', '')
            results = selected_html.replace('</span>', '')
            results= int(results)
            return results
        except requests.exceptions.ConnectionError:
            errorMessage_array.append("switchscienceサイトにアクセスができませんでした。")

    elif("https://www.marutsu.co.jp" in page_url):#marutu用
        try:
            lot_price = dict()
            morethan_lot= None
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            lot_list_html = soup.select(".item_price table th .set-item span")#注文数によって個数が変わるため
            price_list_html = soup.select(".item_price table td .stepPriceIncludeTax")
            if len(lot_list_html)==len(price_list_html):
                lot_list= list()
                price_list = list()
                for i in range(len(lot_list_html)):
                    lot_html=str(lot_list_html[i])
                    price_html=str(price_list_html[i])
                    lot_html = lot_html.replace("\n","")
                    price_html = price_html.replace("\n","")
                    lot  = re.findall('[0-9]+', lot_html)[3]
                    price = re.findall('[0-9]+', price_html)[3]

                    lot_list.append(int(lot))
                    price_list.append(int(price))
                isMorethan = list()
                for i in range(len(lot_list_html)-1):
                    if oder_num >= lot_list[-1]:
                        morethan_lot = lot_list[-1]
                    elif lot_list[i] <= oder_num and oder_num < lot_list[i+1]:
                        morethan_lot = lot_list[i]
                morethan_lot_index = lot_list.index(morethan_lot)

                return price_list[morethan_lot_index]

        except requests.exceptions.ConnectionError:
            errorMessage_array.append("marutuサイトにアクセスができませんでした。")
    elif("https://akizukidenshi.com/" in page_url):#akiduki用
        try:
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            selected_html = soup.select(".order_g td .f14b")
            selected_html = str(selected_html[1])
            selected_html = selected_html.replace('<span class="f14b">￥', '')
            selected_html = selected_html.replace('\n', '')
            selected_html = selected_html.replace('</span>', '')
            selected_html = selected_html.replace(',', '')
            results= int(selected_html)
            return results
        except requests.exceptions.ConnectionError:
            return "error"

    
    else:
        print("this url is invalid")

def get_name(page_url):
    if("https://www.switch-science.com/" in page_url):#switchsience用
        try:
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            selected_html = soup.select(".table-bordered-rect tr td")
            selected_html = str(selected_html[1])
            selected_html = selected_html.replace('<td>', '')
            results = selected_html.replace('</td>', '')
            return results
        except requests.exceptions.ConnectionError:
            errorMessage_array.append("switchscienceサイトにアクセスができませんでした。")
    if("https://www.marutsu.co.jp" in page_url):#switchsience用
        try:
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            selected_html = soup.select("title")
            selected_html = str(selected_html[0])
            selected_html = selected_html.replace("｜電子部品・半導体通販のマルツ</title>","")
            selected_html =  selected_html.replace("<title>","")
            results = selected_html
            return results
        except requests.exceptions.ConnectionError:
            errorMessage_array.append("marutuサイトにアクセスができませんでした。")

    elif("https://akizukidenshi.com/" in page_url):#akiduki用
        try:
            res = requests.get(page_url)
            soup = bs4.BeautifulSoup(res.text,"html.parser")
            print(res)
            results = None
            selected_html = soup.select(".order_g")
            selected_html = str(selected_html[0])
            startIndex = selected_html.find("""<div class="order_g">""")+21
            endIndex = selected_html.find("""<a href=""")
            results=selected_html[startIndex:endIndex]
            results = results.split("　")
            results=results[1]
            return results
        except requests.exceptions.ConnectionError:
            return "error"
    else:
        errorMessage_array.append(str(page_url)+":このサイトには対応していません。")