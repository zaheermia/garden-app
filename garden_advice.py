def get_user_input():
    """Ask the user for the season and plant type.

    Returns:
        tuple: The season and plant type in lowercase.
    """
    season = input("Enter the season (summer or winter): ").strip().lower()
    plant_type = input("Enter the plant type (flower or vegetable): ").strip().lower()
    return season, plant_type


def get_season_advice(season):
    """Return gardening advice for the given season.

    Args:
        season (str): The season entered by the user.

    Returns:
        str: Advice for that season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice for the given plant type.

    Args:
        plant_type (str): The plant type entered by the user.

    Returns:
        str: Advice for that plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Run the garden advice program."""
    season, plant_type = get_user_input()

    # Join the season and plant advice on separate lines
    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)
    print(advice)


# Only run the program when this file is run directly
if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
