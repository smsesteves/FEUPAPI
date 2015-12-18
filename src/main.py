import flask
import food_menu

app = flask.Flask("OFEUPAPI - Food Menu")


@app.errorhandler(404)
def entry_point(error):
    return flask.jsonify(dict(
        error="You're probably looking for /food_menu/cafeteria or /food_menu/restaurant"
    )), 400


@app.route("/food_menu/cafeteria")
def cafeteria():
    code = 200
    menu = food_menu.get_menu_cafeteria()
    menu = food_menu.prepare_menu(menu, "cafeteria")
    return flask.jsonify(menu), code


@app.route("/food_menu/restaurant")
def restaurant():
    code = 200
    menu = food_menu.get_menu_restaurant()
    menu = food_menu.prepare_menu(menu, "restaurant")
    return flask.jsonify(menu), code

if __name__ == "__main__":
    app.run()  # Default port is 5000
