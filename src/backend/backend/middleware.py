from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from rest_framework_api_key.models import APIKey
from datasocks.models import Machine,MachineAccessAPIKey

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

@database_sync_to_async
def get_machine(api_key):
    apikey =  MachineAccessAPIKey.objects.get_from_key(api_key)
    machine = Machine.objects.get(api_key=apikey)
    return machine

class WebSocketAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        
        token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        api_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('api_key', None)
        
        if token_key:
            scope['user'] = await get_user(token_key)
            scope['machine'] = None


        if api_key:
            scope['machine'] =  await get_machine(api_key)
            scope['user'] = None
        
        return await super().__call__(scope, receive, send)


 