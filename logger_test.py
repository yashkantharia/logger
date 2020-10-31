from flask import Flask, render_template, Response, url_for
import datetime 
import os
import time
from flask import request
import collections


l = collections.deque(10*[0],10)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



APP = Flask(__name__, static_folder="app/static/", template_folder="app/static/")




@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")


def flask_logger():
    """creates logging information"""
    for i in range(100):
    	#current_time = datetime.datetime.now().strftime('%H:%M:%S') +" "+ str(i)
    	#l.append(current_time.encode())
    	l.append(str(i))
    	f = open("log.txt", 'r+')
    	yield str(i)+" "+str(collections.deque(f, 10))+"\n"+"\n"
    	f.write(str([x for x in l])+"\n")
    	f.close()
    	time.sleep(1)




@APP.route("/log_stream", methods=["GET"])
def log_stream():
    """returns logging information"""
    return Response(flask_logger(), mimetype="text/plain", content_type="text/event-stream")



if __name__=='__main__':
	APP.run(debug=True,threaded=True)