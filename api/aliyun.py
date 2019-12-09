# -*- coding: utf-8 -*-
import json
from flask import request, jsonify, redirect
from flask import render_template

from config.common import app

from application.aliyun_owner import AliyunOwner

'''为公众号支付提供h5页面'''


@app.route('/aliyun', methods=['GET'])
def aliyun_index(**kwargs):
    # return render_template('aliyun.html', host=WEB_HOST)
    return render_template('aliyun.html')


@app.route('/ssswitch', methods=['POST'])
def aliyun_ssswitch(**kwargs):
    flag = request.values.get("flag")
    kfm = AliyunOwner()
    kfm.ssswitch(flag)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

