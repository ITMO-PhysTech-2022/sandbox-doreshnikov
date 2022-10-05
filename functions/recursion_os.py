import os, pathlib


# os, pathlib
def walk(path):
    for item in os.listdir(path):
        # path = 'C:/Users/.../Pictures'
        # item = 'sunset.jpg'
        # full_path = 'C:/Users/.../Pictures/sunset.jpg'
        full_path = f'{path}/{item}'
        descriptor = pathlib.Path(full_path)
        if descriptor.is_file():
            # full_path = 'C:/x.y/sunset.jpg'
            # full_path.split('.') = ['C:/x', 'y/sunset', 'jpg']
            print(full_path.split('.')[-1])
        elif descriptor.is_dir():
            walk(full_path)


walk('C:/Users/jetbrains/Pictures')