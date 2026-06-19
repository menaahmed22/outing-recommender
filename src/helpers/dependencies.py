from apify_client import ApifyClient
from helpers.config import Apify_api

client = ApifyClient(Apify_api)

def get_apify_client():
    return client