import string, urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        sName = string.zfill(i, 5) + '.html'
        print 'Downloading ' + str(i) +', and stored them as' + sName + '......'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

bdurl = str(raw_input(u'input the address'))
begin_page = int(raw_input(u'begin page: \n'))
end_page = int(raw_input(u'end page: \n'))

baidu_tieba(bdurl, begin_page, end_page)
