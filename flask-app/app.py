from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Bhai, ye Automation ka kamaal hai! 🔥 Ye page {count} baar dekha gaya hai.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
