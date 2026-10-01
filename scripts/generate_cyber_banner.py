import base64
import os

def generate_banner(output_path, photo_path, is_dark=True):
    W, H = 1180, 610

    # Colors
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
        shadow_color = "#000000"
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
        shadow_color = "#94a3b8"

    # Read photo and convert to base64
    with open(photo_path, "rb") as f:
        photo_b64 = base64.b64encode(f.read()).decode("utf-8")
    photo_data_uri = f"data:image/jpeg;base64,{photo_b64}"

    # YAML profile content lines
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
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">Doriam Flores - Senior Backend Architect &amp; AI Integrator</title>',
        f'  <desc id="desc">Cyberpunk terminal profile with visual portrait and Neovim YAML configuration.</desc>',
        '  <defs>',
        f'    <linearGradient id="cyberBorder" x1="0%" y1="0%" x2="100%" y2="100%">',
        f'      <stop offset="0%" stop-color="{cyan_accent}"/>',
        f'      <stop offset="50%" stop-color="{purple_accent}"/>',
        f'      <stop offset="100%" stop-color="{pink_accent}"/>',
        f'    </linearGradient>',
        '    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">',
        '      <feGaussianBlur stdDeviation="2.5" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
        '    <!-- Photo Rounded Clip -->',
        '    <clipPath id="photoClip">',
        '      <rect x="49" y="130" width="390" height="388" rx="8"/>',
        '    </clipPath>',
        '  </defs>',

        '  <style>',
        '    .mono { font-family: "JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }',
        '  </style>',

        f'  <!-- Main Background -->',
        f'  <rect width="{W}" height="{H}" rx="16" fill="{bg}"/>',
        f'  <rect x="10" y="10" width="{W-20}" height="{H-20}" rx="14" fill="{panel_bg}" stroke="{line_color}" stroke-width="1.5"/>',

        f'  <!-- Top Window Header Bar -->',
        f'  <path d="M10 58 H{W-10}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <circle cx="38" cy="34" r="6" fill="#ff0055" filter="url(#subtleGlow)"/>',
        f'  <circle cx="58" cy="34" r="6" fill="#ffe600" opacity="0.9"/>',
        f'  <circle cx="78" cy="34" r="6" fill="#00ff9f" filter="url(#subtleGlow)"/>',

        f'  <text x="110" y="39" class="mono" font-size="13" fill="{muted_text}">nvim ~/profile.yml</text>',
        f'  <text x="265" y="39" class="mono" font-size="13" fill="{line_color}">::</text>',
        f'  <text x="285" y="39" class="mono" font-size="13" fill="{cyan_accent}" font-weight="700">DO\'0R.DEV // CYBER_CORE [ONLINE ⚡]</text>',
        f'  <text x="{W-150}" y="39" class="mono" font-size="12" fill="{green_accent}" font-weight="600">UPTIME: 99.99%</text>',

        f'  <!-- ==================== LEFT PANEL: VISUAL ID (PORTRAIT) ==================== -->',
        f'  <rect x="35" y="76" width="418" height="500" rx="8" fill="{panel_inner}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <path d="M35 116 H453" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <text x="49" y="101" class="mono" font-size="13" font-weight="700" fill="{cyan_accent}" letter-spacing="1">⚡ VISUAL.ID // PORTRAIT</text>',
        f'  <text x="375" y="101" class="mono" font-size="11" fill="{pink_accent}">[200 OK]</text>',

        f'  <!-- Frame for Portrait -->',
        f'  <rect x="47" y="128" width="394" height="392" rx="10" fill="none" stroke="url(#cyberBorder)" stroke-width="2" filter="url(#subtleGlow)"/>',
        
        f'  <!-- User Portrait Image (Base64) -->',
        f'  <image href="{photo_data_uri}" x="49" y="130" width="390" height="388" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip)"/>',

        f'  <!-- Cyberpunk Scanline Overlays on photo -->',
        f'  <g opacity="0.12">',
    ]

    for y_line in range(130, 518, 6):
        svg_parts.append(f'    <line x1="49" y1="{y_line}" x2="439" y2="{y_line}" stroke="{cyan_accent}" stroke-width="1"/>')

    svg_parts.extend([
        f'  </g>',

        f'  <!-- Cyber HUD Brackets on corners -->',
        f'  <path d="M55 150 V136 H69" stroke="{cyan_accent}" stroke-width="3" fill="none" filter="url(#subtleGlow)"/>',
        f'  <path d="M433 150 V136 H419" stroke="{cyan_accent}" stroke-width="3" fill="none" filter="url(#subtleGlow)"/>',
        f'  <path d="M55 498 V512 H69" stroke="{pink_accent}" stroke-width="3" fill="none" filter="url(#subtleGlow)"/>',
        f'  <path d="M433 498 V512 H419" stroke="{pink_accent}" stroke-width="3" fill="none" filter="url(#subtleGlow)"/>',

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
    ])

    # Render YAML Lines
    start_y = 142
    line_height = 20.5

    for idx, item in enumerate(yaml_lines):
        y = start_y + idx * line_height
        ln = item[0]
        # Line number
        svg_parts.append(f'  <text x="510" y="{y}" text-anchor="end" class="mono" font-size="12" fill="{line_num}">{ln}</text>')

        if item[2]:  # Section header (profile:, stack:, etc.)
            sec_name = item[1]
            col = item[3]
            svg_parts.append(f'  <text x="528" y="{y}" class="mono" font-size="12" font-weight="700" fill="{col}">{sec_name}</text>')
        else:
            k = item[1]
            k_col = item[3]
            v = item[4]
            v_col = item[5]
            svg_parts.append(f'  <text x="528" y="{y}" class="mono" font-size="12"><tspan fill="{k_col}">{k}</tspan><tspan fill="{v_col}">{v}</tspan></text>')

    # Vim Status Line
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

    generate_banner(os.path.join(assets_dir, "banner-dark.svg"), photo, is_dark=True)
    generate_banner(os.path.join(assets_dir, "banner-light.svg"), photo, is_dark=False)
