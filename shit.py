from math import sqrt
from mcpi.minecraft import Minecraft
from time import sleep
import PIL.Image
mc = Minecraft.create()


lava = 10
water = 8
air = 0
grass = 2
xp, yp, zp = mc.player.getPos()

colours = ((255, 255, 255, "white"), (0, 0, 0, "black"),
           (255, 0, 0, "red"),
           (0, 255, 0, "lime"),
           (0, 0, 255, "blue"), (240, 230, 140, "SAND_STONE"), (255, 192, 203, "pink"), (100, 149, 237, "light blue"), (255, 127, 80, "orange"), (139, 69, 19, "brown"), (255, 255, 0, "yellow"), (192, 192, 192, "light gray"), (0, 255, 255, "cyan"), (255, 0, 255, "magenta"), (128, 128, 128, "gray"), (128, 128, 0, "olive"), (128, 0, 128, "purple"))
colorsss = thisdict = {
    "white": (35, 0),
    "orange": (35, 1),
    "magenta": (35, 2),
    "light blue": (35, 3),
    "yellow": (35, 4),
    "lime": (35, 5),
    "pink": (35, 6),
    "gray": (35, 7),
    "light gray": (35, 8),
    "cyan": (35, 9),
    "purple": (35, 10),
    "blue": (35, 11),
    "brown": (35, 12),
    "olive": (35, 13),
    "red": (35, 14),
    "black": (35, 15),
    "SAND_STONE": (24, 0)
}


def nearest_colour(query):
    return min(colours, key=lambda subject: sum((s - q) ** 2 for s, q in zip(subject, query)))[3]


def shit(img):

    basewidth = 100
    img = PIL.Image.open(img)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    width, height = img.size

    img_rgb = img.convert("RGBA")
    for x in range(0, width):
        for z in range(0, height):
            rgb_pixel_value = img_rgb.getpixel((x, z))
            if rgb_pixel_value[0] == 0 and rgb_pixel_value[1] == 0 and rgb_pixel_value[2] == 0 and rgb_pixel_value[3] == 0:
                continue
            named_color = nearest_colour(rgb_pixel_value[0:3])
            mc.setBlock(xp+x, 200, zp + z, colorsss[named_color])


shit("p382.png")
