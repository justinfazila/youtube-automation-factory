import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Ensure directory structure
os.makedirs("assets/branding", exist_ok=True)
os.makedirs("assets/thumbnails/video-1", exist_ok=True)
os.makedirs("assets/canva-automation", exist_ok=True)

# System Fonts
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
C_DARK_BG   = (10, 22, 40, 255)       # #0A1628
C_MID_BG    = (30, 58, 95, 255)       # #1E3A5F
C_GOLD      = (255, 215, 0, 255)      # #FFD700
C_RED       = (255, 40, 40, 255)      # #FF2828
C_CYAN      = (0, 255, 255, 255)      # #00FFFF
C_WHITE     = (255, 255, 255, 255)    # #FFFFFF
C_BLACK     = (0, 0, 0, 255)          # #000000

def create_gradient_bg(w, h, c1=(10,22,40), c2=(30,58,95), diagonal=True):
    base = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(base)
    for y in range(0, h, 2):
        factor = (y / h) if not diagonal else ((y / h + 0.3) / 1.3)
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        draw.rectangle([0, y, w, y+2], fill=(r, g, b, 255))
    return base

def draw_text_with_outline(draw, pos, text, font, fill_color, outline_color=(0,0,0,255), outline_width=8, align="left"):
    x, y = pos
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    
    if align == "center":
        x = x - text_w // 2
    elif align == "right":
        x = x - text_w

    # Outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width*outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
                
    # Shadow
    draw.text((x + outline_width//2 + 3, y + outline_width//2 + 5), text, font=font, fill=(0, 0, 0, 180))
    # Main Text
    draw.text((x, y), text, font=font, fill=fill_color)
    return text_w

def draw_lightning_bolt(draw, cx, cy, size, color=C_GOLD, outline=(0,0,0,255)):
    s = size
    pts = [
        (cx + s*0.12, cy - s*0.5),
        (cx - s*0.32, cy + s*0.05),
        (cx + s*0.06, cy + s*0.05),
        (cx - s*0.12, cy + s*0.5),
        (cx + s*0.38, cy - s*0.05),
        (cx - s*0.02, cy - s*0.05),
    ]
    draw.polygon([(p[0]+3, p[1]+3) for p in pts], fill=outline)
    draw.polygon([(p[0]-3, p[1]-3) for p in pts], fill=outline)
    draw.polygon(pts, fill=color)

def draw_hologram_ui(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=16, fill=(0, 255, 255, 25), outline=C_CYAN, width=3)
    draw.line([x+20, y+30, x+w-20, y+30], fill=C_CYAN, width=2)
    draw.line([x+20, y+55, x+w*0.65, y+55], fill=C_GOLD, width=4)
    draw.line([x+20, y+80, x+w*0.85, y+80], fill=C_CYAN, width=2)
    draw.ellipse([x+w-35, y+20, x+w-18, y+37], fill=C_GOLD)
    draw.ellipse([x+w-60, y+20, x+w-43, y+37], fill=C_CYAN)

def draw_watermark(img, pos=(30, 25)):
    draw = ImageDraw.Draw(img)
    x, y = pos
    f1 = get_font(FONT_BOLD, 18)
    f2 = get_font(FONT_SEMI, 11)
    
    draw.rounded_rectangle([x, y, x + 235, y + 52], radius=12, fill=(10, 22, 40, 235), outline=C_GOLD, width=2)
    draw_lightning_bolt(draw, x + 22, y + 26, 32, color=C_GOLD)
    draw.text((x + 45, y + 8), "LE BON RACCOURCI", font=f1, fill=C_WHITE)
    draw.text((x + 45, y + 30), "UN PROBLÈME • UNE DÉMO", font=f2, fill=C_CYAN)

def draw_character_illustration(img, bbox, expression="surprised"):
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = bbox
    cx = (x1 + x2) // 2
    w = x2 - x1
    h = y2 - y1

    # Cyan Aura Glow
    for r in range(40, 0, -5):
        draw.ellipse([cx - w//2 - r, y1 + h//4 - r, cx + w//2 + r, y2 + r], fill=(0, 255, 255, 8))

    # Suit
    suit_poly = [
        (x1 - 20, y2),
        (cx - w//3, y1 + int(h*0.55)),
        (cx, y1 + int(h*0.75)),
        (cx + w//3, y1 + int(h*0.55)),
        (x2 + 20, y2)
    ]
    draw.polygon(suit_poly, fill=(20, 35, 60))
    draw.polygon(suit_poly, fill=None, outline=(0, 255, 255), width=2)
    
    # Shirt & Tie
    draw.polygon([(cx - 25, y1 + int(h*0.58)), (cx, y2), (cx + 25, y1 + int(h*0.58))], fill=(240, 240, 250))
    draw.polygon([(cx - 8, y1 + int(h*0.60)), (cx + 8, y1 + int(h*0.60)), (cx + 12, y2), (cx - 12, y2)], fill=(220, 30, 30))

    # Neck
    neck = [cx - 22, y1 + int(h*0.48), cx + 22, y1 + int(h*0.58)]
    draw.rectangle(neck, fill=(245, 195, 160))
    
    # Head
    head_bbox = [cx - int(w*0.28), y1 + int(h*0.12), cx + int(w*0.28), y1 + int(h*0.50)]
    draw.ellipse(head_bbox, fill=(255, 205, 170))
    
    # Hair
    hair_poly = [
        (cx - int(w*0.30), y1 + int(h*0.25)),
        (cx - int(w*0.28), y1 + int(h*0.10)),
        (cx, y1 + int(h*0.06)),
        (cx + int(w*0.28), y1 + int(h*0.10)),
        (cx + int(w*0.30), y1 + int(h*0.25)),
        (cx + int(w*0.18), y1 + int(h*0.18)),
        (cx, y1 + int(h*0.15)),
        (cx - int(w*0.18), y1 + int(h*0.18)),
    ]
    draw.polygon(hair_poly, fill=(40, 25, 15))

    # Eyes (Wide)
    eye_y = y1 + int(h*0.28)
    draw.ellipse([cx - int(w*0.16), eye_y - 12, cx - int(w*0.04), eye_y + 12], fill=C_WHITE, outline=C_BLACK, width=2)
    draw.ellipse([cx + int(w*0.04), eye_y - 12, cx + int(w*0.16), eye_y + 12], fill=C_WHITE, outline=C_BLACK, width=2)
    
    # Pupils
    draw.ellipse([cx - int(w*0.11), eye_y - 6, cx - int(w*0.07), eye_y + 6], fill=(10, 50, 100))
    draw.ellipse([cx + int(w*0.07), eye_y - 6, cx + int(w*0.11), eye_y + 6], fill=(10, 50, 100))
    
    # Eyebrows high
    draw.line([cx - int(w*0.18), eye_y - 22, cx - int(w*0.03), eye_y - 18], fill=(40, 25, 15), width=5)
    draw.line([cx + int(w*0.03), eye_y - 18, cx + int(w*0.18), eye_y - 22], fill=(40, 25, 15), width=5)

    # Mouth open wide
    mouth_y = y1 + int(h*0.40)
    draw.ellipse([cx - 18, mouth_y - 15, cx + 18, mouth_y + 18], fill=(120, 20, 20), outline=C_BLACK, width=3)
    draw.ellipse([cx - 12, mouth_y - 10, cx + 12, mouth_y - 2], fill=C_WHITE)

    # Glasses / Reflets
    draw.rectangle([cx - int(w*0.22), eye_y - 16, cx - int(w*0.02), eye_y + 16], outline=C_CYAN, width=3)
    draw.rectangle([cx + int(w*0.02), eye_y - 16, cx + int(w*0.22), eye_y + 16], outline=C_CYAN, width=3)
    draw.line([cx - int(w*0.02), eye_y, cx + int(w*0.02), eye_y], fill=C_CYAN, width=3)


# ==========================================
# 1. LOGO GENERATION (800x800)
# ==========================================
def generate_logo():
    print("Generating logo_800x800.png...")
    img = create_gradient_bg(800, 800, (10, 22, 40), (20, 45, 80))
    draw = ImageDraw.Draw(img)
    
    # Outer Glowing Ring (Gold + Cyan)
    draw.ellipse([80, 80, 720, 720], fill=(15, 30, 55, 255), outline=C_GOLD, width=16)
    draw.ellipse([68, 68, 732, 732], fill=None, outline=C_CYAN, width=4)
    
    # Central Shortcut Badge
    draw_lightning_bolt(draw, 400, 310, 220, color=C_GOLD)
    
    # Text
    f_title = get_font(FONT_BOLD, 72)
    f_sub = get_font(FONT_SEMI, 32)
    
    draw_text_with_outline(draw, (400, 470), "LE BON RACCOURCI", f_title, C_WHITE, outline_width=8, align="center")
    
    # Slogan pill
    draw.rounded_rectangle([150, 580, 650, 640], radius=30, fill=(15, 32, 58, 240), outline=C_GOLD, width=3)
    draw.text((400, 592), "UN PROBLÈME • UNE DÉMO • UNE SOLUTION", font=f_sub, fill=C_CYAN, anchor="mm")
    
    img.save("assets/branding/logo_800x800.png", "PNG")
    img.convert("RGB").save("assets/branding/logo_800x800.jpg", "JPEG", quality=95)
    print(" -> Saved assets/branding/logo_800x800.png & jpg")


# ==========================================
# 2. BANNER GENERATION (2560x1440, Safe Area 1546x423)
# ==========================================
def generate_banner():
    print("Generating banner_2560x1440.png...")
    img = create_gradient_bg(2560, 1440, (8, 18, 35), (25, 55, 95))
    draw = ImageDraw.Draw(img)
    
    # Safe area guides / background glow inside safe area (y: 508 to 931)
    draw.rectangle([0, 508, 2560, 931], fill=(12, 28, 52, 255))
    
    # Circuit overlay
    for x in range(100, 2500, 300):
        draw.line([x, 508, x+100, 931], fill=(0, 255, 255, 20), width=2)
        
    # Safe area box (507 to 2053)
    # Left Icon Badge
    draw_lightning_bolt(draw, 640, 720, 260, color=C_GOLD)
    
    # Titles inside safe area
    f_banner_title = get_font(FONT_BOLD, 95)
    f_slogan = get_font(FONT_BOLD, 36)
    f_schedule = get_font(FONT_SEMI, 28)
    
    draw_text_with_outline(draw, (820, 550), "LE BON RACCOURCI", f_banner_title, C_GOLD, outline_width=10)
    draw.text((825, 680), "UN PROBLÈME  •  UNE DÉMO  •  UNE SOLUTION", font=f_slogan, fill=C_WHITE)
    
    # Schedule Pill
    draw.rounded_rectangle([825, 760, 1520, 830], radius=20, fill=(18, 40, 72, 255), outline=C_CYAN, width=3)
    draw_lightning_bolt(draw, 855, 795, 40, color=C_GOLD)
    draw.text((885, 775), "NOUVELLE VIDÉO CHAQUE MARDI À 18H", font=f_schedule, fill=C_CYAN)
    
    # Right side Hologram UI inside safe area
    draw_hologram_ui(draw, 1680, 580, 320, 260)
    
    img.save("assets/branding/banner_2560x1440.png", "PNG")
    img.convert("RGB").save("assets/branding/banner_2560x1440.jpg", "JPEG", quality=95)
    print(" -> Saved assets/branding/banner_2560x1440.png & jpg")


# ==========================================
# 3. THUMBNAIL VAR 1: CLASSIC HIGH-CONTRAST (1280x720)
# ==========================================
def generate_thumb_v1():
    print("Generating video-1_var1_classic.png...")
    img = create_gradient_bg(1280, 720, (10, 22, 40), (25, 50, 85))
    draw = ImageDraw.Draw(img)
    
    # Left 40%: Character & Hologram UI
    draw_character_illustration(img, (50, 160, 480, 680), "surprised")
    draw_hologram_ui(draw, 280, 320, 240, 200)
    
    # Right 60%: Massive Text
    f_huge = get_font(FONT_BOLD, 140)
    f_sub  = get_font(FONT_BOLD, 38)
    
    # "7" in giant Red
    draw_text_with_outline(draw, (530, 130), "7", f_huge, C_RED, outline_width=12)
    # "SECRETS" in Gold
    draw_text_with_outline(draw, (640, 130), "SECRETS", f_huge, C_GOLD, outline_width=12)
    # "IA" in Cyan
    draw_text_with_outline(draw, (530, 310), "IA", f_huge, C_CYAN, outline_width=12)
    
    # Subtitle Pill
    draw.rounded_rectangle([530, 500, 1220, 580], radius=16, fill=(180, 20, 20, 255), outline=C_GOLD, width=3)
    draw_text_with_outline(draw, (550, 515), "QUE LES ENTREPRENEURS IGNORENT !", f_sub, C_WHITE, outline_width=4)
    
    # Watermark Logo
    draw_watermark(img, (30, 25))
    
    img.save("assets/thumbnails/video-1/video-1_var1_classic.png", "PNG")
    img.convert("RGB").save("assets/thumbnails/video-1/video-1_var1_classic.jpg", "JPEG", quality=95)
    print(" -> Saved assets/thumbnails/video-1/video-1_var1_classic.png & jpg")


# ==========================================
# 4. THUMBNAIL VAR 2: CENTERED HERO (1280x720)
# ==========================================
def generate_thumb_v2():
    print("Generating video-1_var2_centered.png...")
    img = create_gradient_bg(1280, 720, (15, 30, 55), (8, 16, 30))
    draw = ImageDraw.Draw(img)
    
    # Top Arc Text
    f_huge = get_font(FONT_BOLD, 125)
    f_cta  = get_font(FONT_BOLD, 36)
    
    # Top Banner Text
    draw_text_with_outline(draw, (640, 40), "7 SECRETS IA", f_huge, C_GOLD, outline_width=12, align="center")
    
    # Center Hero Character
    draw_character_illustration(img, (420, 180, 860, 640), "surprised")
    draw_hologram_ui(draw, 490, 400, 300, 180)
    
    # Bottom CTA Banner
    draw.rectangle([0, 620, 1280, 720], fill=(180, 20, 20, 240))
    draw.line([0, 620, 1280, 620], fill=C_GOLD, width=4)
    draw_text_with_outline(draw, (640, 640), "▼ REGARDEZ JUSQU'AU BOUT ! ▼", f_cta, C_WHITE, outline_width=6, align="center")
    
    # Watermark Logo
    draw_watermark(img, (30, 25))
    
    img.save("assets/thumbnails/video-1/video-1_var2_centered.png", "PNG")
    img.convert("RGB").save("assets/thumbnails/video-1/video-1_var2_centered.jpg", "JPEG", quality=95)
    print(" -> Saved assets/thumbnails/video-1/video-1_var2_centered.png & jpg")


# ==========================================
# 5. THUMBNAIL VAR 3: SPLIT DIAGONAL 45° (1280x720)
# ==========================================
def generate_thumb_v3():
    print("Generating video-1_var3_diagonal.png...")
    img = create_gradient_bg(1280, 720, (10, 22, 40), (30, 60, 100))
    draw = ImageDraw.Draw(img)
    
    # Diagonal Split Line (45deg from top-right to bottom-left)
    draw.polygon([(750, 0), (1280, 0), (1280, 720), (450, 720)], fill=(15, 35, 65, 255))
    draw.line([(750, 0), (450, 720)], fill=C_CYAN, width=6)
    draw.line([(755, 0), (455, 720)], fill=C_GOLD, width=4)
    
    # Lightning bolt on diagonal
    draw_lightning_bolt(draw, 600, 360, 140, color=C_GOLD)
    
    # Top-Left Zone: Text & NOUVEAU Badge
    draw.rounded_rectangle([50, 100, 240, 150], radius=10, fill=C_RED, outline=C_GOLD, width=2)
    f_badge = get_font(FONT_BOLD, 22)
    draw.text((145, 125), "NOUVEAU", font=f_badge, fill=C_WHITE, anchor="mm")
    
    f_huge = get_font(FONT_BOLD, 120)
    f_sub  = get_font(FONT_SEMI, 34)
    
    draw_text_with_outline(draw, (50, 170), "7 SECRETS", f_huge, C_GOLD, outline_width=12)
    draw_text_with_outline(draw, (50, 330), "IA 2026", f_huge, C_CYAN, outline_width=12)
    
    draw.text((50, 520), "ACCÉLÉREZ VOTRE IA & BROWSER", font=f_sub, fill=C_WHITE)
    
    # Bottom-Right Zone: Character & Hologram
    draw_character_illustration(img, (720, 180, 1180, 680), "surprised")
    draw_hologram_ui(draw, 880, 350, 280, 190)
    
    # Watermark Logo
    draw_watermark(img, (30, 25))
    
    img.save("assets/thumbnails/video-1/video-1_var3_diagonal.png", "PNG")
    img.convert("RGB").save("assets/thumbnails/video-1/video-1_var3_diagonal.jpg", "JPEG", quality=95)
    print(" -> Saved assets/thumbnails/video-1/video-1_var3_diagonal.png & jpg")


if __name__ == "__main__":
    generate_logo()
    generate_banner()
    generate_thumb_v1()
    generate_thumb_v2()
    generate_thumb_v3()
    print("\n✅ ALL BRANDING & THUMBNAIL ASSETS SUCCESSFULLY GENERATED!")
