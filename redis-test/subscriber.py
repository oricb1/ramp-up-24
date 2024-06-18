import redis

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Create a PubSub object
pubsub = r.pubsub()
pubsub.subscribe('my_channel')

print('Subscribed to the channel. Waiting for messages...')

# Listen for messages
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received message: {message['data']}")