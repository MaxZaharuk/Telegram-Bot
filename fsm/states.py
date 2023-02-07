from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    start_state = State()
    forex_instrument = State()
    digital_instrument = State()
    time_series = State()
    choose_mode = State()
    subscribe = State()
