#!/usr/bin/env python

app_header= """
import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A, I
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.factories import ActionFactory, Inject
from py4web.utils.param import Param
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV
from py4web.utils.param import Param
from .settings import SESSION_SECRET_KEY

from .common import db, session, T, flash, cache, authenticated, unauthenticated, auth
"""

NUMS_CTRL=10

from string import Template
import uuid
import base64

ctrl_text = """
@action('ctrl_act$CTRL_ACT')
def ctrl_nm$CTRL_NM():
    # mynum: $NUM
    return 'ctrl_act$CTRL_ACT' 
    #return 'hello_world_$RET' 
"""




# --------------------------------------------- mk_app -------------------------------------------------------------
t = Template( ctrl_text )

ctrl_file = 'controllers.py'
request_file = 'test_minus_yatl.py'

def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return str(r_uuid.replace(b'=', b'') )

rtr_list=[]
 
def mk_app():
    with open( ctrl_file, 'w' ) as f :
       f.write (app_header)
       for e in range(NUMS_CTRL):
           some_act = str(uuid.uuid4())
           some_ctrl = str( uuid.uuid4().hex )
           rtr_list.append(some_act)
           f.write (t.substitute({'CTRL_ACT' : some_act , 'CTRL_NM': some_ctrl, 'RET':e,  'NUM': e }))


# ---------------------------------------------- mk_test -----------------------------------------

r_begin="""
import requests as req
import time
start_time = time.time()

OK_CNT = 0

"""

r_end="""
print(  "duration: {:.2f} seconds.".format(   time.time() - start_time   ) )
print ('OK_CNT: ',OK_CNT)

"""


r_text="""
resp= req.get( "http://localhost:8000/minus_yatl/ctrl_act$CTRL_ACT" )
get_suffix = 'ctrl_act$CTRL_ACT'
#print (resp.text)
if resp.text != get_suffix:
   print ('routing error!')
else: 
#   print ('equal !')
    OK_CNT += 1


if resp.status_code != 200:
     print('error!')
     print (  "http://localhost:8000/minus_yatl/ctrl_act$CTRL_ACT" )

"""
r = Template( r_text  )

def mk_test():
    with open( request_file, 'w' ) as f :
       f.write( r_begin )
       for e in range(NUMS_CTRL):
           f.write (r.substitute({'CTRL_ACT' : rtr_list[e], }))
           f.write('\n')
       f.write( r_end )



mk_app()
mk_test()
