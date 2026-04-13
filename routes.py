from flask import request, jsonify

def register_routes(app, session, customers):

    @app.route("/register", methods=["POST"])
    def register():
        data = request.json

        new_user = customers.insert().values(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )

        session.execute(new_user)
        session.commit()

        return jsonify({"message": "User Registered Successfully"})
