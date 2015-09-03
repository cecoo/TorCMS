# -*- coding:utf-8 -*-
'''
Author: Bu Kun
E-mail: bukun@osgeo.cn
CopyRight: http://www.yunsuan.org
'''

import hashlib
# import peewee
from torlite.core.base_model import BaseModel
from torlite.model.core_tab import CabMember

from torlite.core import tools




class MUser(BaseModel):
    def __init__(self):
        try:
            CabMember.create_table()
        except:
            pass

    def get_by_uid(self, uid):
        try:
            return CabMember.get(CabMember.uid == uid)
        except:
            return False

    def get_by_id(self, uname):
        try:
            return CabMember.get(user_name=uname)
        except:
            return False
    def get_by_email(self, emai):
        print(emai)
        try:
            return CabMember.get(user_email = emai)
        except:
            return False

    def check_user(self, u_name, u_pass):
        tt = CabMember.select().where(CabMember.user_name == u_name).count()
        if tt == 0:
            return -1
        a = CabMember.get(user_name=u_name)
        if a.user_pass == tools.md5( u_pass) :
            return 1
        return 0

    def update_pass(self, u_name, newpass):
        entry = CabMember.update(
            user_pass= tools.md5(newpass),
        ).where(CabMember.user_name == u_name)
        entry.execute()
        return entry

    def update_info(self, u_name, newemail):

        entry = CabMember.update(
            user_email=newemail,

        ).where(CabMember.user_name == u_name)
        entry.execute()
        return entry

    def update_reset_passwd_timestamp(self, uname, timeit):

        entry = CabMember.update(
            reset_passwd_timestamp = timeit,
        ).where(CabMember.user_name == uname)
        entry.execute()
        return entry

    def update_privilege(self, u_name, newprivilege):
        print(u_name)

        entry = CabMember.update(

            privilege=newprivilege
        ).where(CabMember.user_name == u_name)
        entry.execute()
        return entry

    def insert_data(self, post_data):
        print(post_data)
        print(type(post_data['user_name'][0]))
        print(type(post_data['user_email'][0]))
        entry = CabMember.create(uid=tools.get_uuid(),
                                 user_name=post_data['user_name'][0],
                                 user_pass=hashlib.md5(post_data['user_pass'][0].encode('utf-8')).hexdigest(),
                                 user_email=post_data['user_email'][0],
                                 privilege='10000')
        return True

    def get_by_keyword(self, par2):
        return CabMember.select().where(CabMember.user_name.contains(par2))


    def delete(self, del_id):

        try:
            del_count = CabMember.delete().where(CabMember.uid == del_id)
            del_count.execute()

            return True
        except:
            return False