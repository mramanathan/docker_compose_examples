from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)
# connect to 'redis' container running 'redis' at port 6379
redis = Redis(host="redis", port=6379, db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

# Support for POST, GET
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.json['name']
        redis.rpush('cities', {'name' : name})
        return jsonify({'name' : name})

    # Default: Emit all the key-value pairs from redis
    if request.method == "GET":
        return jsonify(redis.lrange('cities', 0, -1))

## CAUTION: Do _NOT_ use in production
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
