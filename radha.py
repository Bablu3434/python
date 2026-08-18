from PIL import Image, ImageDraw, ImageFont

# Canvas
width, height = 900, 700
img = Image.new("RGB", (width, height), "#f8e7c4")
draw = ImageDraw.Draw(img)

# Background - sunset
for y in range(height):
    r = int(255 - (y / height) * 40)
    g = int(210 - (y / height) * 60)
    b = int(150 - (y / height) * 30)
    draw.line((0, y, width, y), fill=(r, g, b))

# Moon
draw.ellipse((680, 70, 790, 180), fill="#fff4c2")

# Decorative flowers
flowers = [
    (80, 100), (150, 160), (760, 250),
    (830, 140), (100, 500), (800, 520)
]

for x, y in flowers:
    draw.ellipse((x-12, y-25, x+12, y+5), fill="#e91e63")
    draw.ellipse((x-25, y-12, x+5, y+12), fill="#ff4081")
    draw.ellipse((x-5, y-12, x+25, y+12), fill="#ff4081")
    draw.ellipse((x-12, y+5, x+12, y+30), fill="#e91e63")
    draw.ellipse((x-6, y-6, x+6, y+6), fill="#ffd54f")

# -------------------------
# KRISHNA
# -------------------------

# Body
draw.ellipse((420, 210, 570, 430), fill="#4169e1")

# Face
draw.ellipse((440, 130, 550, 250), fill="#4169e1")

# Hair
draw.arc((425, 105, 565, 245), 180, 360, fill="#222222", width=18)

# Eyes
draw.ellipse((465, 175, 477, 187), fill="black")
draw.ellipse((510, 175, 522, 187), fill="black")

# Smile
draw.arc((475, 185, 515, 220), 10, 170, fill="#8b0000", width=3)

# Peacock feather
draw.line((500, 135, 535, 55), fill="#228b22", width=6)
draw.ellipse((515, 35, 555, 100), fill="#008000")
draw.ellipse((523, 45, 547, 88), fill="#00bfff")
draw.ellipse((530, 52, 542, 72), fill="#ffd700")

# Yellow clothes
draw.polygon(
    [(420, 350), (570, 350), (620, 600), (370, 600)],
    fill="#ffd700"
)

# Necklace
draw.arc((445, 230, 545, 330), 0, 180, fill="#ffd700", width=8)

# -------------------------
# RADHA
# -------------------------

# Body
draw.ellipse((250, 220, 410, 450), fill="#f0a080")

# Face
draw.ellipse((275, 135, 385, 255), fill="#f0a080")

# Hair
draw.pieslice((260, 110, 400, 270), 180, 360, fill="#301934")

# Eyes
draw.ellipse((300, 175, 312, 187), fill="black")
draw.ellipse((350, 175, 362, 187), fill="black")

# Smile
draw.arc((315, 190, 350, 220), 10, 170, fill="#8b0000", width=3)

# Bindi
draw.ellipse((328, 160, 337, 169), fill="#d00000")

# Radha dress
draw.polygon(
    [(250, 350), (410, 350), (470, 600), (190, 600)],
    fill="#d81b60"
)

# Dress decoration
for x in range(220, 451, 45):
    draw.ellipse((x, 480, x+15, 495), fill="#ffd700")

# Dupatta
draw.polygon(
    [(280, 260), (390, 250), (450, 450), (390, 430)],
    fill="#ff80ab"
)

# -------------------------
# FLUTE
# -------------------------

draw.line((400, 300, 570, 270), fill="#8b4513", width=10)

for x in range(430, 560, 30):
    draw.ellipse((x, 282, x+8, 290), fill="#222222")

# -------------------------
# VRINDAVAN TREES
# -------------------------

for x in [40, 120, 700, 850]:
    draw.rectangle((x, 400, x+20, 600), fill="#704214")
    draw.ellipse((x-50, 330, x+70, 450), fill="#228b22")
    draw.ellipse((x-30, 290, x+80, 400), fill="#2e8b57")

# Grass
draw.rectangle((0, 600, 900, 700), fill="#4caf50")

# Title
try:
    font = ImageFont.truetype("arial.ttf", 32)
except:
    font = ImageFont.load_default()

draw.text(
    (285, 630),
    "Radha Krishna",
    fill="#fff8dc",
    font=font
)

# Save
img.save("radha_krishna.png")

# Show
img.show()

print("Radha Krishna image successfully created!")