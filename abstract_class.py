from abc import ABC, abstractmethod 

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass
    @abstractmethod
    def get_all_users(self):
        pass
    

