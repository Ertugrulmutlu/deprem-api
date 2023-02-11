#kÜTÜPHANE İNDİRİMİ--------------------------------
import requests
from bs4 import BeautifulSoup
#kÜTÜPHANE İNDİRİMİ--------------------------------
class Script_design:
    
    def __init__(self, url: str):
    #Gerekli verilerin init------------------------

        #Scrapping---------------------------------
        URL = url
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        self.result = soup.find_all("pre") 
        #Scrapping----------------------------------
        self.splitted_data = []
        self.pre_list = []
        self.deprem_liste = []
    #Gerekli verilerin init-------------------------
    def data_organize(self):
    #Gelen dataların ayrılması (Tablere göre)-------
        for i in self.result:
            for z in i:
                self.splitted_data = z.split("\n")

#Gelen dataların ayrılması (Tablere göre)-------
    #ayrılan dataların içinden İlksel ve Revize gibi terimlerin çıkartılıp bir düzene oturtulması-----
        for lists in self.splitted_data[7:-2]:
            lists.strip()
            sentences = lists.split()
            for i in range(0,8):
                self.pre_list.append(sentences[i])
            
            if sentences[8].encode('utf-8') != b'\xc4\xb0lksel' and sentences[8].encode('utf-8') != b'REVIZE01' and sentences[8].encode('utf-8') != b'REVIZE02' and sentences[8].encode('utf-8') != b'REVIZE03':
                self.pre_list.append(sentences[8])
                if sentences[9].encode('utf-8') != b'\xc4\xb0lksel' and sentences[9].encode('utf-8') != b'REVIZE01' and sentences[9].encode('utf-8') != b'REVIZE02' and sentences[9].encode('utf-8') != b'REVIZE03':
                    word = sentences[8] + sentences[9]
                    self.pre_list.pop(-1)
                    self.pre_list.append(word)
                    
                    if sentences[10].encode('utf-8') != b'\xc4\xb0lksel' and sentences[10].encode('utf-8') != b'REVIZE01' and sentences[10].encode('utf-8') != b'REVIZE02' and sentences[10].encode('utf-8') != "revize03":
                        word = word + sentences[10]
                        self.pre_list.pop(-1)
                        self.pre_list.append(word)
    #ayrılan dataların içinden İlksel ve Revize gibi terimlerin çıkartılıp bir düzene oturtulması-----
        #Datanın 9'ar parçaya ayrılması--------------------------------
        for i in range(0,len(self.pre_list)+2):
            if i == 0:
                continue
            if i % 9 == 0:
                pre_sentences = self.pre_list[i-9:i]
                self.deprem_liste.append(pre_sentences)
        #Datanın 9'ar parçaya ayrılması--------------------------------
        return self.deprem_liste




