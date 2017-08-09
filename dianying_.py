class return_url_dianying:
    def __init__(self, types, place, year):
        self.type = types
        self.place = place
        self.year = year
    def url(self,yema=1):
        import urllib.request as ur
        url_1 = "http://list.youku.com/category/show/c_96_g_"
        key_1 = self.place
        key_1_b = ur.quote(key_1)
        key_2 = self.type
        key_2_b = ur.quote(key_2)
        url_2 = "_a_"
        key_year = str(self.year)
        url_2_1 = "_s_1_d_1_r_"
        url_3 = ".html?spm=a2h1n.8251845.filterPanel.5!3~1~3!6~A"
        url = url_1 + key_1_b + url_2 +key_2_b + url_2_1  +key_year+ url_3
        return url
