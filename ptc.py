# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print('->', a, '>', v)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print('->', a, '>', v)
html = ''
n = int(input())
for i in range(n):
    html += input().rstrip() +'\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()