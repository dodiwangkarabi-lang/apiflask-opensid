from myapp.features.auth.utils import hash_password, check_password

# ----- repository -----
from myapp.features.auth.repository import user_repository

class GantiPasswordAdmin:
    def __init__(self):
        self.user_repository = user_repository
    
    def execute(self, user_id, password_lama, password_baru) -> None:
        user = self.user_repository.get_user_by_id(user_id)
        
        if not check_password(password_lama, user.password):
            raise Exception("Password lama salah")
        
        user.password = hash_password(password_baru)

        user_repository.update_user(user)

        return