from mkdocs.plugins import BasePlugin
import json
import os
import re


class MarkdownExportPlugin(BasePlugin):

  data = list()


  def on_page_content(self, html, page, config, files):

    breadcrumb = ''
    for item in reversed(page.ancestors[:-1]):
      breadcrumb += item.title + ' > '
    breadcrumb += page.title

    if page.ancestors:
      topic = page.ancestors[-1].title
    else:
      topic = page.title

    nohtml = re.compile(r'<[^>]+>')
    trim = re.compile(r'[\n\t ]{2,}')

    for part2 in html.split("<h2 id="):
      h2 = re.match(r'^"([^"]+)">([^<]+)', part2)

      if h2:
        for part3 in part2.split("<h3 id="):
          h3 = re.match(r'^"([^"]+)">([^<]+)\<a[^>]+\>#\<\/a\>\<\/h3\>', part3)

          if h3:
            self.data.append({
              'url': page.abs_url + '#' + h3.group(1).strip('"'),
              'topic': topic,
              'title': breadcrumb + ' > ' + h2.group(2) + ' > ' + h3.group(2),
              'content': trim.sub(' ', nohtml.sub(' ', '<h3 id=' + part3))
            })
          else:
            self.data.append({
              'url': page.abs_url + '#' + h2.group(1).strip('"'),
              'topic': topic,
              'title': breadcrumb + ' > ' + h2.group(2),
              'content': trim.sub(' ', nohtml.sub(' ', '<h2 id=' + part3))
            })
      else:
        self.data.append({
          'url': page.abs_url,
          'topic': topic,
          'title': breadcrumb,
          'content': trim.sub(' ', nohtml.sub(' ', part2))
        })


    return html


  def on_post_build(self, config):

    path = os.path.join(os.getcwd(), 'export.json')

    if os.path.exists(path):
      os.remove(path)

    json.dump(self.data, open(os.path.join(path), "w"), ensure_ascii=False, indent=4)
