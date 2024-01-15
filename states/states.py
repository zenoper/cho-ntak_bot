from aiogram.dispatcher.filters.state import StatesGroup, State

class user_states(StatesGroup):
    start = State()
    set_val = State()
    set_key = State()
    confirmation = State()


class delete_states(StatesGroup):
    select = State()
    delete = State()