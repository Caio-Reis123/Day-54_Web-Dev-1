class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticaded_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authenticaded_decorator
def create_blog_post(user):
    print(f'This is {user.name}s new blog post.')

new_user = User('Caio')
new_user.is_logged_in = True
create_blog_post(new_user)