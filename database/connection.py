import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
users = client.users
teams = client.teams
