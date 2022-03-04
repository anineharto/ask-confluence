from ask_confluence.app.service.answer_service import get_answer_from_confluence
from flask import Flask, jsonify
try:
    from flask_restplus import Resource, Api, reqparse
except ImportError: # Due to bug in werkzeug. See https://github.com/jarus/flask-testing/issues/143.
    import werkzeug, flask.scaffold
    werkzeug.cached_property = werkzeug.utils.cached_property
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
    from flask_restplus import Resource, Api, reqparse


def create_app():
    """Create flask application with swagger documentation.

    Returns: 
        flask_app (Flask): API service for ask confluence.
    """
    flask_app = Flask(__name__)
    app = Api(flask_app)

    name_space = app.namespace("app", description="Main API for asking Confluence")

    parser_question = create_parser("Question")

    @name_space.route("/healthcheck")
    class Health(Resource):
        """Allow resource for health check of application."""

        @name_space.doc("")
        @name_space.response(200, "Healthy")
        def get(self):
            """
            Resource get for checking health of application.
            
            Returns:
                json: Status
            """
            return jsonify({"status": "Healthy"})

    @name_space.route("/askConfluence")
    class askConfluence(Resource):
        """Get answer to a question from Confluence documents."""

        @name_space.doc(
            responses={
                200: "Success",
                500: "Internal Server error",
            }
        )
        @name_space.expect(parser_question)
        def post(self):
            """
            Post endpoint to get answer for question from Confluence.

            Returns:
                answer (str): Answer to question.
            """
            question = parser_question.parse_args().get("Question")
            try:
                return jsonify({"answer": get_answer_from_confluence(question)})
            except Exception as e:
                return app.abort(
                    500, f"Asking failed. {e}"
                )

    return flask_app


def create_parser(question):
    """Create parser for api."""
    parser = reqparse.RequestParser()
    parser.add_argument(question, type=str, required=True)
    return parser


if __name__ == "__main__":
    flask = create_app()
    flask.run(debug=True, host="0.0.0.0", port=8000)