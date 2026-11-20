# utils/__init__.py: makes utils a package
# utils/helpers.py
# utils/parsers.py

# Inside utils/parsers.py: relative import from sibling
# from .helpers import clean_text

# Inside main.py (at project root): absolute import
# from utils.parsers import parse_log_line
