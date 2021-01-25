from mcpi.minecraft import Minecraft
import time
Aerin=Minecraft.create()
x = 200
y = 200
z = 100
Aerin.player.setTilePos(x,y,z)
time.sleep(2)
x = 150
y = 150
Aerin.player.setTilePos(x,y,z)
time.sleep(2)
x = 100
y = 100
Aerin.player.setTilePos(x,y,z)