from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.lesson import Lesson
from data.reqparse import parser


def abort_if_lesson_not_found(lesson_id):
    session = db_session.create_session()
    lesson = session.query(Lesson).get(lesson_id)
    if not lesson:
        abort(404, message=f"User {lesson_id} not found")


class LessonResource(Resource):
    def get(self, lesson_id):
        abort_if_lesson_not_found(lesson_id)
        session = db_session.create_session()
        lesson = session.query(Lesson).get(lesson_id)
        return jsonify({'lesson': lesson.to_dict(
            only=('id', 'name', 'about'))})

    def delete(self, lesson_id):
        abort_if_lesson_not_found(lesson_id)
        session = db_session.create_session()
        lesson = session.query(User).get(lesson_id)
        session.delete(lesson)
        session.commit()
        return jsonify({'success': 'OK'})


class LessonListResource(Resource):
    def get(self):
        session = db_session.create_session()
        lesson = session.query(Lesson).all()
        return jsonify({'lesson': [item.to_dict(
            only=('id', 'name', 'lesson.name')) for item in lesson]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        lesson = L(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            created_date=args['created_date']
        )
        session.add(lesson)
        session.commit()
        return jsonify({'success': 'OK'})
