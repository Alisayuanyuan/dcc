import requests
import hashlib
import json

def login(username,password):
    loginurl = 'https://api.douchacha.com/circle/user/login'
    header = {
        "Content-Type":"application/json",
        "TypeId":"f8W1vf",
    }
    sha_pass = hashlib.sha1(password.encode()).hexdigest()
    body = {
        "phone":username,
        "password":sha_pass
    }
    s = requests.post(loginurl,headers = header,data=json.dumps(body))
    #{"code":200,"msg":"登录成功","data":{"token":"eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiV0VCIiwiZXhwIjoxNTkxNjY2MDQ5LCJ1c2VySWQiOjEyNjYzMDUzODg0MTQ2Njg4MDIsImNyZWF0ZURhdGUiOiIyMDIwLTA2LTAyIDA5OjI3OjI5In0.z0VrvOy7iJabeZOcI8U3rkr9TLp9qlO4ec6P2oH2R30","rf_certificate":"eyJhbGciOiJIUzUxMiJ9.eyJ0eXBlIjoiV0VCIiwiZXhwIjoxNTkyMjcwODQ5LCJ1c2VySWQiOjEyNjYzMDUzODg0MTQ2Njg4MDIsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKMGVYQmxJam9pVjBWQ0lpd2laWGh3SWpveE5Ua3hOalkyTURRNUxDSjFjMlZ5U1dRaU9qRXlOall6TURVek9EZzBNVFEyTmpnNE1ESXNJbU55WldGMFpVUmhkR1VpT2lJeU1ESXdMVEEyTFRBeUlEQTVPakkzT2pJNUluMC56MFZydk95N2lKYWJlWk9jSThVM3JrcjlUTHA5cWxPNGVjNlAyb0gyUjMwIiwiY3JlYXRlRGF0ZSI6IjIwMjAtMDYtMDIgMDk6Mjc6MjkifQ.ok8iz6JpsUQvPlvr-9u6VG_lRCExqjId0pa5oSiUtR5XpIlnRZwNoMuDTC1RMjH_V-2gKqvStSGLKGedXlIkVw","user":{"user_id":"1266305388414668802","phone":"17635433806","nick_name":"Clown","head_img":"http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLHGZgQJjatG4b4Gya2dvI1VqftW6MHHWlQTAPK2T25uhFk5wSQB0g7dSh8kujxmclibeiahu4NAUow/132","gender":"male","need_entry":false,"can_use":true},"user_id":"1266305388414668802"}}
    try:
        token = json.loads(s.content)['data']['token']
    except:
        print(s.content.decode())
        print(username+'登录失败')
        exit(0)
    return token