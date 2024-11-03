import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGO_URI = os.environ.get('mongodb+srv://abdullahesmatullah:UlX9twEZ5VllSy7x@cluster0.jqezl.mongodb.net/') or 'your_mongodb_connection_string'