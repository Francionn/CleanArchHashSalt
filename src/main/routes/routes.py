import os

from flask import Blueprint, request
from flask import render_template, url_for, redirect, session

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.user_login_composer import user_login_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_name_composer import user_name_composer

from src.main.forms.form_login import LoginForm
from src.main.forms.form_register import RegisterUser

from src.erros.erro_handle import handle_errors

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'presentation', 'templates')
user_route_bp = Blueprint("user_routes", __name__, template_folder=template_dir)

import logging

logger = logging.getLogger(__name__)

@user_route_bp.route('/')
@user_route_bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@user_route_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = request_adapter(request, user_login_composer())
        except Exception as exception:
            user = handle_errors(exception)
        
        if user.body["data"]:
            try:
                name = request_adapter(request, user_name_composer())
            except Exception as exception:
                name = handle_errors(exception)
            
            session['username'] = name.body['data']
            get_name = name.body['data']
            
            return redirect(url_for('user_routes.welcome', username=get_name))

    return render_template('login.html', form=form)

@user_route_bp.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = RegisterUser()
    if form.validate_on_submit():
        try:    
            user = request_adapter(request, user_register_composer())
        except Exception as exception:
            user = handle_errors(exception)
        
        if user:
            return redirect(url_for('user_routes.login'))
    
    return render_template('createacc.html', form=form) 

@user_route_bp.route('/welcome/<username>', methods=['GET'])
def welcome(username):
    if 'username' not in session or session['username'] != username:
        return redirect(url_for('user_routes.login'))

    return f'Welcome {username}'
