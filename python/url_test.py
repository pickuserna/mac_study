import urlparse
url = "https://docs.python.org/2/library/urlparse.html"
url_with_query = "http://v.youku.com/v_show/id_XNDgwNzE4NzQw.html?from=s1.8-3-1.1"

split_result = urlparse.urlsplit(url_with_query)
print split_result
import os
paths = os.path.split(split_result.path)

new_url = urlparse.urljoin(url, paths[-1])
print new_url