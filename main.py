from flask import Flask
from flask_restful import Api

from data import db_session, news_resources, users_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app, catch_all_404s=True)


def main():
    db_session.global_init("04_Samples/db/blogs.db")

    api.add_resource(users_resource.UsersListResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')
    app.run()


if __name__ == '__main__':
    main()
