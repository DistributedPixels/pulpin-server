import os
from dotenv import load_dotenv
from supabase import create_client

class Connection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            url = os.environ.get("SUPABASE_URL")
            key = os.environ.get("SUPABASE_KEY")
            cls._instance =  create_client(url, key)
        return  cls._instance

    def get_client(self):
        return self._instance

