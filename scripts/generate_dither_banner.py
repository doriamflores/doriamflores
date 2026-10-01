import os
import html
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

def floyd_steinberg(gray: np.ndarray) -> np.ndarray:
    """Serpentine 1-bit Floyd-Steinberg error diffusion."""
    work = gray.astype(np.float32) / 255.0
    out = np.zeros_like(work, dtype=bool)
    height, width = work.shape
    for y in range(height):
        left_to_right = y % 2 == 0
        xs = range(width) if left_to_right else range(width - 1, -1, -1)
        direction = 1 if left_to_right else -1
        for x in xs:
            old = work[y, x]
            new = 1.0 if old >= 0.5 else 0.0
            out[y, x] = bool(new)
            err = old - new
            nx = x + direction
            if 0 <= nx < width:
                work[y, nx] += err * 7 / 16
            if y + 1 < height:
                if 0 <= x - direction < width:
                    work[y + 1, x - direction] += err * 3 / 16
                work[y + 1, x] += err * 5 / 16
                if 0 <= nx < width:
                    work[y + 1, nx] += err * 1 / 16
    return out

def point_path(points: np.ndarray) -> str:
    """Aggregate adjacent horizontal one-pixel dots into compact SVG path runs."""
    if not len(points):
        return ""
    integer = np.rint(points).astype(int)
    unique = sorted({(int(x), int(y)) for x, y in integer}, key=lambda p: (p[1], p[0]))
    chunks: list[str] = []
    i = 0
    while i < len(unique):
        x0, y = unique[i]
        x1 = x0
        i += 1
        while i < len(unique) and unique[i][1] == y and unique[i][0] <= x1 + 1:
            x1 = unique[i][0]
            i += 1
        chunks.append(f"M{x0} {y}h{x1 - x0 + 1}")
    return "".join(chunks)

def get_portrait_path(photo_path: str, offset_x=69, offset_y=140, is_dark=True):
    img = Image.open(photo_path).convert("RGB")
    w, h = img.size
    crop_size = min(w, h)
    left = (w - crop_size) // 2
    top = int((h - crop_size) * 0.2)
    crop = img.crop((left, top, left + crop_size, top + crop_size))
    target_w, target_h = 350, 370
    resized = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)

    gray = ImageOps.grayscale(resized)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    if is_dark:
        gray = ImageEnhance.Contrast(gray).enhance(1.4)
        gray = ImageEnhance.Brightness(gray).enhance(1.1)
    else:
        gray = ImageEnhance.Contrast(gray).enhance(1.3)
        gray = ImageEnhance.Brightness(gray).enhance(1.0)
    gray = gray.filter(ImageFilter.UnsharpMask(radius=2.0, percent=150, threshold=1))

    arr = np.asarray(gray)
    bits = floyd_steinberg(arr)
    active = bits if is_dark else ~bits
    ys, xs = np.where(active)
    if len(xs) == 0:
        return ""
    points = np.column_stack((offset_x + xs, offset_y + ys)).astype(np.float32)
    return point_path(points)

def generate_banner(output_path, photo_path, filter_id, is_dark=True):
    W, H = 1180, 610

    if is_dark:
        bg = "#07080e"
        panel_bg = "#0c0e17"
        panel_inner = "#101321"
        line_color = "#1f253d"
        text_white = "#f1f5f9"
        cyan_accent = "#00f3ff"
        pink_accent = "#ff007f"
        yellow_accent = "#ffe600"
        green_accent = "#00ff9f"
        purple_accent = "#b026ff"
        muted_text = "#64748b"
        line_num = "#475569"
        portrait_color = "#00f3ff"
    else:
        bg = "#f1f5f9"
        panel_bg = "#ffffff"
        panel_inner = "#f8fafc"
        line_color = "#cbd5e1"
        text_white = "#0f172a"
        cyan_accent = "#0284c7"
        pink_accent = "#db2777"
        yellow_accent = "#d97706"
        green_accent = "#059669"
        purple_accent = "#7c3aed"
        muted_text = "#64748b"
        line_num = "#94a3b8"
        portrait_color = "#0284c7"

    dither_svg_path = get_portrait_path(photo_path, offset_x=69, offset_y=140, is_dark=is_dark)

    yaml_lines = [
        (" 1", "profile:", True, purple_accent),
        (" 2", "  subject: ", False, pink_accent, "Doriam Flores", text_white),
        (" 3", "  role: ", False, pink_accent, "Senior Backend Developer & AI Integrator", text_white),
        (" 4", "  origin: ", False, pink_accent, "Lima, Perú [UTC-5] 🇵🇪", text_white),
        (" 5", "  focus: ", False, pink_accent, "Microservices · Event-Driven · AI Agents", text_white),
        (" 6", "  status: ", False, pink_accent, "Ready for Production · Sub-second Latency", green_accent),
        (" 7", "stack:", True, purple_accent),
        (" 8", "  languages: ", False, cyan_accent, "TypeScript · Node.js · Python · Go · SQL", text_white),
        (" 9", "  frameworks: ", False, cyan_accent, "NestJS · Express · GraphQL · FastAPI", text_white),
        ("10", "  databases: ", False, cyan_accent, "PostgreSQL · MySQL · MongoDB · Redis", text_white),
        ("11", "  cloud_devops: ", False, cyan_accent, "AWS (EC2/Lambda/S3) · Docker · Jenkins", text_white),
        ("12", "  messaging: ", False, cyan_accent, "Apache Kafka · RabbitMQ · WebSockets", text_white),
        ("13", "ai_engineering:", True, purple_accent),
        ("14", "  frameworks: ", False, yellow_accent, "OpenAI API · LangChain · Claude · Agents", text_white),
        ("15", "  architecture: ", False, yellow_accent, "Autonomous workflows & LLM orchestration", text_white),
        ("16", "contact:", True, purple_accent),
        ("17", "  web: ", False, cyan_accent, "doriamflores.github.io/doriamflores", text_white),
        ("18", "  linkedin: ", False, cyan_accent, "/in/doriamflores", text_white),
        ("19", "  github: ", False, cyan_accent, "@Doriamflores", text_white),
    ]

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">Doriam Flores - Live System Profile</title>',
        f'  <desc id="desc">Animated terminal profile with a dithered portrait and Neovim YAML configuration.</desc>',
        '  <defs>',
        f'    <filter id="{filter_id}" x="-10%" y="-10%" width="120%" height="120%">',
        '      <feGaussianBlur stdDeviation="2" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
        '  </defs>',

        '  <style>',
        '    .mono { font-family: "JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }',
        '  </style>',

        f'  <!-- Main Background -->',
        f'  <rect width="{W}" height="{H}" rx="16" fill="{bg}"/>',
        f'  <rect x="10" y="10" width="{W-20}" height="{H-20}" rx="14" fill="{panel_bg}" stroke="{line_color}" stroke-width="1.5"/>',

        f'  <!-- Top Window Header Bar -->',
        f'  <path d="M10 58 H{W-10}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <circle cx="38" cy="34" r="6" fill="#ff0055"/>',
        f'  <circle cx="58" cy="34" r="6" fill="#ffe600" opacity="0.9"/>',
        f'  <circle cx="78" cy="34" r="6" fill="#00ff9f"/>',

        f'  <text x="110" y="39" class="mono" font-size="13" fill="{muted_text}">nvim ~/profile.yml</text>',
        f'  <text x="265" y="39" class="mono" font-size="13" fill="{line_color}">::</text>',
        f'  <text x="285" y="39" class="mono" font-size="13" fill="{cyan_accent}" font-weight="700">DO\'0R.DEV // CYBER_CORE [ONLINE ⚡]</text>',
        f'  <text x="{W-150}" y="39" class="mono" font-size="12" fill="{green_accent}" font-weight="600">UPTIME: 99.99%</text>',

        f'  <!-- ==================== LEFT PANEL: VISUAL ID (PORTRAIT DITHERED) ==================== -->',
        f'  <rect x="35" y="76" width="418" height="500" rx="8" fill="{panel_inner}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <path d="M35 116 H453" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <text x="49" y="101" class="mono" font-size="13" font-weight="700" fill="{cyan_accent}" letter-spacing="1">⚡ VISUAL.MAP // PORTRAIT</text>',
        f'  <text x="375" y="101" class="mono" font-size="11" fill="{pink_accent}">[DITHERED]</text>',

        f'  <!-- Frame for Portrait -->',
        f'  <rect x="49" y="128" width="390" height="392" rx="6" fill="{panel_bg}" stroke="{line_color}" stroke-width="1"/>',
        
        f'  <!-- Vector Dithered Portrait Points (Floyd-Steinberg Pure Vectors) -->',
        f'  <path d="{dither_svg_path}" fill="none" stroke="{portrait_color}" stroke-width="1" opacity="0.92"/>',

        f'  <!-- Cyber HUD Brackets on corners -->',
        f'  <path d="M55 146 V134 H67" stroke="{cyan_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M433 146 V134 H421" stroke="{cyan_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M55 502 V514 H67" stroke="{pink_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M433 502 V514 H421" stroke="{pink_accent}" stroke-width="2" fill="none"/>',

        f'  <!-- Bottom Telemetry in Visual Frame -->',
        f'  <text x="49" y="542" class="mono" font-size="11" fill="{muted_text}">SUBJECT:</text>',
        f'  <text x="110" y="542" class="mono" font-size="11" fill="{text_white}" font-weight="700">DORIAM FLORES</text>',
        f'  <text x="245" y="542" class="mono" font-size="11" fill="{muted_text}">ROLE:</text>',
        f'  <text x="285" y="542" class="mono" font-size="11" fill="{cyan_accent}">SR. BACKEND</text>',
        f'  <text x="49" y="562" class="mono" font-size="10" fill="{green_accent}">AI AGENTS &amp; DISTRIBUTED ARCHITECTURE</text>',

        f'  <!-- ==================== RIGHT PANEL: NEOVIM YAML ==================== -->',
        f'  <rect x="474" y="76" width="672" height="500" rx="8" fill="{panel_inner}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <path d="M474 116 H1146" stroke="{line_color}" stroke-width="1.5"/>',

        f'  <!-- File Tab -->',
        f'  <text x="492" y="101" class="mono" font-size="13" font-weight="700" fill="{pink_accent}">profile.yml</text>',
        f'  <text x="590" y="101" class="mono" font-size="11" fill="{muted_text}">[YAML · UTF-8]</text>',

        f'  <!-- Badge @Doriamflores -->',
        f'  <rect x="996" y="86" width="136" height="22" rx="11" fill="{cyan_accent}" fill-opacity="0.12" stroke="{cyan_accent}" stroke-width="1"/>',
        f'  <text x="1064" y="101" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="{cyan_accent}">@Doriamflores</text>',
    ]

    start_y = 142
    line_height = 20.5

    for idx, item in enumerate(yaml_lines):
        y = start_y + idx * line_height
        ln = item[0]
        svg_parts.append(f'  <text x="510" y="{y}" text-anchor="end" class="mono" font-size="12" fill="{line_num}">{ln}</text>')

        if item[2]:
            sec_name = html.escape(item[1])
            col = item[3]
            svg_parts.append(f'  <text x="528" y="{y}" class="mono" font-size="12" font-weight="700" fill="{col}">{sec_name}</text>')
        else:
            k = html.escape(item[1])
            k_col = item[3]
            v = html.escape(item[4])
            v_col = item[5]
            svg_parts.append(f'  <text x="528" y="{y}" class="mono" font-size="12"><tspan fill="{k_col}">{k}</tspan><tspan fill="{v_col}">{v}</tspan></text>')

    svg_parts.extend([
        f'  <!-- Vim Status Line -->',
        f'  <path d="M474 538 H1146" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <rect x="475" y="539" width="670" height="36" fill="{panel_bg}" rx="0 0 7 7"/>',
        f'  <rect x="486" y="546" width="76" height="22" rx="4" fill="{pink_accent}"/>',
        f'  <text x="524" y="561" text-anchor="middle" class="mono" font-size="11" font-weight="800" fill="#ffffff">NORMAL</text>',
        f'  <text x="574" y="561" class="mono" font-size="12" font-weight="600" fill="{text_white}">profile.yml</text>',
        f'  <text x="730" y="561" class="mono" font-size="11" fill="{muted_text}">[unix · utf-8]</text>',
        f'  <text x="1130" y="561" text-anchor="end" class="mono" font-size="11" fill="{cyan_accent}">19L, 642B  100%  19:1</text>',
        '</svg>'
    ])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    print(f"Generated: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == '__main__':
    base_dir = r"C:\Users\Door\Documents\github-doriam-profile"
    photo = os.path.join(base_dir, "assets", "profile.jpg")
    assets_dir = os.path.join(base_dir, "assets")

    for suffix in ["", ".v2"]:
        generate_banner(
            os.path.join(assets_dir, f"banner-dark{suffix}.svg"),
            photo,
            filter_id=f"glow_banner_dark{suffix.replace('.', '_')}",
            is_dark=True
        )
        generate_banner(
            os.path.join(assets_dir, f"banner-light{suffix}.svg"),
            photo,
            filter_id=f"glow_banner_light{suffix.replace('.', '_')}",
            is_dark=False
        )
