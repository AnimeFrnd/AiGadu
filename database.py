
from config import DB_URL, DB_NAME
from pymongo import MongoClient

# MongoDB Connection
mongo_client = MongoClient(DB_URL)
db = mongo_client[DB_NAME]

# Collections
user_collection = db["users"]
file_collection = db["files"]
log_collection = db["logs"]

# Add New User
def add_user(user_id, first_name):
    if not user_collection.find_one({"user_id": user_id}):
        user_collection.insert_one({"user_id": user_id, "first_name": first_name})

# Check User
def is_user_exist(user_id):
    return user_collection.find_one({"user_id": user_id}) is not None

# Add File to Database
def save_file(file_id, file_name, file_type, file_size, owner_id):
    file_collection.insert_one({
        "file_id": file_id,
        "file_name": file_name,
        "file_type": file_type,
        "file_size": file_size,
        "owner_id": owner_id
    })

# Get File
def get_file(file_id):
    return file_collection.find_one({"file_id": file_id})

# Log Activity
def log_activity(user_id, action, file_id=None):
    log_collection.insert_one({
        "user_id": user_id,
        "action": action,
        "file_id": file_id
    })

# Count Total Users
def total_users():
    return user_collection.count_documents({})
