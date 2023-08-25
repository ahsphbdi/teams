from database.connection import teams_collection
from .schema import TeamCreateSchema


class TeamsController:
    @staticmethod
    async def get_team(t_id: str):
        return await teams_collection.find_one({"_id": t_id})

    @staticmethod
    async def get_teams(skip, limit):
        teams = []
        cursor = teams_collection.find().skip(skip).limit(limit)
        for document in await cursor.to_list(length=100):
            teams.append(document)
        return teams

    @staticmethod
    async def create_team(body: TeamCreateSchema):
        result = await teams_collection.insert_one({"title": body.title, "members": []})
        inserted_team = await teams_collection.find_one({"_id": result.inserted_id})
        return {**inserted_team, "_id": str(inserted_team["_id"])}

    @staticmethod
    async def update_team(t_id: str):
        pass

    @staticmethod
    async def delete_team(t_id: str):
        pass

    @staticmethod
    async def join_on_team(t_id: str):
        pass
