from tornado import web
class PageNumModule(web.UIModule):
    def render(self, pageinfo):
        return self.render_string('modules/pagenum.html', pageinfo=pageinfo)

UI_MODULES = {'pagenum': PageNumModule}
