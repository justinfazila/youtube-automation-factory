import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Create target directories
os.makedirs("assets/branding", exist_ok=True)
os.makedirs("assets/thumbnails/video-1", exist_ok=True)
os.makedirs("assets/canva-automation", exist_ok=True)

# Select best available system fonts
FONT_BOLD = "C:\\Windows\\Fonts\\seguibl.ttf"  # Segoe UI Black
FONT_SEMI = "C:\\Windows\\Fonts\\seguisb.ttf"  # Segoe UI Semibold
FONT_MAIN = "C:\\Windows\\Fonts\\arialbd.ttf"  # Arial Bold
FONT_REG  = "C:\\Windows\\Fonts\\arial.ttf"    # Arial Regular

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

# Colors
C_DARK_BG   = (10, 22, 40)       # #0A1628
C_MID_BG    = (30, 58, 95)       # #1E3A5F
C_GOLD      = (255, 215, 0)      # #FFD700
C_RED       = (255, 40, 40)      # #FF2828
C_CYAN      = (0, 255, 255)      # #00FFFF
C_WHITE     = (255, 255, 255)    # #FFFFFF
C_BLACK     = (0, 0, 0)          # #000000
C_DARK_PILL = (15, 32, 58)

def draw_gradient_bg(width, height, c1=C_DARK_BG, c2=C_MID_BG, diagonal=True):
    img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(0, width, 4):  # step for speed
            if diagonal:
                factor = (x / width + y / height) / 2.0
            else:
                factor = y / height
            r = int(c1[0] + (c2[0] - c1[0]) * factor)
            g = int(c1[1] + (c2[1] - c1[1]) * factor)
            b = int(c1[2] + (c2[2] - c1[2]) * factor)
            draw.rectangle([x, y, x+4, y+1], fill=(r, g, b, 255))
    return img

def add_circuit_lines(img):
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    # Subtle circuit pattern
    lines = [
        [(0, int(h*0.2)), (int(w*0.25), int(h*0.2)), (int(w*0.35), int(h*0.35)), (int(w*0.6), int(h*0.35))],
        [(int(w*0.4), 0), (int(w*0.4), int(h*0.15)), (int(w*0.55), int(h*0.3)), (w, int(h*0.3))],
        [(0, int(h*0.75)), (int(w*0.3), int(h*0.75)), (int(w*0.45), int(h*0.6)), (int(w*0.8), int(h*0.6))],
        [(int(w*0.15), h), (int(w*0.15), int(h*0.8)), (int(w*0.35), int(h*0.65)), (int(w*0.35), int(h*0.5))]
    ]
    for line in lines:
        draw.line(line, fill=(0, 255, 255, 35), width=3)
        for pt in line:
            draw.ellipse([pt[0]-5, pt[1]-5, pt[0]+5, pt[1]+5], fill=(0, 255, 255, 60))
            draw.ellipse([pt[0]-2, pt[1]-2, pt[0]+2, pt[1]+2], fill=(255, 255, 255, 120))

def draw_text_with_outline(draw, pos, text, font, fill_color, outline_color=C_BLACK, outline_width=8, align="left"):
    x, y = pos
    # Calculate bounding box for alignment
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    
    if align == "center":
        x = x - text_w // 2
    elif align == "right":
        x = x - text_w

    # Draw outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width*outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
                
    # Draw drop shadow
    draw.text((x + outline_width//2, y + outline_width//2 + 4), text, font=font, fill=(0, 0, 0, 180))
    
    # Draw main text
    draw.text((x, y), text, font=font, fill=fill_color)
    return text_w

def draw_watermark_logo(img, pos=(30, 30), scale=0.6):
    draw = ImageDraw.Draw(img, "RGBA")
    x, y = pos
    font_title = get_font(FONT_BOLD, int(20 * scale))
    font_sub = get_font(FONT_SEMI, int(12 * scale))
    
    # Pill background
    pw, ph = int(240 * scale), int(54 * scale)
    draw.rounded_rectangle([x, y, x + pw, y + ph], radius=int(12*scale), fill=(10, 22, 40, 220), outline=(255, 215, 0, 200), width=int(2*scale))
    
    # Icon (Lightning/Shortcut arrow)
    ix, iy = x + int(12*scale), y + int(10*scale)
    draw.polygon([(ix+int(12*scale), iy), (ix+int(4*scale), iy+int(18*scale)), (ix+int(11*scale), iy+int(18*scale)),
                  (ix+int(8*scale), iy+int(32*scale)), (ix+int(20*scale), iy+int(12*scale)), (ix+int(12*scale), iy+int(12*scale))], fill=C_GOLD)
    
    # Text
    draw.text((x + int(42*scale), y + int(6*scale)), "LE BON RACCOURCI", font=font_title, fill=C_WHITE)
    draw.text((x + int(42*scale), y + int(28*scale)), "UN PROBLÈME • UNE DEMO", font=font_sub, fill=C_CYAN)

print("Helper functions defined.")
