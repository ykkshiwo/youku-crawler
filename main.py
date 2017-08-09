import re
from dianshi_ import return_url_dianshi
from dianying_ import return_url_dianying
class youku:
    def __init__(self,url):
        self.url_=url
    def all_name(self):
        import urllib.request as ur
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

url_ds=return_url_dianshi("军事","大陆",2015)
url_dy=return_url_dianying("美国","西部",2013)
yk=youku(url_dy)
li=yk.all_name()
print(li)
