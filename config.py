from environs import Env
from pathlib import Path

env = Env()
env.read_env()

EMAIL = env.str('EMAIL')
PASSWORD = env.str('PASSWORD')
SIGN_IN_URL = env.str('SIGN_IN_URL')
TEMPLATE_URL = env.str('TEMPLATE_URL')
BASE_DIR = str(Path(__file__).resolve().parent)