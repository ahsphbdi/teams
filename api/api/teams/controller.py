from bson import ObjectId
from fastapi.exceptions import HTTPException
from database.connection import teams_collection, users_collection
from core.security.auth import User
from .schema import TeamCreateSchema, TeamUpdateScema


class TeamsController:
    @staticmethod
    async def get_team(t_id: str):
        date = await teams_collection.find_one({"_id": ObjectId(t_id)})
        if date is None:
            raise HTTPException(status_code=404, detail="not found")
        return date

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
        return inserted_team

    @staticmethod
    async def update_team(t_id: str, body: TeamUpdateScema):
        result = await teams_collection.update_one(
            {"_id": ObjectId(t_id)}, {"$set": body.model_dump()}
        )
        if result.modified_count == 1:
            pass
        else:
            raise HTTPException(status_code=404, detail="not found")
        updated_team = await teams_collection.find_one({"_id": ObjectId(t_id)})
        return updated_team

    @staticmethod
    async def delete_team(t_id: str):
        date = await teams_collection.delete_one({"_id": ObjectId(t_id)})
        if date.deleted_count == 0:
            raise HTTPException(status_code=404, detail="not found")
        return {"message": "ok"}

    @staticmethod
    async def join_on_team(t_id: str, current_user: User):
        result = await teams_collection.update_one(
            {"_id": ObjectId(t_id)}, {"$push": {"members": ObjectId(current_user.id)}}
        )
        if result.modified_count == 1:
            return {"message": "member added to team"}
        elif result.modified_count >= 1:
            raise HTTPException(status_code=500, detail="error acured")
        elif result.modified_count >= 1:
            raise HTTPException(status_code=404, detail="not found")
