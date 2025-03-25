import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Accepts the connection

    async def disconnect(self, close_code):
        pass  # Handles disconnection

    async def receive(self, text_data):
        data = json.loads(text_data)  # Convert text to Python dictionary
        message = data["message"]  # Extract message from dictionary

        # Send message back
        await self.send(text_data=json.dumps({
            "message": message  # Sends the same message back
        }))
