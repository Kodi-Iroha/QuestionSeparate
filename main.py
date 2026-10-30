from PIL import Image

img = Image.open("test.jpg")
img = img.convert("RGB")
pixels = img.load()
width, height = img.size

target = (255, 0, 0)  # 你想找的紅色
tolerance = 75         # 容許誤差，數字越大越寬鬆

found_coords = [0]

def valid(y, coords):
    for i in coords: 
        if y <= i + 50 and y >= i - 50: 
            return False
    return True


for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        if (abs(r - target[0]) <= tolerance and
            abs(g - target[1]) <= tolerance and
            abs(b - target[2]) <= tolerance):
            if valid(y, found_coords): 
                found_coords.append((y))
            # found_coords.append((y))
found_coords.append(height)
    

print(found_coords)

cut = []

for k in range(len(found_coords)): 
    if k != len(found_coords) - 1: 
        cut.append((0, found_coords[k], width, found_coords[k + 1]))

for j in range(len(cut)): 
    cutting = img.crop(cut[j])
    cutting.save(f"彩葉 {j + 1}.jpg")

print("Done")

