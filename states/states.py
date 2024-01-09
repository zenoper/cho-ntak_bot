from aiogram.dispatcher.filters.state import StatesGroup, State

class user_states(StatesGroup):
    set_val = State()
    set_key = State()
    confirmation = State()