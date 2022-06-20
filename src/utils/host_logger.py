from colorama import init, reinit
from colorama import Fore, Back, Style

__colorama_initialized = False
if __colorama_initialized == False:
    init()
    __colorama_initialized = True
else:
    reinit()

class HostLogger:
    _lastValues: dict = {}

    def __init__(self) -> None:
        pass

    def log_loss(self, val, name: str):
        lastVal = self._lastValues.get(name)
        if lastVal is None:
            print(self.__get_first_loss_str(val, name))
        elif val < lastVal:
            print(self.__get_loss_decreased_str(val, name))
        elif val == lastVal:
            print(self.__get_loss_stable_str(val, name))
        else:
            print(self.__get_loss_increased_str(val, name))
        
        self._lastValues[name] = val

    def __get_loss_name_str(self, name: str):
        if name is None:
            return ''
        return '%s: ' % name

    def __get_first_loss_str(self, val, name: str)-> str:
        return Fore.LIGHTYELLOW_EX + self.__get_loss_name_str(name) + ('%s' % (val))
    
    def __get_loss_decreased_str(self, val, name: str)-> str:
        return Fore.GREEN + self.__get_loss_name_str(name) + ('%s' % (val))
    
    def __get_loss_increased_str(self, val, name: str)-> str:
        return Fore.RED + self.__get_loss_name_str(name) + ('%s' % (val))
    
    def __get_loss_stable_str(self, val, name: str)-> str:
        return Fore.LIGHTYELLOW_EX + self.__get_loss_name_str(name) + ('%s' % (val))
    

    def log_warning(self, message: str):
        print(self.__get_warning_str(message))

    def __get_warning_str(self, message: str):
        return Fore.LIGHTYELLOW_EX + ('warning: %s' % message)

    
    def log_info(self, message: str):
        print(self.__get_info_str(message))
    
    def __get_info_str(self, message: str):
        return Fore.WHITE + ('info: %s' % message)
    
    
    def log_important(self, message: str):
        print(self.__get_important_str(message))

    def __get_important_str(self, message: str):
        return Back.WHITE + Fore.BLACK + ('info: %s' % message)


HostLoggerInstance = HostLogger()