def log_method(method):
    def wrapper(self, *args):
        print(f"Calling method {method.__name__} with args: {args} ")
        result = method(self, *args)
        print(f"Method:{method.__name__} returned {result}")
        return result
    return wrapper
class Myclass:
    @log_method
    def say_hi(self,name):
        return f"Hi, {name}!"

obj = Myclass()
obj.say_hi("Immanuel")