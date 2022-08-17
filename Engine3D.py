from cgitb import grey
from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, greyscale, hologram, invertedcolor, randomstatic, unlit, gourad, toon, glow, textureBlend, pinkjelly, toongreyscale, heatmap

width = 960
height = 540

rend = Renderer(width, height)

#Posiciones de camara y modelos
modelPosition1 = V3(2, 0, 0)
modelPosition2 = V3(3, 0, 0)
modelPosition3 = V3(4, 0, 0)
modelPosition4 = V3(5, 0, 0)
modelPosition5 = V3(2, 1.4, 0)
modelPosition6 = V3(3, 1.4, 0)
modelPosition7 = V3(4, 1.4, 0)
modelPosition8 = V3(5, 1.4, 0)
mediumShotPos = V3(5.3, 1, 3)

lookatPos = V3(4, 1, 0)
rend.glLookAt(lookatPos, mediumShotPos) 

###Renderizado de los modelos y texturas

rend.active_texture = Texture("models/seraphine.bmp")
#Escala de grises basado en el Toon shader
rend.active_shader = toongreyscale
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition1,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))


#Shader que intenta imitar el aspecto de una gelatina rosada
rend.active_texture = Texture("models/seraphine.bmp")
rend.active_shader = pinkjelly
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition2,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))


#Escala de grises basica
rend.active_shader = greyscale
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition3,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))

#Mapa de calor
rend.active_shader = heatmap
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition4,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))

#Shader con colores invertidos de la textura
rend.active_shader = invertedcolor
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition6,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))

#Shader de comparacion (Original)
rend.active_shader = gourad
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition5,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))

#Shader estatica random
rend.active_shader = randomstatic
rend.glLoadModel("models/fallguy.obj",
                translate = modelPosition7,
                scale = V3(0.3,0.3,0.3),
                rotate = V3(0,25,0))

rend.glFinish("output.bmp")

