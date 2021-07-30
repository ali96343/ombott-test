
import requests as req
import time
start_time = time.time()
NUMS=100

for _ in range(NUMS):

    resp= req.get( "http://localhost:8000/volt/X404" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/X500" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/lock" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/index" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/forms" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/modals" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/buttons" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/signXin" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/signXup" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/settings" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/dashboard" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/typography" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/transactions" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/notifications" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/upgradeXtoXpro" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/resetXpassword" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/forgotXpassword" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

    resp= req.get( "http://localhost:8000/volt/bootstrapXtables" )
    if resp.status_code != 200:
         print('error!')
         print (  resp )

print(  "volt duration: {:.2f} seconds.".format(   time.time() - start_time   ) )
