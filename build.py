from app import app
from flask_frozen import Freezer

freezer = Freezer(app=app, with_static_files=True)
if __name__ == '__main__':
    freezer.freeze()
    
