import MySQLdb
import web
from web import db

"""
官网demo测试webpy环境搭建
"""

render = web.template.render('Template')

urls = (
    # 顺序很重要
    # 'article', 'GetArticle'
    '/index', 'Index',
    '/blog/\d+', 'Blog',
    '/(.*)', 'Hello'      # 匹配所有，放到所有url最后面，放前面出错
)
app = web.application(urls, globals())


class Index:

    # 所有类中，get和post方法必须大写
    def GET(self):
        # 获取数据类型
        query = web.input()
        return query


class Blog:
    def POST(self):
        # 获取表单类型,
        data = web.input()
        return data

    def GET(self):
        # 请求头获取
        return web.ctx.env


class Hello:
    def GET(self, name):
        # 如果不使用模板则用下面语句返回
        # return open(r"Template/index.html")

        # 如果使用模板
        return render.index(name)


class GetArticle:
    def GET(self):

        print('获取文章的方法')
        conn = MySQLdb.connect(host='localhost', user='root', password='root',
                               db='webpy', port=3306, coursorclass=MySQLdb.cursors.Dictcursor)
        cur = conn.cursor()
        cur.execute('select * from t_article')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print(r)
        return render.article(r)


if __name__ == "__main__":
    app.run()