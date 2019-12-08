#from flask import Flask
#from redis import Redis, RedisError
#import os
#import socket
#
#redis = Redis(host="redis-server", db=0, socket_connect_timeout=2, socket_timeout=2)
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    try:
#        visits = redis.incr("counter")
#    except RedisError:
#        visits = "<i>cannot connect to Redis server to count</i>"
#
#    html = "<h3>Hello World!</h3>\n" \
#           "<b>Hostname:</b> {hostname}<br/>\n" \
#           "<b>Visits:</b> {visits}\n"
#
#    return html.format(hostname=socket.gethostname(), visits=visits)
#
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=80)

from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379, db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.json['name']
        redis.rpush('cities', {'name' : name})
        return jsonify({'name' : name})

    if request.method == "GET":
        return jsonify(redis.lrange('cities', 0, -1))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
