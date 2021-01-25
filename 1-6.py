from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
Aerin.postToChat("I'm watching you")
while True:
    x,y,z = Aerin.player.getTilePos()
    Aerin.postToChat(" X:"+str(x)+" Y:"+str(y)+" Z:"+str(z))
            