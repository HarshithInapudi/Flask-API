# Flask-API

install Python 3.8.0 

install required packages using pip.

pip install -r requirements.txt 

--On windows-- install redis from https://github.com/microsoftarchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.msi 

you can run redis from C:\Program Files\Redis\redis-server.exe

once redis is up and running, run the api using

python run.py

use the credentials(username as username, auth_id as password) from the sql dump file(https://gist.github.com/paragradke/a629bb4e332125b1388390fcc156cfcd) to login.


API /inbound/sms/:

API behaviour:

1- If required parameter is missing, then it returns an error: "required parameter is missing"

2- If the ‘to’ parameter is not present in the phone_number table for the specific account 
used for the basic authentication then it returns an error: "to parameter not found"

3- When text is STOP or STOP\n or STOP\r or STOP\r\n
- The ‘from’ and ‘to’ pair will be stored in cache as a unique entry and they
 expire after 4 hours.

 
 API /outbound/sms/:
 
 API behaviour:
 
1- If required parameter is missing, then it returns an error: "required parameter is missing"
 
2- If the pair ‘to’, ‘from’ matches any entry in cache (STOP), return an error “sms from <from> to <to> blocked by STOP request”.
  
3- If the ‘from’ parameter is not present in the phone_number table for the specific account
 used for the basic authentication then it returns an error: "from parameter not found"
