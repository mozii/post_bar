# -- coding: utf8 --
import web
from config.config import render
from models import post_model

class create:
    def GET(self):
        form = post_model.form
        title = '创建主题'
        return render.create_post(form, title)
    
    def POST(self):
        form = post_model.form
        if not form.validates():
            return render.create(form, '创建失败')
        post_model.insert(form.d.title, form.d.content)
        raise web.seeother('/')