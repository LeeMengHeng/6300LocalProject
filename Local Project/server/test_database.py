import pymysql
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

num_list = []

sig_door = 'SMS_464116180'
sig_window = 'SMS_464096123'

access_key_id = "LTAI5tK9NnCjUCgDuDrbsFYo"
access_key_secret = "yK9iLuOYSuTzyo28XwPcPJCQ8fIrpa"

client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')

def send_message(phone_num, sig):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone_num)
    request.add_query_param('SignName', "room")
    request.add_query_param('TemplateCode', sig)
    request.add_query_param('TemplateParam', "{\"code\":\"12345\"}")

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))



link=pymysql.connect(
    host = 'gz-cynosdbmysql-grp-6ml1wj8z.sql.tencentcdb.com'
    ,user = 'root'
    ,passwd='652398Aq'
    ,port= 27898
    ,db='project'
    ,charset='utf8'
)

cur = link.cursor()
sql="SELECT phone_number FROM table_user WHERE phone_number is not null"
cur.execute(sql)
data = cur.fetchall()
for i in data:
    num_list.append(i[0])
cur.close()
link.close()

def send_sms(mobile, content):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

        data = {'account':'C76810478',
                'password':'423a2a1d5e4e45433c6c846e707aa85a',
                'mobile':mobile,
                'content':content
                }
        response = requests.post('https://106.ihuyi.com/webservice/sms.php?method=Submit', headers=headers, data=data)
        print(response.content.decode())


for num in num_list:
    send_message(num, sig_window)
    
  

