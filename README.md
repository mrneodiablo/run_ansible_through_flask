FIle mieu ta interface cua app api

[ http://127.0.0.1/api/tcm ]
    * request
      + header request authen-basic with user/pass
      + header request content-type request : 'application/json'
      + request method POST
      + body request json data : {'method': 'check/run', 'command': 'ls -las'}

    * respone
        {
            'status': 0/1/-1,
            'data': data,
            'msg': msg
        }

        status : 0 == okie
                 1 == error
                -1 == exception



[ http://127.0.0.1/api/get_patch ]
    * request
      + header request authen-basic with user/pass
      + header request content-type request : 'application/json'
      + request method POST
      + body request json data : {'method': 'download', 'url': ' cfm.ffddd.vn.tar.gz'}

    * respone
        {
            'status': 0/1/-1,
            'data': data,
            'msg': msg
        }

        status : 0 == okie
                 1 == error
                -1 == exception


[ http://127.0.0.1/api/copy ]
     * request
       + header request authen-basic with user/pass
       + header request content-type request : 'application/json'
       + request method POST
       + body request json data : {'method': 'check/run', 'filename': 'cfm.ssff.tar.gz'}

     * respone
         {
             'status': 0/1/-1,
             'data': data,
             'msg': msg
         }

         status : 0 == okie
                  1 == error
                 -1 == exception