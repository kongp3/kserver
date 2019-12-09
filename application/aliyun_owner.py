# -*- coding: utf-8 -*-
from config import ALIYUN_ROOT


class AliyunOwner(object):
    def __init__(self):
        pass

    def ssswitch(self, flag):
        if flag:
            profile_root = ALIYUN_ROOT + 'enable'
        else:
            profile_root = ALIYUN_ROOT + 'disable'
