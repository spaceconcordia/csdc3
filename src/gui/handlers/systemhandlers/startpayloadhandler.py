import sys
sys.path.append("/root/csdc3/src/payload")
import tornado.web
#from payload import Payload

class StartPayloadHandler(tornado.web.RequestHandler):
    def put(self):
        # start Payload! call payload job 
        #payload = Payload(2)
        #`payload.start()
        pass
