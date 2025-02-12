from typing import Optional
from main_library.user import User
from main_library.library import Library


class Registration:

    @staticmethod
    def add_user(user: User, library: Library) -> Optional[str]:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with ID = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library) -> Optional[str]:
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        try:
            user = [u for u in library.user_records if u.user_id == user_id][0]
            if user.username != new_username:
                user.username = new_username
                return f"Username successfully changed to: {new_username} for " \
                       f"user id: {user.user_id}"
            return "Please check again the provided username - it should be different" \
                   "than the username used so far!"
        except IndexError:
            return f"There is no user with id = {user_id}"
