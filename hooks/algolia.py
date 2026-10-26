# Algolia export for MkDocs
#
# Writes the search records of all pages to "<site_dir name>.json"
# in the current working directory after the build.

import json
import os
import re


data = list()
nohtml = re.compile(r'<[^>]+>')
trim = re.compile(r'[\n\t ]{2,}')


def on_pre_build(config):

  data.clear()


def on_page_content(html, page, config, files):

  breadcrumb = ''
  for item in reversed(page.ancestors[:-1]):
    breadcrumb += item.title + ' > '
  breadcrumb += page.title

  if page.ancestors:
    topic = page.ancestors[-1].title
  else:
    topic = page.title

  for part2 in html.split("<h2 id="):
    h2 = re.match(r'^"([^"]+)">([^<]+)', part2)

    if h2:
      for part3 in part2.split("<h3 id="):
        h3 = re.match(r'^"([^"]+)">([^<]+)\<a[^>]+\>#\<\/a\>\<\/h3\>', part3)

        if h3:
          data.append({
            'url': page.abs_url + '#' + h3.group(1).strip('"'),
            'topic': topic,
            'title': breadcrumb + ' > ' + h2.group(2) + ' > ' + h3.group(2),
            'content': trim.sub(' ', nohtml.sub(' ', '<h3 id=' + part3))
          })
        else:
          data.append({
            'url': page.abs_url + '#' + h2.group(1).strip('"'),
            'topic': topic,
            'title': breadcrumb + ' > ' + h2.group(2),
            'content': trim.sub(' ', nohtml.sub(' ', '<h2 id=' + part3))
          })
    else:
      data.append({
        'url': page.abs_url,
        'topic': topic,
        'title': breadcrumb,
        'content': trim.sub(' ', nohtml.sub(' ', part2))
      })

  return html


def on_post_build(config):

  path = os.path.join(os.getcwd(), os.path.basename(os.path.normpath(config.site_dir)) + '.json')

  with open(path, 'w') as fh:
    json.dump(data, fh, ensure_ascii=False, indent=4)
