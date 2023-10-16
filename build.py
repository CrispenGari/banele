from app import app
from flask_frozen import Freezer


freezer = Freezer(app=app)
freezer.freeze_yield()
if __name__ == '__main__':
    freezer.freeze()
    
