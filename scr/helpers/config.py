import os
from dotenv import load_dotenv

load_dotenv('.env') 
 
# define apify api token
Apify_api=os.getenv("apify_token")