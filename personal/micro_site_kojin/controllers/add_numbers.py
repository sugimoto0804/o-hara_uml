from app_logic import set_first_value,set_second_value, get_my_additon
from utils import render_template


def add_numbers():
    set_first_value()
    set_second_value()
    add_numbers = get_my_additon()

    return render_template("boundaries/add_numbers.html",add_numbers = add_numbers)