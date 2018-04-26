

class SysExceptionCode (object):
    def globalInfo(self):
        if SYS_SUCCESS(0,"操作成功") == True:
            return 0,"操作成功"
