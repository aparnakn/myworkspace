from notes2.bottle import *
from pprint import pprint
import time, os
import algebra, monkey_patching

@get('/')
def welcome():
   # pprint(dict(request.headers))
    response.set_header('Vary', 'Accept')
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello'

@get('/now')
def time_microservice():
    response.content_type = 'text/plain'
    return time.ctime()

@get('/upper/<word>')
def uppercase_microservice(word):
    response.content_type = 'text/plain'
    return word.upper()

@get('/area/circle')
def circle_area_microservice():
    pprint(dict(request.query))
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError:
        return 'Error: expected a float radius'
    area = algebra.area(radius)
    return dict(service=request.path, radius=radius, area=area)

######### File server ##################################################

files_template = '''\
<h1> List of files in <em> notes2 </em> directory </h1>
<hr>
<ol>
     % for filename in sorted(files):
       <li> <a href="files/{{ filename }}"> {{ filename }} </a> </li>
     % end
</ol>
'''

@get('/files')
def show_file_service():
    files = os.listdir('notes2')
    return template(files_template, files=files)

@get('/files/<filename>')
def file_service(filename):
    return static_file(filename, root='./notes2')

############### quadratic equation service ##############################


@get('/quadratic')   #http://localhost:8080/quadratic?a=25&b=80&c=4
def quadratic_microservice():
    pprint(dict(request.query))
    try:
        a = float(request.query.get('a', '0.0'))
        b = float(request.query.get('b', '0.0'))
        c = float(request.query.get('c', '0.0'))
    except ValueError:
        return dict(error= 'expected float values for a, b and c')
    x1, x2 = algebra.quadratic(a,b,c)
    response.set_header('Vary', 'Accept')
    response.set_header('Cache-Control', 'max-age=60')
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return template('notes2/quadratic.tpl', a=a, b=b, c=c, x1=x1, x2=x2)
    return dict(service=request.path, a=a, b=b,c=c, 
                x1 = dict(real = x1.real, imag=x1.imag),
                x2 = dict(real = x2.real, imag=x2.imag))

if __name__=='__main__':
    run(host='localhost', port=8080)
