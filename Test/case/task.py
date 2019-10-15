
----111登陆注册修改密码
-注册用户
http://192.168.0.185:7700/auth/register_form/
post
req
phonenum
password
name
secutity_code
resp{
    "code": 3004,
    "detail": "验证码错误"
}

-短信修改验证码

http://192.168.0.185:7700/auth/change_pwd_msg/
post
req
tel   pwd  secutity
resp

{
    "code": 3035,
    "detail": "手机号未注册"
}

-用户名和密码登录
http://192.168.0.185:7700/auth/signin_form/
token
req
username =admin  password=123456  type=password   security_code=1234
resp
{
    "warn_status": 0,
    "detail": "登陆成功",
    "username": "admin",
    "code": 2000,
    "user_id": 0,
    "tk": "2a0f2369950569ccba4c43f7250fc3e85fbb2ca81f29b39f6cbdb587"
}
-token检测  是否有效
http://192.168.0.185:7700/auth/token/
req token=cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5
resp{
    "code": 2000,
    "detail": "token检测成功",
    "role": 0
}


----222 短信模块
#注册 登录 修改密码

---发送短信验证
/auth/sms/digits/

id=1注册账号，id=2修改密码，id=0用户登录
req
 id =1 tel=13693653825

resp

注册返回
{
    "code": 2000,
    "detail": "验证码发送成功"
}

----绑定手机号
msg_type=1绑定手机号,msg_type=0解除手机绑定
http://192.168.0.185:7700/user/auth_send_bind_msg/

query
token
body：


pthon_num   13692653825
msg_type   1

resp


{
    "code": 500,
    "detail": "服务器内部错误"
}

--3333用户管理

#获取随机用户名
url=http://192.168.0.185:7700/user/random_username/
get
resp


{
    "code": 2000,
    "detail": "访问成功",
    "username": "userti8ujb"
}

#创建用户名
http://192.168.0.185:7700/user/auth_create_user/

name=ceshi
username=test01
resp -


{
    "code": 2000,
    "password": "7582695",
    "detail": "新建成功",
    "username": "test01",
    "change_time": 1568711160.0559604
}


#修改用户状态
/user/auth_change_status/
method   post

req
user_id=2 user_status=1
（user_status=1为通过审核并启用user_status=0为禁用）
resp
{
    "code": 2000,
    "detail": "操作成功",
    "change_time": 1568711902.346937
}


#修改用户角色
/user/auth_role/
http://192.168.0.185:7700/user/auth_role/
method  post
resq
user_id=2  role=2
(role=1为manager，role=2为controller，role=3为inspector,role=4为visitor)
resp


{
    "code": 2000,
    "detail": "操作成功",
    "change_time": 1568712324.2751932
}


#检验超级管理员密码
url =http://192.168.0.185:7700/user/check_superuser_password/
body   password =123456
post
resp

{
    "code": 2000,
    "expiration_time": 1568712616,
    "detail": "验证成功",
    "identification_code": "89e981896c21cd17eb23138d5b79c59bcc1612b3a2ad51bc20677bf4"
}

#重置用户密码
get
http://192.168.0.185:7700/user/auth_change_user/?user_id=1&identification_code=89e981896c21cd17eb23138d5b79c59bcc1612b3a2ad51bc20677bf4

resp
{
    "code": 3416,
    "detail": "管理员验证失败，请重新输入密码验证"
}



#查询所有用户
/user/auth_opt/

#查找单个用户
/user/auth_single/{user_id}

#重置用户姓名
http://192.168.0.185:7700/user/auth_change_name/

req   name =ceshi003
       user_id=2
resp

{
    "code": 2000,
    "detail": "修改成功",
    "change_time": 1568713803.1420999
}

----4444个人中心
#密码修改个人密码
/auth/personage_change_pwd/
http://192.168.0.185:7700/auth/personage_change_pwd/
post
old_password
new_password

resp
{
    "code": 3029,
    "detail": "原密码错误"
}

#短信修改个人密码
http://192.168.0.185:7700/auth/personage_change_pwd_msg/
post
body
pwd   security  phone_num
resp
{
    "code": 3415,
    "detail": "您未绑定手机号"
}


#修改个人用户名
http://192.168.0.185:7700/auth/change_username/personage_change_username/
post
resq
new_username=123456

respo
{
    "code": 2000,
    "detail": "修改成功",
    "tk": "2efc7bdcac959d6acd41a9defc6b7d4b6bee8f7e6cc1dc0e6077ac21"
}

#个人主页
url=http://192.168.0.185:7700/auth
resq ：token =cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5
resp
{
    "user_info": {
        "head_pic": null,
        "role": 0,
        "phone_num": null,
        "name": null,
        "username": "admin"
    },
    "code": 2000,
    "detail": "访问成功"
}


---系统相关操作
#查看挡墙用户的access_token列表
/user/access_token/

---77777任务管理

#查询所有任务
url=http://192.168.0.185:7700/tasks/task/task_type_detail/?token=7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4&task_type=&typeTk=token&
header:
Accept: application/json, text/plain, */*
Authorization: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
Origin: http://192.168.0.185
Referer: http://192.168.0.185/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36


param :
token: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
task_type:
typeTk: token


#创建任务
url= http://192.168.0.185:7700/tasks/task/?token=7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
hearders=
Accept: application/json, text/plain, */*
Authorization: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.0.185
Referer: http://192.168.0.185/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36

param
token: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
data=
task_type: 201
dst_node: 1
attitude: 1
target_vehicle: 12


#任务操作  克隆任务
url= http://192.168.0.185:7700/tasks/task/task_exe_status/

methond :POST
heard =Accept: application/json, text/plain, */*
Authorization: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.0.185
Referer: http://192.168.0.185/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36

from data = task_id: 1644816047762571265
action: 11
action_code: 0
token: 7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4

respones ：{"code":2000,"detail":"重新执行（克隆）操作发送成功"}


# 查询单个任务
任务id 1644817036984975361
url:http://192.168.0.185:7700//tasks/task/?task_id=1644820112523395073
method:get
params
token:7c2ded444e30e477ff2a25c92552d9b18c99ccd6f1335448661f85b4
access_token :

#查询单个子任务
url== /tasks/task/sub_task/{sub_task_id}

#查询排队状态任务

URL=/tasks/task/wait/
method :get
headers  :

http://192.168.0.185:7700/tasks/task/await_task_setting/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600

#查询任务队列
/tasks/task/execute_queue/
method   get
http://192.168.0.185:7700/tasks/task/execute_queue/?page=1&order=desc&token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&task_status=execute_queue&urtType=execute_queue&per_page=10&start_time=1568649600&end_time=1568686366.762&offset=0&limit=30&

#查询近期完成任务
url=http://192.168.0.185:7700/tasks/task/complete/?page=1&order=desc&token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&task_status=complete&urtType=complete&per_page=10&start_time=1568649600&end_time=1568686458.28&offset=0&limit=30&
method  get


#查询历史任务
/tasks/task/history/
url =http://192.168.0.185:7700/tasks/task/history/?page=1&order=desc&token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&task_status=history&urtType=history&per_page=10&start_time=1568649600&end_time=1568686355.023&offset=0&limit=30&

#   未找到接口
#   查看单个任务  查看符合任务子任务列表  查看单个任务
#   查找单车排队任务&查询单车正在执行任务 &查询单车已完成任务

#获取任务类型明细
/tasks/task/task_type_detail/
url =http://192.168.0.185:7700/tasks/task/task_type_detail/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&task_type=&typeTk=token&

#低电量自动充电设置
/tasks/task/condition_task/
method post
data
started: 1
low_power: 90
max_power: 95

url=http://192.168.0.185:7700/tasks/task/condition_task/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600

前提需要正在执行中任务  构建任务
#一键暂停
Request URL: http://192.168.0.185:7700/tasks/task/task_exe_status/
Request Method: POST

form data
task_id: 1644888440495407105
action: 1
action_code: 12
token: bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600
关联
form data  一键执行
task_id: 1644888440495407105
action: 2
action_code: 11
token: bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600


#新建模版
/tasks/task_template/template_manager/
Content-Type	application/x-www-form-urlencoded	是
token		是
access_token		是
Body:
参数名称	参数类型	是否必须	示例	备注
task_template_name	T文本	是

ignore_sub_task_error	T文本	是
0

该值只能为0或1，1表示忽略子任务失败，0表示不忽略

task_template_task_list	T文本	是
[{"task_type": 201, "dst_node": 2}, {"task_type": 304, "dst_node": 1}]

#新增需求还未完成  模板任务的子任务列表

- #设置自定义任务自动完成   未找到

#设置车辆闲置任务
Status Code: 200 OK
Request URL: http://192.168.0.185:7700/tasks/task/await_task_setting/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600
Request Method: POST

form data
started: 1
await_time: 10
token: bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600

---8车辆管理

#查看车辆详细信息

Request URL: http://192.168.0.185:7700/auth/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&
Request Method: GET
Status Code: 200 OK

token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600

Request URL: http://192.168.0.185:7700/data/vehicles/?page=1&order=desc&register_status=0&token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600&per_page=10&
Request Method: GET
Status Code: 200 OK


#取消注册车辆
Request URL: http://192.168.0.185:7700/data/vehicles_regist/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600
Request Method: POST
Status Code: 200 OK

vehicles_id=30&register_status=0

#注册车辆信息
Request URL: http://192.168.0.185:7700/data/vehicles_regist/?token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600
Request Method: POST
Status Code: 200 OK

form data

vehicles_id: 30
register_status: 1


#9999999地图管理
method get
header token=bbba21bb3fe6a14c87569e36cd5e3d9a4557617f530d7035ce413600
http://192.168.0.185:7700/maps/current_map/

-获取png文件
get
token=
http://192.168.0.185:7700/maps/current_map/map_png/

-获取restrict  （限定 约束）
/maps/current_map/restrict/
get

-获取agv_graph
http://192.168.0.185:7700/maps/current_map/agv_graph/
method   get
--提交agv_graph
http://192.168.0.185:7700/maps/current_map/agv_graph/
post
map_id:
graoh:

--获取anchors
/maps/current_map/anchors/
get
hearders   token
resp
{
    "code": 2000,
    "detail": "请求成功",
    "anchors": "[]"
}

--获取poi
http://192.168.0.185:7700/maps/current_map/poi/
get
resp


{
    "poi": "{\"version\": \"1.0.0\", \"encoding\": \"utf-8\", \"poi_info\": [{\"name\": \"新位置\", \"position\": {\"x\": -13.9926, \"y\": 0.40386, \"yaw\": 2.84066}, \"tags\": []}, {\"name\": \"新位置 1\", \"position\": {\"x\": -0.2, \"y\": -0.15, \"yaw\": 0.0}, \"tags\": []}], \"charge_points_info\": [], \"groups\": {}}",
    "code": 2000,
    "detail": "请求成功"
}
---获取agv_graph的edges
http://192.168.0.185:7700/maps/current_map/agv_graph/nodes/
get
resp
{
    "code": 2000,
    "count_node_id": 33,
    "detail": "查询成功",
    "nodes": [
        {
            "is_singular": 0,
            "node_id": 0,
            "directed": 0,
            "x": -0.561,
            "reference_count": 4,
            "name": "结构点0",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.949,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 1,
            "directed": 0,
            "x": -0.561,
            "reference_count": 3,
            "name": "结构点1",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -0.218,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 2,
            "directed": 1,
            "x": -14.039,
            "reference_count": 1,
            "name": "606 前台",
            "yaw": 0,
            "navigation_feature": 1,
            "node_type": 12,
            "y": -0.027,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 3,
            "directed": 0,
            "x": 6.478,
            "reference_count": 3,
            "name": "结构点3",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.949,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 4,
            "directed": 0,
            "x": 6.478,
            "reference_count": 2,
            "name": "结构点4",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -3.511,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 5,
            "directed": 1,
            "x": 7.617,
            "reference_count": 2,
            "name": "601 前台",
            "yaw": 0,
            "navigation_feature": 1,
            "node_type": 12,
            "y": -2.411,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 6,
            "directed": 1,
            "x": -0.561,
            "reference_count": 1,
            "name": "财务室",
            "yaw": 1.5708,
            "navigation_feature": 1,
            "node_type": 12,
            "y": 2.274,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 7,
            "directed": 0,
            "x": 11.668,
            "reference_count": 3,
            "name": "结构点7",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.02,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 8,
            "directed": 0,
            "x": 14.514,
            "reference_count": 2,
            "name": "结构点8",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.02,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 9,
            "directed": 0,
            "x": 10.213,
            "reference_count": 3,
            "name": "结构点9",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.02,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 11,
            "directed": 0,
            "x": 10.213,
            "reference_count": 1,
            "name": "结构点11",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": 1.665,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 12,
            "directed": 0,
            "x": 11.668,
            "reference_count": 1,
            "name": "结构点12",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -3.511,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 13,
            "directed": 0,
            "x": 10.213,
            "reference_count": 2,
            "name": "结构点13",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": 0.238,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 14,
            "directed": 0,
            "x": 16.203,
            "reference_count": 1,
            "name": "结构点14",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -1.802,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 15,
            "directed": 0,
            "x": -0.561,
            "reference_count": 2,
            "name": "结构点15",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -8.435,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 16,
            "directed": 0,
            "x": -0.561,
            "reference_count": 1,
            "name": "结构点16",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -11.101,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 17,
            "directed": 0,
            "x": -4.026,
            "reference_count": 2,
            "name": "结构点17",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.949,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 18,
            "directed": 0,
            "x": -6.915,
            "reference_count": 1,
            "name": "结构点18",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.949,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 19,
            "directed": 0,
            "x": 10.213,
            "reference_count": 1,
            "name": "结构点19",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.949,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 20,
            "directed": 0,
            "x": 11.668,
            "reference_count": 2,
            "name": "结构点20",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.773,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 23,
            "directed": 0,
            "x": 12.683,
            "reference_count": 2,
            "name": "结构点23",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.02,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 24,
            "directed": 0,
            "x": 13.721,
            "reference_count": 2,
            "name": "结构点24",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -2.02,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 25,
            "directed": 0,
            "x": 19.084,
            "reference_count": 1,
            "name": "结构点25",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -3.223,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 26,
            "directed": 0,
            "x": 21.561,
            "reference_count": 1,
            "name": "结构点26",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -3.223,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 27,
            "directed": 0,
            "x": 14.572,
            "reference_count": 1,
            "name": "结构点27",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.015,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 28,
            "directed": 0,
            "x": 16.114,
            "reference_count": 3,
            "name": "结构点28",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.015,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 29,
            "directed": 0,
            "x": 17.508,
            "reference_count": 3,
            "name": "结构点29",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.015,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 30,
            "directed": 0,
            "x": 18.995,
            "reference_count": 1,
            "name": "结构点30",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.015,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 31,
            "directed": 0,
            "x": 16.114,
            "reference_count": 1,
            "name": "结构点31",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -5.25,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 32,
            "directed": 0,
            "x": 17.508,
            "reference_count": 2,
            "name": "结构点32",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.457,
            "tags": []
        },
        {
            "is_singular": 0,
            "node_id": 33,
            "directed": 0,
            "x": 17.508,
            "reference_count": 1,
            "name": "结构点33",
            "yaw": 0,
            "navigation_feature": 0,
            "node_type": 10,
            "y": -6.992,
            "tags": []
        }
    ]


--获取agv_graph的edges
/maps/current_map/agv_graph/edges/
    method   get
resp
{
    "count_edges_id": 285,
    "code": 2000,
    "detail": "查询成功",
    "edges": [
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 13.479,
            "line_id": 54,
            "edge_type": 1,
            "end_node_id": 1,
            "edge_id": 114,
            "start_node_id": 2
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 13.479,
            "line_id": 54,
            "edge_type": 1,
            "end_node_id": 2,
            "edge_id": 115,
            "start_node_id": 1
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 5.731,
            "line_id": 55,
            "edge_type": 1,
            "end_node_id": 0,
            "edge_id": 116,
            "start_node_id": 1
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 5.731,
            "line_id": 55,
            "edge_type": 1,
            "end_node_id": 1,
            "edge_id": 117,
            "start_node_id": 0
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 7.039,
            "line_id": 56,
            "edge_type": 1,
            "end_node_id": 3,
            "edge_id": 118,
            "start_node_id": 0
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 7.039,
            "line_id": 56,
            "edge_type": 1,
            "end_node_id": 0,
            "edge_id": 119,
            "start_node_id": 3
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.438,
            "line_id": 57,
            "edge_type": 1,
            "end_node_id": 4,
            "edge_id": 120,
            "start_node_id": 3
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.438,
            "line_id": 57,
            "edge_type": 1,
            "end_node_id": 3,
            "edge_id": 121,
            "start_node_id": 4
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.583,
            "line_id": 58,
            "edge_type": 1,
            "end_node_id": 5,
            "edge_id": 122,
            "start_node_id": 4
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.583,
            "line_id": 58,
            "edge_type": 1,
            "end_node_id": 4,
            "edge_id": 123,
            "start_node_id": 5
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.492,
            "line_id": 59,
            "edge_type": 1,
            "end_node_id": 1,
            "edge_id": 124,
            "start_node_id": 6
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.492,
            "line_id": 59,
            "edge_type": 1,
            "end_node_id": 6,
            "edge_id": 125,
            "start_node_id": 1
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.625,
            "line_id": 62,
            "edge_type": 1,
            "end_node_id": 9,
            "edge_id": 130,
            "start_node_id": 5
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.625,
            "line_id": 62,
            "edge_type": 1,
            "end_node_id": 5,
            "edge_id": 131,
            "start_node_id": 9
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.455,
            "line_id": 63,
            "edge_type": 1,
            "end_node_id": 7,
            "edge_id": 132,
            "start_node_id": 9
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.455,
            "line_id": 63,
            "edge_type": 1,
            "end_node_id": 9,
            "edge_id": 133,
            "start_node_id": 7
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.427,
            "line_id": 67,
            "edge_type": 1,
            "end_node_id": 13,
            "edge_id": 162,
            "start_node_id": 11
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.427,
            "line_id": 67,
            "edge_type": 1,
            "end_node_id": 11,
            "edge_id": 163,
            "start_node_id": 13
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.258,
            "line_id": 68,
            "edge_type": 1,
            "end_node_id": 9,
            "edge_id": 164,
            "start_node_id": 13
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.258,
            "line_id": 68,
            "edge_type": 1,
            "end_node_id": 13,
            "edge_id": 165,
            "start_node_id": 9
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.703,
            "line_id": 69,
            "edge_type": 1,
            "end_node_id": 14,
            "edge_id": 166,
            "start_node_id": 8
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.703,
            "line_id": 69,
            "edge_type": 1,
            "end_node_id": 8,
            "edge_id": 167,
            "start_node_id": 14
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.889,
            "line_id": 70,
            "edge_type": 1,
            "end_node_id": 17,
            "edge_id": 168,
            "start_node_id": 18
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.889,
            "line_id": 70,
            "edge_type": 1,
            "end_node_id": 18,
            "edge_id": 169,
            "start_node_id": 17
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 3.465,
            "line_id": 71,
            "edge_type": 1,
            "end_node_id": 0,
            "edge_id": 170,
            "start_node_id": 17
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 3.465,
            "line_id": 71,
            "edge_type": 1,
            "end_node_id": 17,
            "edge_id": 171,
            "start_node_id": 0
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 3.735,
            "line_id": 72,
            "edge_type": 1,
            "end_node_id": 19,
            "edge_id": 172,
            "start_node_id": 3
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 3.735,
            "line_id": 72,
            "edge_type": 1,
            "end_node_id": 3,
            "edge_id": 173,
            "start_node_id": 19
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.486,
            "line_id": 73,
            "edge_type": 1,
            "end_node_id": 15,
            "edge_id": 174,
            "start_node_id": 0
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.486,
            "line_id": 73,
            "edge_type": 1,
            "end_node_id": 0,
            "edge_id": 175,
            "start_node_id": 15
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.666,
            "line_id": 74,
            "edge_type": 1,
            "end_node_id": 16,
            "edge_id": 176,
            "start_node_id": 15
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.666,
            "line_id": 74,
            "edge_type": 1,
            "end_node_id": 15,
            "edge_id": 177,
            "start_node_id": 16
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.753,
            "line_id": 75,
            "edge_type": 1,
            "end_node_id": 20,
            "edge_id": 178,
            "start_node_id": 7
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.753,
            "line_id": 75,
            "edge_type": 1,
            "end_node_id": 7,
            "edge_id": 179,
            "start_node_id": 20
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.738,
            "line_id": 76,
            "edge_type": 1,
            "end_node_id": 12,
            "edge_id": 180,
            "start_node_id": 20
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.738,
            "line_id": 76,
            "edge_type": 1,
            "end_node_id": 20,
            "edge_id": 181,
            "start_node_id": 12
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.015,
            "line_id": 80,
            "edge_type": 1,
            "end_node_id": 23,
            "edge_id": 188,
            "start_node_id": 7
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.038,
            "line_id": 81,
            "edge_type": 1,
            "end_node_id": 24,
            "edge_id": 189,
            "start_node_id": 23
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.793,
            "line_id": 82,
            "edge_type": 1,
            "end_node_id": 8,
            "edge_id": 190,
            "start_node_id": 24
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.793,
            "line_id": 82,
            "edge_type": 1,
            "end_node_id": 24,
            "edge_id": 191,
            "start_node_id": 8
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.038,
            "line_id": 81,
            "edge_type": 1,
            "end_node_id": 23,
            "edge_id": 192,
            "start_node_id": 24
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.015,
            "line_id": 80,
            "edge_type": 1,
            "end_node_id": 7,
            "edge_id": 193,
            "start_node_id": 23
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.477,
            "line_id": 83,
            "edge_type": 1,
            "end_node_id": 26,
            "edge_id": 272,
            "start_node_id": 25
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 2.477,
            "line_id": 83,
            "edge_type": 1,
            "end_node_id": 25,
            "edge_id": 273,
            "start_node_id": 26
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.542,
            "line_id": 84,
            "edge_type": 1,
            "end_node_id": 28,
            "edge_id": 274,
            "start_node_id": 27
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.394,
            "line_id": 85,
            "edge_type": 1,
            "end_node_id": 29,
            "edge_id": 275,
            "start_node_id": 28
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.487,
            "line_id": 86,
            "edge_type": 1,
            "end_node_id": 30,
            "edge_id": 276,
            "start_node_id": 29
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.487,
            "line_id": 86,
            "edge_type": 1,
            "end_node_id": 29,
            "edge_id": 277,
            "start_node_id": 30
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.394,
            "line_id": 85,
            "edge_type": 1,
            "end_node_id": 28,
            "edge_id": 278,
            "start_node_id": 29
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 1.542,
            "line_id": 84,
            "edge_type": 1,
            "end_node_id": 27,
            "edge_id": 279,
            "start_node_id": 28
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.765,
            "line_id": 87,
            "edge_type": 1,
            "end_node_id": 28,
            "edge_id": 280,
            "start_node_id": 31
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.765,
            "line_id": 87,
            "edge_type": 1,
            "end_node_id": 31,
            "edge_id": 281,
            "start_node_id": 28
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.442,
            "line_id": 88,
            "edge_type": 1,
            "end_node_id": 32,
            "edge_id": 282,
            "start_node_id": 29
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.442,
            "line_id": 88,
            "edge_type": 1,
            "end_node_id": 29,
            "edge_id": 283,
            "start_node_id": 32
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.535,
            "line_id": 89,
            "edge_type": 1,
            "end_node_id": 33,
            "edge_id": 284,
            "start_node_id": 32
        },
        {
            "max_angular_velocity": 0.5,
            "max_linear_velocity": 1,
            "width": 0,
            "tracking_mode": 0,
            "distance": 0.535,
            "line_id": 89,
            "edge_type": 1,
            "end_node_id": 32,
            "edge_id": 285,
            "start_node_id": 33
        }
    ]
}

--获取agv_grap的lines
/maps/current_map/agv_graph/lines/
get
{
    "code": 2000,
    "detail": "查询成功",
    "lines": [
        {
            "two_way": true,
            "width": 0,
            "line_id": 54,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -0.027,
                "x": -14.039,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 13.479,
            "nodes": [
                2,
                1
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段54",
            "tracking_mode": 0,
            "edges": [
                114,
                115
            ],
            "end_node_pose": {
                "y": -0.218,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 55,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -0.218,
                "x": -0.561,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 5.731,
            "nodes": [
                1,
                0
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段55",
            "tracking_mode": 0,
            "edges": [
                116,
                117
            ],
            "end_node_pose": {
                "y": -5.949,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 56,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": -0.561,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 7.039,
            "nodes": [
                0,
                3
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段56",
            "tracking_mode": 0,
            "edges": [
                118,
                119
            ],
            "end_node_pose": {
                "y": -5.949,
                "x": 6.478,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 57,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": 6.478,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.438,
            "nodes": [
                3,
                4
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段57",
            "tracking_mode": 0,
            "edges": [
                120,
                121
            ],
            "end_node_pose": {
                "y": -3.511,
                "x": 6.478,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 58,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -3.511,
                "x": 6.478,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.583,
            "nodes": [
                4,
                5
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段58",
            "tracking_mode": 0,
            "edges": [
                122,
                123
            ],
            "end_node_pose": {
                "y": -2.411,
                "x": 7.617,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 59,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": 2.274,
                "x": -0.561,
                "yaw": 1.5708
            },
            "line_type": 1,
            "distance": 2.492,
            "nodes": [
                6,
                1
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段59",
            "tracking_mode": 0,
            "edges": [
                124,
                125
            ],
            "end_node_pose": {
                "y": -0.218,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 62,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.411,
                "x": 7.617,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.625,
            "nodes": [
                5,
                9
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段62",
            "tracking_mode": 0,
            "edges": [
                130,
                131
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 10.213,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 63,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 10.213,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.455,
            "nodes": [
                9,
                7
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段63",
            "tracking_mode": 0,
            "edges": [
                132,
                133
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 11.668,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 67,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": 1.665,
                "x": 10.213,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.427,
            "nodes": [
                11,
                13
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段67",
            "tracking_mode": 0,
            "edges": [
                162,
                163
            ],
            "end_node_pose": {
                "y": 0.238,
                "x": 10.213,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 68,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": 0.238,
                "x": 10.213,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.258,
            "nodes": [
                13,
                9
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段68",
            "tracking_mode": 0,
            "edges": [
                164,
                165
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 10.213,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 69,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 14.514,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.703,
            "nodes": [
                8,
                14
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段69",
            "tracking_mode": 0,
            "edges": [
                166,
                167
            ],
            "end_node_pose": {
                "y": -1.802,
                "x": 16.203,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 70,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": -6.915,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.889,
            "nodes": [
                18,
                17
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段70",
            "tracking_mode": 0,
            "edges": [
                168,
                169
            ],
            "end_node_pose": {
                "y": -5.949,
                "x": -4.026,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 71,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": -4.026,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 3.465,
            "nodes": [
                17,
                0
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段71",
            "tracking_mode": 0,
            "edges": [
                170,
                171
            ],
            "end_node_pose": {
                "y": -5.949,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 72,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": 6.478,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 3.735,
            "nodes": [
                3,
                19
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段72",
            "tracking_mode": 0,
            "edges": [
                172,
                173
            ],
            "end_node_pose": {
                "y": -5.949,
                "x": 10.213,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 73,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.949,
                "x": -0.561,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.486,
            "nodes": [
                0,
                15
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段73",
            "tracking_mode": 0,
            "edges": [
                174,
                175
            ],
            "end_node_pose": {
                "y": -8.435,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 74,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -8.435,
                "x": -0.561,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.666,
            "nodes": [
                15,
                16
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段74",
            "tracking_mode": 0,
            "edges": [
                176,
                177
            ],
            "end_node_pose": {
                "y": -11.101,
                "x": -0.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 75,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 11.668,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.753,
            "nodes": [
                7,
                20
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段75",
            "tracking_mode": 0,
            "edges": [
                178,
                179
            ],
            "end_node_pose": {
                "y": -2.773,
                "x": 11.668,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 76,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.773,
                "x": 11.668,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.738,
            "nodes": [
                20,
                12
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段76",
            "tracking_mode": 0,
            "edges": [
                180,
                181
            ],
            "end_node_pose": {
                "y": -3.511,
                "x": 11.668,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 80,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 11.668,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.015,
            "nodes": [
                7,
                23
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段80",
            "tracking_mode": 0,
            "edges": [
                188,
                193
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 12.683,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 81,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 12.683,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.038,
            "nodes": [
                23,
                24
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段81",
            "tracking_mode": 0,
            "edges": [
                189,
                192
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 13.721,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 82,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -2.02,
                "x": 13.721,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.793,
            "nodes": [
                24,
                8
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段82",
            "tracking_mode": 0,
            "edges": [
                190,
                191
            ],
            "end_node_pose": {
                "y": -2.02,
                "x": 14.514,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 83,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -3.223,
                "x": 19.084,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 2.477,
            "nodes": [
                25,
                26
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段83",
            "tracking_mode": 0,
            "edges": [
                272,
                273
            ],
            "end_node_pose": {
                "y": -3.223,
                "x": 21.561,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 84,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -6.015,
                "x": 14.572,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.542,
            "nodes": [
                27,
                28
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段84",
            "tracking_mode": 0,
            "edges": [
                274,
                279
            ],
            "end_node_pose": {
                "y": -6.015,
                "x": 16.114,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 85,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -6.015,
                "x": 16.114,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.394,
            "nodes": [
                28,
                29
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段85",
            "tracking_mode": 0,
            "edges": [
                275,
                278
            ],
            "end_node_pose": {
                "y": -6.015,
                "x": 17.508,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 86,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -6.015,
                "x": 17.508,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 1.487,
            "nodes": [
                29,
                30
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段86",
            "tracking_mode": 0,
            "edges": [
                276,
                277
            ],
            "end_node_pose": {
                "y": -6.015,
                "x": 18.995,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 87,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -5.25,
                "x": 16.114,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.765,
            "nodes": [
                31,
                28
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段87",
            "tracking_mode": 0,
            "edges": [
                280,
                281
            ],
            "end_node_pose": {
                "y": -6.015,
                "x": 16.114,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 88,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -6.015,
                "x": 17.508,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.442,
            "nodes": [
                29,
                32
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段88",
            "tracking_mode": 0,
            "edges": [
                282,
                283
            ],
            "end_node_pose": {
                "y": -6.457,
                "x": 17.508,
                "yaw": 0
            }
        },
        {
            "two_way": true,
            "width": 0,
            "line_id": 89,
            "max_linear_velocity": 1,
            "start_node_pose": {
                "y": -6.457,
                "x": 17.508,
                "yaw": 0
            },
            "line_type": 1,
            "distance": 0.535,
            "nodes": [
                32,
                33
            ],
            "max_angular_velocity": 0.5,
            "name": "普通线段89",
            "tracking_mode": 0,
            "edges": [
                284,
                285
            ],
            "end_node_pose": {
                "y": -6.992,
                "x": 17.508,
                "yaw": 0
            }
        }
    ],
    "count_line_id": 89
}
--获取agv_graph 的shelf_layers
http://192.168.0.185:7700/maps/current_map/agv_graph/shelf_layers/
method   get
resp
{
    "code": 2000,
    "detail": "查询成功",
    "shelf_layers": []
}


--提交agv_graph 的shelf_layers

method   post

--获取agv——graph的node_tags
method   get
http://192.168.0.185:7700/maps/current_map/agv_graph/node_tags/
resp



{
    "code": 2000,
    "node_tags": [],
    "detail": "查询成功"
}

--提交agv——graph的node_types&删除agv_graph_types

--获取agv_graph的node_types
http://192.168.0.185:7700/maps/current_map/agv_graph/node_types/
get
resp
{
    "code": 2000,
    "detail": "查询成功",
    "node_types": [
        {
            "detail_en": "charge",
            "navigation_feature": 2,
            "detail_zh": "充电节点",
            "directed": 1,
            "type_num": 13
        },
        {
            "detail_en": "loading",
            "navigation_feature": 1,
            "detail_zh": "装货点",
            "directed": 1,
            "type_num": 19
        },
        {
            "detail_en": "undirected",
            "navigation_feature": 1,
            "detail_zh": "无向目标节点",
            "directed": 0,
            "type_num": 11
        },
        {
            "detail_en": "station",
            "navigation_feature": 2,
            "detail_zh": "操作站",
            "directed": 1,
            "type_num": 16
        },
        {
            "detail_en": "multi_layer_shelf",
            "navigation_feature": 1,
            "detail_zh": "多层货架（叉车专用）",
            "directed": 1,
            "type_num": 17
        },
        {
            "detail_en": "direct",
            "navigation_feature": 1,
            "detail_zh": "有向节点",
            "directed": 1,
            "type_num": 12
        },
        {
            "detail_en": "default",
            "navigation_feature": 0,
            "detail_zh": "结构点",
            "directed": 0,
            "type_num": 10
        },
        {
            "detail_en": "unloading",
            "navigation_feature": 1,
            "detail_zh": "卸货点",
            "directed": 1,
            "type_num": 20
        },
        {
            "detail_en": "storage",
            "navigation_feature": 1,
            "detail_zh": "储货位（无向）",
            "directed": 0,
            "type_num": 18
        },
        {
            "detail_en": "parking",
            "navigation_feature": 2,
            "detail_zh": "泊车位",
            "directed": 1,
            "type_num": 15
        }
    ]
}

--创建场景
http://192.168.0.185:7700/maps/scene/create_scene/
post
body ： name:    describe:

resp
{
    "code": 2000,
    "all_page": 1,
    "scenes": [
        {
            "id": 1,
            "name": "新建场景(1)"
        },
        {
            "describe": "257003444",
            "id": 3,
            "name": "1有"
        },
        {
            "describe": "测试中",
            "id": 6,
            "name": "场景测试"
        },
        {
            "describe": "率",
            "id": 7,
            "name": "问问"
        }
    ],
    "detail": "请求成功",
    "page": 1,
    "data_count": 4,
    "per_page": 15
}
--查看场景
http://192.168.0.185:7700/maps/scene/get_all_scene/
get
resp
{
    "code": 2000,
    "all_page": 1,
    "scenes": [
        {
            "id": 1,
            "name": "新建场景(1)"
        },
        {
            "describe": "257003444",
            "id": 3,
            "name": "1有"
        },
        {
            "describe": "测试中",
            "id": 6,
            "name": "场景测试"
        },
        {
            "describe": "率",
            "id": 7,
            "name": "问问"
        },
        {
            "id": 9,
            "name": "新建场景(3)"
        }
    ],
    "detail": "请求成功",
    "page": 1,
    "data_count": 5,
    "per_page": 15
}

--获取单个场景

/maps/scene/get_scene/{scene_id}
get
--修改场景信息
/maps/scene/get_scene/{scene_id}

req  name  describe

post

--删除单个场景
、
/maps/scene/del_scene/{scene_id}

--获取单场景的地图
/maps/scene/get_map/{scene_id}





