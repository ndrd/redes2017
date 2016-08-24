
class ChatWrapper:
    _cur_id = None

    def __init__(self, webView):
        self.webView = webView
        self.contentHtml = ''

    def _ADD(self, content):
        self.contentHtml += content
        self.webView.setHtml(self.contentHtml)

    def clear(self):
        self.webView.setHtml('')

    def append_message(self, message):
        html = '<div id="message">'
        html += '<strong>Name</strong>'
        html += '<span class="message">{message}</span>'.format(
            message=message
        )
        html += '/<div>'
        self._ADD(html)
