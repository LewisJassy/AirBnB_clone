import uuid #Universally Unique Identifier
from datetime import datetime


class BaseModel:
    """Basemodel class for  data models."""
    def __init__(self): #initializes the instance with a unique ID, creation timestamp
        # and update timestamp
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self): 
        """
        provide human readable string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the update timestamp of the instance to the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance into a dictionary.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
