from models.models import KnownFaces, UnknownFace
from db import db
from sqlalchemy.exc import NoResultFound


class FaceSpace():
    def __init__(self):
        self.session = db.create_database()

    def insert_face(self, data: KnownFaces):
        self.session.add(data)

    def update_face(self, data: KnownFaces):
        try:
            record = self.session.query(KnownFaces).filter(
                KnownFaces.first_name == data.first_name).one()

        except NoResultFound:
            self.insert_face(data)

        self.session.commit()

    def add_unknown_face(self, data: UnknownFace):
        self.session.add(data)
        self.session.commit()


known = KnownFaces(
    first_name='Daniil',
    second_name='Ermolaev',
    path_to_face='/path/'
)

unknownface = UnknownFace(
    path_to_face='/path/'
)


#root = FaceSpace().update_face(known)
#key = FaceSpace().add_unknown_face(unknownface)
