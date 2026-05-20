import os
from dotenv import load_dotenv

load_dotenv('.env') 
 
# define apify api token
Apify_api=os.environ["apify_token"]