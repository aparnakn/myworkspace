import os
from subprocess import Popen, PIPE, check_output

def graphviz(dot):
    p = Popen(['dot', '-Tsvg'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    text, errmsg = p.communicate(input=dot)
    svg_start = text.index('<svg ')
    return text[svg_start:]

if __name__=='__main__':


    hettingers = '''\
    digraph {
       raymond -> matthew;
       rachel -> matthew;
    }
    '''
    #This wasy the simplest, slowest and the least secure
    #and has least integration 
    r = os.system('netstat -s > temp.txt')
    print r

    with open('temp.txt') as f:
        s = f.read()

    print s[:100]

 #this captures the string directly without
#creating a file. It is much faster and integrates better with
#python but creates a shell
    s = check_output('netstat -s', shell=True)
    print s[:100]


#This way integrates well with python, doesnt create a file
#doesnt create a shell and very fast
#calls netstat directly , no bash, it is secure
    s = check_output(['netstat', '-s'])
    print s[:100]


    p = Popen(['dot', '-Tsvg'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    text, errmsg = p.communicate(input=hettingers)
    print 'Error message:', errmsg
    print 'Text'
    print text
