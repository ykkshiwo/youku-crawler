import urllib.request as ur
import re
class return_url:
    def __init__(self, type, place, year):
        self.type = type
        self.place = place
        self.year = year
    def url(self,yema):
        url_1 = "http://list.youku.com/category/show/c_97_g_"
        key_1 = self.type
        key_1_b = ur.quote(key_1)
        key_2 = self.place
        key_2_b = ur.quote(key_2)
        url_2 = "_r_"
        key_year = str(self.year)
        url_2_1 = "_pt_0_s_1_d_1_p_"
        key_3 = str(yema)
        url_3 = ".html?spm=a2h1n.8251845.filterPanel.5!3~1~3!2~A"
        url = url_1 + key_1_b + "_a_" + key_2_b + url_2 + key_year + url_2_1 + key_3 + url_3
        return url


class youku:
    def __init__(self,url):
        self.url_=url

    def all_name(self):
        regex_mz = re.compile(rb'<a href="//list.*?title="(?P<mz>.{,100})" target="_blank">(?P=mz)</a>', re.S)
        bb=bytes("下一页",encoding="utf-8")
        regex_yeshu=re.compile(rb'<a href=.*?charset="-4-1-999">'+bb+rb'</a>')
        data = ur.urlopen(self.url_.url(1))
        file = data.read()
        l=[]
        l=regex_mz.findall(file)
        y=2
        while regex_yeshu.search(file):
            url_dz=self.url_.url(y)
            file = ur.urlopen(url_dz).read()
            list_ = regex_mz.findall(file)
            l=l+list_
            y=y+1
        list_mz = [str(i, encoding="utf-8") for i in l]
        return list_mz

url=return_url("古装","大陆",2013)
yk=youku(url)
li=yk.all_name()
print(li)
