from django.test import TestCase
from channels.testing import WebsocketCommunicator
from django.urls import path
from channels.routing import URLRouter

from .consumers import ChatConsumer

class MyTests(TestCase):
    async def test_chatconsumer(self):
        application = URLRouter([
            path("testws/<room_name>/", ChatConsumer.as_asgi()),
        ])
        communicator = WebsocketCommunicator(application, "/testws/test/")
        
        connected, subprotocol = await communicator.connect()
        assert connected
        
        # Test sending text
        await communicator.send_to(text_data='{"message":"hello", "username":"Pushkar", "room":"test"}')
        response = await communicator.receive_from()
        self.assertEqual(response, '{"message": "hello", "username": "Pushkar", "room": "test"}') 
        
        # Close
        await communicator.disconnect()