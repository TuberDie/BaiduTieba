from urllib import request
from bs4 import BeautifulSoup
from tkinter import *
root = Tk()
response = request.urlopen("http://news.163.com/")
a = response.read()
soup = BeautifulSoup(a,'html5lib')
r = soup.find_all('div',class_='mod_top_news2')
#print (r)
#y = r[0].find_all('li')
y = r[0].find_all('h2')
tr = r[0].find_all('li')
t = 0
xw = '今日头条:\n'+y[0].get_text().strip()+'\n'+y[1].get_text().strip()+'新闻:\n'
Label(root,text=xw).pack()
#print (xw)
for i in range(len(tr)):
    #print(tr[t].get_text())
    Label(root,text=tr[t].get_text()).pack()
    t = t + 1

#ad = '今日头条:\n'+y[0].get_text().strip()+'\n'+y[1].get_text().strip()
#Label(root,text=ad).pack()
mainloop()
