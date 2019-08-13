import cookielib
import urllib2
import urllib

url_start = r'https://www.zhihu.com/topic/19556498/questions?page='
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))





pener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

