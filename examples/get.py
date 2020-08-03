import os
import random
from _datetime import datetime

from dotenv import load_dotenv
from rauth import OAuth1Service

from bricklink import CatalogApi, ApiClient, Configuration
from bricklink.rest import RESTClientObject

load_dotenv()

configuration = Configuration(api_key=dict(
    consumer_key=os.environ['OAUTH_CONSUMER_KEY'],
    consumer_secret=os.environ['OAUTH_CONSUMER_SECRET'],
    token=os.environ['OAUTH_TOKEN'],
    token_secret=os.environ['OAUTH_TOKEN_SECRET']
))


def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


class Oauth1RestClient(RESTClientObject):
    def __init__(self, configuration):
        self.configuration = configuration
        self.service = OAuth1Service(
            consumer_key=self.configuration.api_key['consumer_key'] ,
            consumer_secret=self.configuration.api_key['consumer_secret'] ,
        )
        self.session = self.service.get_session((self.configuration.api_key['token'], self.configuration.api_key['token_secret']))
        super().__init__(configuration)

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):

        oauth_params = dict(
            oauth_consumer_key=self.configuration.api_key['consumer_key'],
            oauth_nonce=generate_nonce(),
            oauth_signature_method="HMAC-SHA1",
            oauth_timestamp=int(datetime.now().timestamp()),
            oauth_token=self.configuration.api_key['token'],
            oauth_version="1.0"
        )

        signature = self.session.signature.sign(
            self.configuration.api_key['consumer_secret'],
            self.configuration.api_key['token_secret'],
            method, url, oauth_params, {}
        )
        oauth_params['oauth_signature'] = signature
        oauth_params['realm'] = ""

        headers['Authorization'] = 'Oauth ' + ','.join(f'{k}=\"{v}\"' for k, v in oauth_params.items())
        return super().request(method, url, query_params, headers,
                               body, post_params, _preload_content, _request_timeout)


class Oauth1Client(ApiClient):
    pass


client = Oauth1Client(configuration)
client.rest_client = Oauth1RestClient(configuration)

api = CatalogApi(client)

data = api.items_type_no_get('MINIFIG', 'cty0859')

pass
