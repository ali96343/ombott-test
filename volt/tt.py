#!/usr/bin/env python

import os,sys,re
from string import Template


def file2data( fnm  ):
    if not os.path.isfile(fnm):
       sys.exit('cant find {fnm}')
    with open(fnm, 'rb') as f:
        data=f.read()
    return data


data=  file2data( 'controllers.py'  ) 
#action('X404', method=["GET", "POST"] )
ll= re.findall( b'\@action\(\'(.*?)\', method=\[',  data, re.MULTILINE  )
#ll= re.findall( b'Template\(\'(.*?\.html)\',', data, re.MULTILINE  )
print (ll)

# -------------------------------------------------------
app_header = '########'

r_begin="""
import requests as req
import time
start_time = time.time()
NUMS=100

for _ in range(NUMS):
"""

r_end="""
print(  "$APP duration: {:.2f} seconds.".format(   time.time() - start_time   ) )
"""
r_end = Template( r_end  )

app_name=os.getcwd().split(os.sep)[-1]
print (app_name)


r_text="""
    resp= req.get( "http://localhost:8000/$CTRL_ACT" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )
"""
r = Template( r_text  )


test_file = 'r-test.py'
def mk_app():
    with open( test_file, 'w' ) as f :
       f.write (r_begin)
       for e in ll:
           if e.startswith(b'api'):
                print (e)
                continue
           xx= f"{app_name}/{e.decode('utf8')}" 
           f.write (r.substitute({'CTRL_ACT' : xx }))
           #f.write (t.substitute({'CTRL_ACT' : e, 'CTRL_NM': e, 'RET': e }))
       f.write(r_end.substitute({ 'APP': app_name }))

mk_app()
