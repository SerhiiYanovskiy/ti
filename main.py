from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="1.invingatorul")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_:ConnectEvent):
    print(client.room_id,"\nВошёл(а) в чат\n=====================================")


# Notice no decorator?
async def on_comment(event: CommentEvent):
    max_len = 35
    if len(event.comment) > max_len:
        event.comment = event.comment[:max_len] + "\n" + event.comment[max_len:]
        print(f"{event.user.uniqueId}\n-> {event.comment}\n=====================================")
    else:
        print(f"{event.user.uniqueId}\n-> {event.comment}\n=====================================")

# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
