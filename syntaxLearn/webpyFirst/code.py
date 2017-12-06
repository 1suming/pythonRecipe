#-*_coding:utf-8_*_
import web

render=web.template.render('templates/')
urls=(
      '/','index')

class index:
    def GET(self):
        #name='Bob'
        i=web.input(name=None)
        return render.hello(i.name)
    
if __name__=='__main__':
    app=web.application(urls,globals())
    app.run()
    