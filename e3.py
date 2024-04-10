from ursina import *
from ursina.prefabs.first_person_controller import *

application.blender_paths['default'] = Path("/mnt/e/SteamLibrary/steamapps/common/Blender/")

app = Ursina()

maze = Entity(model='maze',
              texture = 'brick'
              )

player = FirstPersonController(y=100)

app.run()