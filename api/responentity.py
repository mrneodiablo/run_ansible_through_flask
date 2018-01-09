'''
return {
    'status': 0/1/-1
    'data': 'xyz'
    'msg': 'xyz'
}

1 = error
0 = okie
-1 = exception
'''

class ResponeEntity(object):

        @staticmethod
        def return_ok(data=None, msg=None):
            return {
                'status': 0,
                'data': data,
                'msg': msg
            }

        @staticmethod
        def return_error(data=None, msg=None):
            return {
                'status': 1,
                'data': data,
                'msg': msg
            }

        @staticmethod
        def return_exception(data=None, msg=None):
            return {
                'status': -1,
                'data': data,
                'msg': msg
            }