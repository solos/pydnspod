#!/usr/bin/python
#coding=utf-8

from pydnspod import pydnspod

if __name__ == "__main__":

    #API
    #print "请输入DNSPod帐号："
    #login_email = raw_input()
    #print "请输入帐号密码："
    #login_password = raw_input()
    #api = pydnspod.Api(login_email, login_password)
    #cookie = api.get_cookie(code)
    #print api.version()

    #User
    #user_manager=pydnspod.User(login_email, login_password)
    #print user_manager.detail()
    #print user_manager.modify(im="123456789")
    #print user_manager.modify_password(old_password="oldpassword", new_password="newpassword")
    #todo  print user_manager.modify_email()
    #print user_manager.get_verify_code(telephone="18600000000")
    #print user_manager.log()

    #Domain
    #domain_manager = pydnspod.Domain(login_email, login_password)
    #print domain_manager.set_cookie(cookie)
    #print domain_manager.create(domain="domain.name")
    #print domain_manager.list()
    #print domain_manager.remove(domain="domain.name")
    #print domain_manager.modify_status(domain="domain.name", status="disable")
    #print domain_manager.info(domain="domain.name")
    #print domain_manager.log(domain="domain.name")
    #print domain_manager.se_push(domain="domain.name", status="no")
    #print domain_manager.share(domain="domain.name", email="user@domain.name")
    #print domain_manager.list_share(domain="domain.name")
    #print domain_manager.modify_share(domain="domain.name", email="user@domain.name", mode="rw")
    #print domain_manager.remove_share(domain="domain.name", email="user@domain.name")
    #print domain_manager.transfer(domain="domain.name", email="user@domain.name")
    #print domain_manager.info(domain="domain.name")
    #print domain_manager.lock_status(domain_id=2356716)
    #print domain_manager.unlock(domain="domain.name", lock_code="748b62")
    #print domain_manager.list_alias(domain="domain.name")
    #print domain_manager.create_alias(domain_id=2356716, domain="domain.name")
    #print domain_manager.remove_alias(domain_id=2356716, alias_id=21126)
    #print domain_manager.list_group()
    #print domain_manager.create_group(group_name="testagain")
    #print domain_manager.modify_group(group_id=2235, group_name="rename_test")
    #print domain_manager.remove_group(group_id=2235)
    #print domain_manager.change_group(domain="domain.name", group_id=2237)
    #print domain_manager.mark(domain="domain.name", is_mark="yes")
    #print domain_manager.remark(domain="domain.name", remark="testapi")
    #print domain_manager.privileges(domain="domain.name")
    #print domain_manager.list_retrieve_email(domain="domain.name")
    #print domain_manager.send_retrieve_captcha(domain="domain.name")
    #print domain_manager.validate_captcha(domain="domain.name", code="code")
    #print domain_manager.get_verify_code(domain="domain.name")
    #print domain_manager.record_type(domain_grade="D_Free")
    #print domain_manager.record_line(domain="domain.name", domain_grade="D_Free")

    #Record
    #record_manager = pydnspod.Record(login_email, login_password)
    #print record_manager.set_cookie(cookie)
    #print record_manager.create(domain_id=2317346,value="1.1.1.1", record_line="默认", record_type="A")
    #print record_manager.list(domain_id=2317346)
    #print record_manager.modify(domain_id=2317346, value="2.2.2.2", record_id=16894439, record_line="默认", record_type="A")
    #print record_manager.remove(domain_id=2317346, record_id=16894439)
    #print record_manager.list(domain_id=2317346)
    #print record_manager.ddns(domain_id=2317346, record_id=16909160, record_line="默认")
    #print record_manager.remark(domain_id=2317346, record_id=16909160, remark="test")
    #print record_manager.info(domain_id=2317346, record_id=16909160)
    #print record_manager.modify_status(domain_id=2317346, record_id=16909160, status="disable")

    #Monitor
    #monitor_manager = pydnspod.Monitor(login_email, login_password)
    #print monitor_manager.set_cookie(cookie)
    #print monitor_manager.list_subdomain(domain_id=2317346)
    #print monitor_manager.list_subvalue(domain_id=2317346, subdomain="@")
    #print monitor_manager.list(domain_id=2317346)
    #print monitor_manager.create(domain_id=2317346, record_id=16909160, port=80, monitor_type="http", monitor_path="/", monitor_interval=180, points="ctc,cuc,cmc", bak_ip="pass", sms_notice="me", email_notice="me")
    #print monitor_manager.create(domain_id=2317346, record_id=16909160, port=80, monitor_type="http", monitor_path="/", monitor_interval=180, points="ctc,cuc,cmc", bak_ip="pass", sms_notice="me", email_notice="me", less_notice="no", keep_ttl="no", host="domain.name" )
    #print monitor_manager.modify(monitor_id="51fc9a20-363c-11e2-bab7-0819a6248970", port=80, monitor_type="http", monitor_path="/", monitor_interval=360, points="ctc", bak_ip="pass")
    #print monitor_manager.remove(monitor_id="51fc9a20-363c-11e2-bab7-0819a6248970")
    #print monitor_manager.info(monitor_id="e91997aa-3641-11e2-bab7-0819a6248970")
    #print monitor_manager.set_status(monitor_id="03e3b268-3643-11e2-bab7-0819a6248970", status="disabled")
    #print monitor_manager.get_status(monitor_id="03e3b268-3643-11e2-bab7-0819a6248970")
    #print monitor_manager.history(monitor_id="03e3b268-3643-11e2-bab7-0819a6248970", hours=1)
    #print monitor_manager.desc()
    #print monitor_manager.get_downs(offset=0, length=10)
    #print monitor_manager.list()

    print "请输入DNSPod帐号："
    login_email = raw_input()
    print "请输入帐号密码："
    login_password = raw_input()
    api = pydnspod.Api(login_email, login_password)
    print "请输入D令牌验证码，未开启D令牌请按回车键："
    code = raw_input()
    if code:
        cookie = api.get_cookie(code)
        print api.version()
        user_manager = pydnspod.User(login_email, login_password, cookie=cookie)
        #print user_manager.set_cookie(cookie)
        #print user_manager._cookie
        print user_manager.detail()
    else:
        api = pydnspod.Api(login_email, login_password)
        print api.version()
        user_manager = pydnspod.User(login_email, login_password)
        print user_manager.detail()
