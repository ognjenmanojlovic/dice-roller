from flask import Blueprint, jsonify, request

from .errors import InvalidDiceError, DiceAlreadyExistsError

api_bp = Blueprint("api", __name__)

# In-memory “database”
dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20},
]

@api_bp.route("/dices", methods=["GET", "POST"])
def handle_dice_requests():
    if request.method == "GET":
        # Simply return all available dice
        return jsonify(available_dices=dices)

    # POST: create a new dice entry
    payload = request.get_json() or {}

    # Validate the numberOfSides value
    try:
        sides = int(payload.get("numberOfSides", 0))
    except (TypeError, ValueError):
        raise InvalidDiceError()

    if sides <= 1:
        raise InvalidDiceError()

    new_dice = {"numberOfSides": sides}

    if new_dice in dices:
        raise DiceAlreadyExistsError()

    dices.append(new_dice)
    return jsonify(message="dice created"), 201


@api_bp.errorhandler(InvalidDiceError)
def handle_invalid_dice(error: InvalidDiceError):
    return jsonify(message=error.message), 400


@api_bp.errorhandler(DiceAlreadyExistsError)
def handle_dice_already_exists(error: DiceAlreadyExistsError):
    return jsonify(message=error.message), 409


@api_bp.errorhandler(Exception)
def handle_unexpected_error(error: Exception):
    return jsonify(message="An unknown error occurred"), 500
