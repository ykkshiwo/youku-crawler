class return_url_dianshi:
    def __init__(self, type, place, year):
        self.type = type
        self.place = place
        self.year = year
    def dianshi(self):
        pass
    def url(self,yema):
        import urllib.request as ur
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
