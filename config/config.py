#import os
#from dotenv import load_dotenv

#load_dotenv()


#class Config:
   # GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Only raise error in local/dev (optional improvement)
if not Config.GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY is not set")
