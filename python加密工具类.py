#coding=utf-8
import hashlib
import hmac



class encryptUtil:
    # 加密函数
    @staticmethod
    def signUp(secretkey,paramMap):
        sha1 = hashlib.sha1()
        sha1.update(secretkey.encode("utf-8"))
        param=encryptUtil.signUpParam(paramMap)
        secret = sha1.hexdigest()
        #print (param)
        apiSign = hmac.new(secret.encode("utf-8"),param.encode("utf-8"),digestmod=hashlib.sha256).hexdigest()
        return apiSign

    # 处理ascessksy返回acesskey
    @staticmethod
    def signUpParam(paramMap):
        param=""
        for key in paramMap:
            param=param+key+"="+paramMap[key]+"&"
        #print param[:len(param)-1]
        return param[:len(param)-1]







