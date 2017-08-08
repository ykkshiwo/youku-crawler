import urllib.request as ur
url_1="http://list.youku.com/category/show/c_97_g_"
key_1="古装"
key_1_b=ur.quote(key_1)
key_2="大陆"
key_2_b=ur.quote(key_2)
url_2="_r_2016_pt_0_s_1_d_1.html?spm=a2h1n.8251845.filterPanel.5!6~1~3~A"
url=url_1+key_1_b+"_a_"+key_2_b+url_2
