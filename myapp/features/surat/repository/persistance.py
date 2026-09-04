from myapp.extensions import db

class Persistence:
    @staticmethod
    def save(obj, commit=True):
        db.session.add(obj)

        if commit:
            db.session.commit()

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()