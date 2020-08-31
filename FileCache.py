import os.path
import hashlib
import time
import json

class FileCache:
    @staticmethod
    def get(key, value):
        return value

    @staticmethod
    def getDir(key):
        sha = hashlib.sha1(str(key).encode('utf-8'))
        encrypts = sha.hexdigest()
        first = encrypts[0:2]
        second = encrypts[2:4]
        path_list = []
        path_list.append(first)
        path_list.append(second)
        return path_list

    '''
            默认过期时间是一天
    '''
    @staticmethod
    def put(key, value, minute=3600*24):
        # 首先确定路径
        if not os.path.exists('cache'):
            os.mkdir('cache')
        path_list = FileCache.getDir(key)
        if not os.path.exists('cache/'+path_list[0]):
            os.mkdir('cache/'+path_list[0])
        if not os.path.exists('cache/'+path_list[0]+"/"+path_list[1]):
            os.mkdir('cache/'+path_list[0]+"/"+path_list[1])
        path = 'cache/'+path_list[0]+"/"+path_list[1]
        # key是文件名
        file_name = key
        # 过期时间是key
        expire = time.time()+minute
        value = json.dumps(value)
        res = {}
        res[expire] = value
        fo = open(path+"/"+file_name, "w")
        fo.write(json.dumps(res))
        # 关闭打开的文件
        fo.close()




if __name__ == '__main__':
    FileCache.put('11','33',3)