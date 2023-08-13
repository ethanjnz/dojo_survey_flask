from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash

DATABASE = "dojo_survey_schema"


class Survey:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def val_form(survey):
        is_valid = True
        if len(survey["name"]) < 3:
            flash("Name must be at least 3 Characters")
            is_valid = False
        if survey["location"] == "none":
            flash("please enter a Location")
            is_valid = False
        if survey["language"] == "none":
            flash("Please enter a Language")
            is_valid = False
        if len(survey["comment"]) < 3:
            flash("comment must be at least 3 Characters")
            is_valid = False

        return is_valid

    @classmethod
    def create(cls, form_data):
        query = """
                INSERT INTO surveys (name, location, language, comment)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);  
                """
        result = connect_to_mysql(DATABASE).query_db(query, form_data)
        return result

    @classmethod
    def get_one(cls, survey_id):
        query = """
                SELECT * FROM surveys
                WHERE id = %(survey_id)s;
                """
        data = {"survey_id": survey_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return Survey(results[0])
