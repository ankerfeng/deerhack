__author__ = 'hal0'

import re
import urllib
import requests
from optparse import OptionParser

parser = OptionParser(usage='%prog fofa/lib/ips API', \
                       description='Get the target url or ip from html!')

parser.add_option("-s", "--site", dest="site",
                  help="the target site!", metavar="site")

parser.add_option("-o", "--output", dest="output",
                  help="output the ip or domain or all!\nexample: -o id",\
                  metavar="Ip(i)Domain(d)",\
                  default='id')

class apiFofaLabIps:
    def __init__(self):
        self.ip_list=[]
        self.domain_list=[]

    def get_cookie(self):

        cookie = open('FoFaCookie', 'r').read()
        regex = re.search(r'_fofa_session=(?P<s_key>[^;]+)', cookie)
        session_key = regex.group('s_key')
        regex = re.search(r'authenticity_token=(?P<t_key>[^&^ ]+)', cookie)
        token_key = regex.group('t_key')
        return {'session_key':session_key, 'token_key':token_key}


    def get_lab_ips(self, host):

        s = requests.Session()
        proxies = {'http':'http://127.0.0.1:8080'}
        url = "http://fofa.so/lab/ips"
        session = requests.Session()
        cookie={"_fofa_session": None}
        author_token=None
        if cookie['_fofa_session'] is None \
                or author_token is None:
            _cookie = self.get_cookie()
            cookie['_fofa_session']=_cookie['session_key']
            author_token = _cookie['token_key']

        data = {'utf8':urllib.unquote('%E2%9C%93'),\
                'all':'true',\
                'authenticity_token':'%s' % (urllib.unquote(author_token)),\
                'domain':'%s' % (host)}
        try:
            resp = session.post(url, data=data,\
                                cookies=cookie)
            return resp.text

        except requests.HTTPError, e:
            print e.errno

        except BaseException, e:
            print e.message


    def crawler(self, html):
        ptr=r'<div class="col-lg-4".+?</div>'
        pattern=re.compile(ptr, re.S)
        self.ip_list = pattern.findall(html)
        print 'find ip:', len(self.ip_list)
        ptr=r'<div class="col-lg-8".+?</div>'
        pattern=re.compile(ptr, re.S)
        self.domain_list = pattern.findall(html)
        print 'find url:', len(self.domain_list)


    def ip_print(self):
        ptr = r'https?://(?P<ip>[^/^"]+)'
        pattern = re.compile(ptr, re.S)
        for line in self.ip_list:
            res = pattern.findall(line)
            for ip in res:
                print ip


    def domain_print(self):
        ptr = r'(?P<domain>https?://[^/^"]+)'
        pattern = re.compile(ptr, re.S)
        for line in self.domain_list:
            res = pattern.findall(line)
            for domain in res:
                print domain.replace('<', '')
def main():
    site = options.site
    output = options.output
    api = apiFofaLabIps()
    html = api.get_lab_ips(site)
    api.crawler(html)
    if 'd' in output:
        api.domain_print()
    if 'i' in output:
        api.ip_print()


if __name__ == '__main__':
    options, args = parser.parse_args()
    if options.site is None:
        parser.print_help()
    else:
        main()


