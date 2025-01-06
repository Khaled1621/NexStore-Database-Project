from supabase import Client

from src.db.dao import BaseDAO
from src.db.models import Orders
from src.db.tables import SupabaseTables


class OrdersDAO(BaseDAO[Orders]):
    def __init__(self, client: Client):
        super().__init__(client, SupabaseTables.ORDERS, Orders)
