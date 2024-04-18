from gui import main
from app_logger import get

if __name__ == '__main__':
    get("app", "w").debug("App started")
    main()
