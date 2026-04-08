import os
import time
import redis
from flask import Flask

app = Flask(__name__)

# Ye line Docker Compose se 'REDIS_HOST' uthayegi
# Agar variable nahi mila, toh default 'redis-db' use karega
redis_host = os.environ.get('REDIS_HOST', 'redis-db')
cache = redis.Redis(host=redis_host, port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'''
    <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1 style="color: #2c3e50;">Shivendra, Automation Sahi Chal Raha Hai! 🔥</h1>
        <p style="font-size: 24px;">Ye page <b style="color: #e74c3c;">{count}</b> baar dekha gaya hai.</p>
        <hr style="width: 50%; border: 0.5px solid #eee;">
        <p style="color: #7f8c8d;">Status: Connected to Redis on <b>{redis_host}</b></p>
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
