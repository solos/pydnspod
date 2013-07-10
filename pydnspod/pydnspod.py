#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import re
from config import USER_AGENT, PARAMS
from config import DEFAULT_FORMAT, DEFAULT_LANG, LOGIN_REMEMBER


class Api(object):

    def __init__(self, email, password, cookie=''):
        self.base_url = "https://dnsapi.cn/"
        self.path = "Info.Version"
        self.params = {}
        self._cookie = cookie
        self._email = email
        self._password = password

    def version(self, **kw):
        self.path = "Info.Version"
        return self._request(**kw)

    def _is_param_missing(self, **kw):
        path = self.path
        try:
            reqir_params = PARAMS[path]["required"]
        except:
            return False
        for par in reqir_params:
            missing = True
            if isinstance(par, tuple):
                for item in par:
                    if item in kw:
                        missing = False
                        break
                if missing:
                    mis_par = " or ".join(par)
                    return "%s required. '%s' requires %s" % \
                           (mis_par, path, reqir_params)
            elif isinstance(par, str):
                if par not in kw:
                    return "%s required. '%s' requires %s" % \
                           (par, path, reqir_params)
        return False

    def _request(self, **kw):
        self.params.update({
            "login_email": self._email,
            "login_password": self._password,
            "format": DEFAULT_FORMAT,
            "lang": DEFAULT_LANG,
            "login_remember": LOGIN_REMEMBER
        })
        self.params.update(kw)
        param_missing = self._is_param_missing(**kw)
        if not param_missing:
            params = urllib.urlencode(self.params)
            headers = {"User-Agent": USER_AGENT, "Cookie": self._cookie}
            url = "".join((self.base_url, self.path))
            req = urllib2.Request(url, params, headers)
            try:
                resp = urllib2.urlopen(req)
                response = resp.read()
                resp_headers = resp.info()
            except Exception, e:
                return e
            return resp_headers if "login_code" in kw and \
                self.path == "User.Detail" else response
        else:
            return param_missing

    def get_cookie(self, login_code):
        self.path = "User.Detail"
        resp_headers = self._request(login_code=login_code)
        cookie_match = re.compile(r'(?P<cookie>t\d+=[^;]*);')
        match_result = cookie_match.findall(resp_headers['set-cookie'])
        if match_result:
            self._cookie = match_result[0]
        return self._cookie

    def set_cookie(self, cookie):
        self._cookie = cookie
        return self._cookie


class User(Api):

    def __init__(self, email, password, cookie=''):
        super(User, self).__init__(email, password, cookie=cookie)

    def detail(self, **kw):
        self.path = "User.Detail"
        return self._request(**kw)

    def modify(self, **kw):
        self.path = "User.Modify"
        return self._request(**kw)

    def modify_password(self, **kw):
        self.path = "Userpasswd.Modify"
        return self._request(**kw)

    def modify_email(self, **kw):
        self.path = "Usermail.Modify"
        return self._request(**kw)

    def get_verify_code(self, **kw):
        self.path = "Telephoneverify.Code"
        return self._request(**kw)

    def log(self, **kw):
        self.path = "User.Log"
        return self._request(**kw)


class Domain(Api):

    def __init__(self, email, password, cookie=''):
        super(Domain, self).__init__(email, password, cookie=cookie)

    def create(self, **kw):
        self.path = "Domain.Create"
        return self._request(**kw)

    def list(self, **kw):
        self.path = "Domain.List"
        return self._request(**kw)

    def remove(self, **kw):
        self.path = "Domain.Remove"
        return self._request(**kw)

    def modify_status(self, **kw):
        self.path = "Domain.Status"
        return self._request(**kw)

    def info(self, **kw):
        self.path = "Domain.Info"
        return self._request(**kw)

    def log(self, **kw):
        self.path = "Domain.Log"
        return self._request(**kw)

    def se_push(self, **kw):
        self.path = "Domain.Searchenginepush"
        return self._request(**kw)

    def share(self, **kw):
        self.path = "Domainshare.Create"
        return self._request(**kw)

    def list_share(self, **kw):
        self.path = "Domainshare.List"
        return self._request(**kw)

    def modify_share(self, **kw):
        self.path = "Domainshare.Modify"
        return self._request(**kw)

    def remove_share(self, **kw):
        self.path = "Domainshare.Remove"
        return self._request(**kw)

    def transfer(self, **kw):
        self.path = "Domain.Transfer"
        return self._request(**kw)

    def lock(self, **kw):
        self.path = "Domain.Lock"
        return self._request(**kw)

    def lock_status(self, **kw):
        self.path = "Domain.Lockstatus"
        return self._request(**kw)

    def unlock(self, **kw):
        self.path = "Domain.Unlock"
        return self._request(**kw)

    def list_alias(self, **kw):
        self.path = "Domainalias.List"
        return self._request(**kw)

    def create_alias(self, **kw):
        self.path = "Domainalias.Create"
        return self._request(**kw)

    def remove_alias(self, **kw):
        self.path = "Domainalias.Remove"
        return self._request(**kw)

    def list_group(self, **kw):
        self.path = "Domaingroup.List"
        return self._request(**kw)

    def create_group(self, **kw):
        self.path = "Domaingroup.Create"
        return self._request(**kw)

    def modify_group(self, **kw):
        self.path = "Domaingroup.Modify"
        return self._request(**kw)

    def remove_group(self, **kw):
        self.path = "Domaingroup.Remove"
        return self._request(**kw)

    def change_group(self, **kw):
        self.path = "Domain.Changegroup"
        return self._request(**kw)

    def mark(self, **kw):
        self.path = "Domain.Ismark"
        return self._request(**kw)

    def remark(self, **kw):
        self.path = "Domain.Remark"
        return self._request(**kw)

    def privileges(self, **kw):
        self.path = "Domain.Purview"
        return self._request(**kw)

    def list_retrieve_email(self, **kw):
        self.path = "Domain.Acquire"
        return self._request(**kw)

    def send_retrieve_captcha(self, **kw):
        self.path = "Domain.Acquiresend"
        return self._request(**kw)

    def validate_captcha(self, **kw):
        self.path = "Domain.Acquirevalidate"
        return self._request(**kw)

    def record_type(self, **kw):
        self.path = "Record.Type"
        return self._request(**kw)

    def record_line(self, **kw):
        self.path = "Record.Line"
        return self._request(**kw)


class Record(Api):

    def __init__(self, email, password, cookie=''):
        super(Record, self).__init__(email, password, cookie=cookie)

    def create(self, **kw):
        self.path = "Record.Create"
        return self._request(**kw)

    def list(self, **kw):
        self.path = "Record.List"
        return self._request(**kw)

    def modify(self, **kw):
        self.path = "Record.Modify"
        return self._request(**kw)

    def remove(self, **kw):
        self.path = "Record.Remove"
        return self._request(**kw)

    def ddns(self, **kw):
        self.path = "Record.Ddns"
        return self._request(**kw)

    def remark(self, **kw):
        self.path = "Record.Remark"
        return self._request(**kw)

    def info(self, **kw):
        self.path = "Record.Info"
        return self._request(**kw)

    def modify_status(self, **kw):
        self.path = "Record.Status"
        return self._request(**kw)


class Monitor(Api):

    def __init__(self, email, password, cookie=''):
        super(Monitor, self).__init__(email, password, cookie=cookie)

    def list_subdomain(self, **kw):
        self.path = "Monitor.Listsubdomain"
        return self._request(**kw)

    def list_subvalue(self, **kw):
        self.path = "Monitor.Listsubvalue"
        return self._request(**kw)

    def list(self, **kw):
        self.path = "Monitor.List"
        return self._request(**kw)

    def create(self, **kw):
        self.path = "Monitor.Create"
        return self._request(**kw)

    def modify(self, **kw):
        self.path = "Monitor.Modify"
        return self._request(**kw)

    def remove(self, **kw):
        self.path = "Monitor.Remove"
        return self._request(**kw)

    def info(self, **kw):
        self.path = "Monitor.Info"
        return self._request(**kw)

    def set_status(self, **kw):
        self.path = "Monitor.Setstatus"
        return self._request(**kw)

    def history(self, **kw):
        self.path = "Monitor.Gethistory"
        return self._request(**kw)

    def desc(self, **kw):
        self.path = "Monitor.Userdesc"
        return self._request(**kw)

    def get_downs(self, **kw):
        self.path = "Monitor.Getdowns"
        return self._request(**kw)
