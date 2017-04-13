"Introduction to the bottle templating system"
# There are many templating engines: bottle cheetah mako jinga2 django

from notes2.bottle import template

family = '''\
The {{ lastname.title() }} Family
{{ "=" * (11 + len(lastname)) }}
% for i, name in enumerate(first_names, start=1):
  {{ i }}. {{ name.title() }}
% end
'''

family_html = '''\
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="utf-8">
   <title> {{ lastname.title() }} Family </title>
</head>
<body>
<h1> The {{ lastname.title() }} </em> Family </h1>
<hr>
<ol>
 % for name in first_names:
   <li> {{ name.title() }} </li>
 % end
</ol>
</body>
</html>
'''

#print template(family_html, lastname='simpsons',
#               first_names = 'homer marge bart lisa maggie'.split())

def family_from_strings(s):
    fields = s.split()
    return dict(lastname=fields[0], first_names=fields[1:])
