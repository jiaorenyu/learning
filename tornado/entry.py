class Entry(tornado.web.UIModule):
    def embedded_css(self):
        return ".entry { margin-bottom: 1em; }"
    def render(self, entry, show_comments=False):
        return self.render_string(
                "module-entry.html", show_comments=show_comments)
