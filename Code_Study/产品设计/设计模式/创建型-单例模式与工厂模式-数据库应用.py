'''
    单例模式，要确保只有一个实例对象存在，以确保所有信息都从这个对象获取（类比管程）
    【系统的配置对象，线程池，减少数据库连接次数】

    想法：
    是不是每次我们使用数据库的时候都需要连接数据库呢？
    当然不是，我们可以使用单例模式来保证连接数据库只会发生一次。

    思路：

'''

import sqlite3
from flask import current_app
from flask import _app_ctx_stack as stack


class SQLite3(object):
    def __init__(self,app):
        self.app = app

    def init_app(self,app):
        app.config.setdefault('SQLITE3_DATABASE',':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        """
        连接到 sqlite 数据库
        """
        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])

    def teardown(self, exception):
        """
          关闭 sqlite 链接
        """
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        """
        单例模式在这里：使用 flask._app_ctx_stack 存放 sqlite 链接,
        每次获取数据库链接时都通过 connection 获取
        """
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db