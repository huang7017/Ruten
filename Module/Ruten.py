import requests
from bs4 import BeautifulSoup
class Ruten:
    def __init__(self,url):
       self.__table,self.__money = [],[]
       self.__headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
       }
       self.__res = requests.get(url,headers=self.__headers)
       self.__res.encoding = 'utf-8'
    def getMenu(self):
        soup = BeautifulSoup(self.__res.text,'html.parser')
        stories1 = soup.find_all('h3',class_ = 'item-name isDefault-name')
        stories2 = soup.find_all('span', class_='item-direct-price rt-ml-remove')
        for s in stories1:
            self.__table.append(s.text)
        for s in stories2:
            self.__money.append(s.text)
        for i in range(len(self.__table)):
            self.__table[i] = self.__table[i].strip()
            self.__money[i] = self.__money[i].lstrip()
        for i in range(len(self.__table)):
            print('標題:',self.__table[i])
            print('價錢:', self.__money[i])
    def getTableSize(self):
        return len(self.__table)
    def getMoneySize(self):
        return len(self.__money)
if __name__ == "__main__":
    obj = Ruten("https://class.ruten.com.tw/user/index00.php?s=hambergurs&fbclid=IwAR1fDwWbVjYNhCySRMeDaSJZk7n-osbtwM7ezSusvn_olPSZLgtsnFbqKyU")
    obj.getMenu()