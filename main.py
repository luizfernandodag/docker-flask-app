
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)
#redis = Redis(host="localhost", port=6379)
# default port 6379



@app.route('/')
def hello_world():
    redis.incr('hits')
    count = str(redis.get('hits'))
    print(count[1:])
    return 'LEARNING' +  count[2:len(count)-1]

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002, debug=True)
    #app.run(port=5002, debug=True)