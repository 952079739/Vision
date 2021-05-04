import json
import os

from flask import Blueprint, request, render_template, url_for, jsonify, redirect, session
from utils.func import create
from utils.music_list import getMusic
from db_sql import *

user = Blueprint('user', __name__, url_prefix="/user")


@user.route('/logout', methods=['GET'])
def logout():
    return render_template('login.html')


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            password_two = data['password_two']
            if len(username) > 0 and len(password) > 0 and len(password_two) > 0:
                user = select_user_name(username)
                if user is None:
                    if password == password_two:
                        filepath = '/home/li/桌面/VisionPlayer/static/{}/upload'.format(username)
                        filepath1 = '/home/li/桌面/VisionPlayer/static/{}/video'.format(username)
                        add_user(username, password, filepath)
                        msg = create(filepath)
                        msg = create(filepath1)
                        # return redirect(url_for('user.login'))
                        return jsonify({'msg': msg})
                    else:
                        return jsonify({'msg':"密码不一致"})
                else:
                    # return jsonify(type_information='False')
                    return jsonify({'msg': "用户名存在"})
            return jsonify({'msg': "请输入密码或用户名"})


# @wolfer test
# 登录页面,传输数据为json,类型为POST
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password']
            users = select_user(username, password)
            if users is not None:
                session['username'] = username
                return jsonify({'msg': "success"})
            else:
                return jsonify(typ_inforamtion='请注册后再登录')
        return jsonify({'msg': "请输入用户名或密码"})


@user.route('/update_password', methods=['POST', 'GET'])
def update_user_one():
    if request.method == 'GET':
        return render_template('update_p.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            username = data['username']
            password = data['password1']
            password2 = data['password2']
            user = select_user_name(username)
            if user is not None:
                if password == password2:
                    update_user_password(username, password)
                    return jsonify({'msg': "success"})
                return jsonify({'msg':"输入密码不一致"})
            return jsonify({'msg': "请输入新密码"})


@user.route('/update_name', methods=['POST', 'GET'])
def update_user_two():
    if request.method == 'GET':
        return render_template('update_n.html')
    if request.method == 'POST':
        data = request.form.get('data')
        if data is not None:
            data = json.loads(data)
            old_username = data['old_username']
            new_username = data['new_username']
            user = select_user_name(old_username)
            if user is not None:
                update_user_name(old_username, new_username)
                old_file1 = '/home/li/桌面/VisionPlayer/static/{}'.format(old_username)
                new_file1 = '/home/li/桌面/VisionPlayer/static/{}'.format(new_username)
                os.rename(old_file1, new_file1)
                session['username'] = new_username
                return jsonify({'msg': "success"})
        return jsonify({'msg': "请输入用户名"})


@user.route('/user_info', methods=['GET'])
def user_info():
    username = session['username']
    filepath = 'static/{}/upload'.format(username)
    music_list = getMusic(filepath)
    return render_template('movie_info.html', musicList=music_list)

#
# @user.route('/movie_info', methods=['POST'])
# def movie_info():
#


@user.route('/info', methods=['POST'])
def info():
    username = session['username']
    user = select_user_name(username)
    user_information = {
        'user_name': user.user_name,
        'user_email': user.user_email
    }
    return jsonify(user_information)