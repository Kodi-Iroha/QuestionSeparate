
from PIL import Image
import pymupdf

def pdf(path):
    doc = pymupdf.open(path)
    for l in len(doc):
        page = doc.load_page(l)          
        pix = page.get_pixmap(dpi=200)         
        pix.save(f"pdf{l}.png")
    doc.close()
    print("pdf Done")

def valid(y, coords):
    for i in coords: 
        if y <= i + 50 and y >= i - 50: 
            return False
    return True

def kaguya(picture: str, change: int):
    img = Image.open(picture)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size
    
    target = (255, 0, 0) 
    tolerance = change 
    found_coords = [0]

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if (abs(r - target[0]) <= tolerance and
                abs(g - target[1]) <= tolerance and
                abs(b - target[2]) <= tolerance):
                if valid(y, found_coords): 
                    found_coords.append((y))

    found_coords.append(height)
    
    print(found_coords)
    cut = []

    for k in range(len(found_coords)): 
        if k != len(found_coords) - 1: 
            cut.append((0, found_coords[k], width, found_coords[k + 1]))
    for j in range(len(cut)): 
        cutting = img.crop(cut[j])
        cutting.save(f"彩葉{j + 1}.png")
    print("picture done")


print("""
+----------------+
| 1| pdf to image|
| 2| cut image   | 
+----------------+ 
""")

def main(): 
    ex = True
    while ex: 
        function = int(input())
        if function == 1:
            pdf("test.pdf")
        elif function == 2: 
            kaguya("test.jpg", 75)
        else: 
            ex = False

main() 
