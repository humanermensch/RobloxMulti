import win32api
import win32event
import winerror
import sys

def create_mutex(mutex_name):
    # give credits please thanks <3
    mutex = win32event.CreateMutex(None, False, mutex_name)

    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        return None
    else:
        print(f"Created '{mutex_name}' created successfully.")
        return mutex

if __name__ == "__main__":
    mutex_name = "ROBLOX_singletonEvent"
    mutex = create_mutex(mutex_name)

    if not mutex:
        sys.exit(1)

    while True:
        pass