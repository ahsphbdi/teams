import os
from beanie import init_beanie
import motor.motor_asyncio
from core.config.mongo import MongoConfig
from database.model import User, Team

client = motor.motor_asyncio.AsyncIOMotorClient(MongoConfig.MONGODB_URL)
database = client.gohar
users_collection = database.users
teams_collection = database.teams


async def create_unique_index():
    unique_index = await users_collection.create_index([("usernaem", 1)], unique=True)
    unique_index = await users_collection.create_index([("email", 1)], unique=True)


async def initiate_database():
    await init_beanie(database=database, document_models=[User, Team])
