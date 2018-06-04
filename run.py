from fe_store import app, db
from fe_store.fake_db import create_fake_db


if __name__ == '__main__':
    create_fake_db(db)

    app.run(debug=True)

