import os
import re
import html

def extract_svg_content(svg_path):
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def generate_animated_banner(output_path, filter_id, is_dark=True):
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
        peru_red = "#ff1744"
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
        peru_red = "#d91023"

    yaml_lines = [
        (" 1", "profile:", True, purple_accent),
        (" 2", "  subject: ", False, pink_accent, "Doriam Flores", text_white),
        (" 3", "  role: ", False, pink_accent, "Senior Backend Developer & AI Integrator", text_white),
        (" 4", "  origin: ", False, pink_accent, "Lima, Perú 🇵🇪  # Perú es clave", text_white),
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

    assets_dir = r"C:\Users\Door\Documents\github-doriam-profile\assets"
    nestjs_inner = extract_svg_content(os.path.join(assets_dir, "icon-skill-nestjs.svg"))
    linux_inner = extract_svg_content(os.path.join(assets_dir, "icon-skill-linux.svg"))
    docker_inner = extract_svg_content(os.path.join(assets_dir, "icon-skill-docker.svg"))
    ts_inner = extract_svg_content(os.path.join(assets_dir, "icon-skill-typescript.svg"))

    icon_x, icon_y, icon_size = 159, 195, 170

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">Doriam Flores - Live System Profile</title>',
        f'  <desc id="desc">Animated terminal profile cycling NestJS, Linux, Docker, TypeScript and Peru Flag every 3 seconds.</desc>',
        '  <defs>',
        f'    <filter id="{filter_id}" x="-20%" y="-20%" width="140%" height="140%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
        '    <!-- Peru Flag Clip -->',
        '    <clipPath id="peruClip">',
        '      <rect x="0" y="0" width="180" height="120" rx="12"/>',
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
        f'  <circle cx="38" cy="34" r="6" fill="#ff0055"/>',
        f'  <circle cx="58" cy="34" r="6" fill="#ffe600" opacity="0.9"/>',
        f'  <circle cx="78" cy="34" r="6" fill="#00ff9f"/>',

        f'  <text x="110" y="39" class="mono" font-size="13" fill="{muted_text}">nvim ~/profile.yml</text>',
        f'  <text x="265" y="39" class="mono" font-size="13" fill="{line_color}">::</text>',
        f'  <text x="285" y="39" class="mono" font-size="13" fill="{cyan_accent}" font-weight="700">DO\'0R.DEV // CYBER_CORE [ONLINE ⚡]</text>',
        f'  <text x="{W-150}" y="39" class="mono" font-size="12" fill="{green_accent}" font-weight="600">UPTIME: 99.99%</text>',

        f'  <!-- ==================== LEFT PANEL: ROTATING TECH LOGOS + PERU (3s CYCLE) ==================== -->',
        f'  <rect x="35" y="76" width="418" height="500" rx="8" fill="{panel_inner}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <path d="M35 116 H453" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <text x="49" y="101" class="mono" font-size="13" font-weight="700" fill="{cyan_accent}" letter-spacing="1">⚡ RUNTIME.ENGINE // MODULES</text>',
        f'  <text x="365" y="101" class="mono" font-size="11" fill="{pink_accent}">[3s_LOOP]</text>',

        f'  <!-- Visual Canvas for Logos -->',
        f'  <rect x="49" y="128" width="390" height="392" rx="8" fill="{panel_bg}" stroke="{line_color}" stroke-width="1"/>',

        f'  <!-- Futuristic Cyber Orbit Rings in Canvas -->',
        f'  <circle cx="244" cy="280" r="140" fill="none" stroke="{line_color}" stroke-width="1" stroke-dasharray="6,8" opacity="0.45"/>',
        f'  <circle cx="244" cy="280" r="110" fill="none" stroke="{cyan_accent}" stroke-width="1" stroke-dasharray="4,6" opacity="0.3">',
        f'    <animateTransform attributeName="transform" type="rotate" from="0 244 280" to="360 244 280" dur="24s" repeatCount="indefinite"/>',
        f'  </circle>',
        f'  <circle cx="244" cy="280" r="80" fill="none" stroke="{pink_accent}" stroke-width="1" stroke-dasharray="3,5" opacity="0.35">',
        f'    <animateTransform attributeName="transform" type="rotate" from="360 244 280" to="0 244 280" dur="18s" repeatCount="indefinite"/>',
        f'  </circle>',
    ]

    # Animation Cycle: 15 seconds total (5 items * 3s each)
    # 01. NESTJS (0s - 3s: 0% to 20%)
    # 02. LINUX (3s - 6s: 20% to 40%)
    # 03. DOCKER (6s - 9s: 40% to 60%)
    # 04. TYPESCRIPT (9s - 12s: 60% to 80%)
    # 05. PERÚ ES CLAVE (12s - 15s: 80% to 100%)
    svg_parts.extend([
        f'  <!-- 01. NESTJS (0s - 3s) -->',
        f'  <g id="logo-nestjs">',
        f'    <animate attributeName="opacity" dur="15s" repeatCount="indefinite" keyTimes="0;0.02;0.18;0.20;0.98;1" values="1;1;1;0;0;1"/>',
        f'    <svg x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" viewBox="0 0 256 256">',
        f'      {nestjs_inner}',
        f'    </svg>',
        f'    <text x="244" y="435" text-anchor="middle" class="mono" font-size="15" font-weight="700" fill="#ea284e">NESTJS FRAMEWORK</text>',
        f'    <text x="244" y="460" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Enterprise Architecture &amp; Microservices</text>',
        f'    <rect x="174" y="480" width="140" height="22" rx="4" fill="#ea284e" fill-opacity="0.15" stroke="#ea284e" stroke-width="1"/>',
        f'    <text x="244" y="495" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#ea284e">MODULE // 01 of 05</text>',
        f'  </g>',

        f'  <!-- 02. LINUX (3s - 6s) -->',
        f'  <g id="logo-linux" opacity="0">',
        f'    <animate attributeName="opacity" dur="15s" repeatCount="indefinite" keyTimes="0;0.18;0.20;0.38;0.40;1" values="0;0;1;1;0;0"/>',
        f'    <svg x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" viewBox="0 0 256 256">',
        f'      {linux_inner}',
        f'    </svg>',
        f'    <text x="244" y="435" text-anchor="middle" class="mono" font-size="15" font-weight="700" fill="{yellow_accent if is_dark else "#d97706"}">LINUX ENVIRONMENT</text>',
        f'    <text x="244" y="460" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Server CLI · Bash · POSIX Kernel Core</text>',
        f'    <rect x="174" y="480" width="140" height="22" rx="4" fill="{yellow_accent if is_dark else "#d97706"}" fill-opacity="0.15" stroke="{yellow_accent if is_dark else "#d97706"}" stroke-width="1"/>',
        f'    <text x="244" y="495" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{yellow_accent if is_dark else "#d97706"}">MODULE // 02 of 05</text>',
        f'  </g>',

        f'  <!-- 03. DOCKER (6s - 9s) -->',
        f'  <g id="logo-docker" opacity="0">',
        f'    <animate attributeName="opacity" dur="15s" repeatCount="indefinite" keyTimes="0;0.38;0.40;0.58;0.60;1" values="0;0;1;1;0;0"/>',
        f'    <svg x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" viewBox="0 0 256 256">',
        f'      {docker_inner}',
        f'    </svg>',
        f'    <text x="244" y="435" text-anchor="middle" class="mono" font-size="15" font-weight="700" fill="#2496ed">DOCKER ENGINE</text>',
        f'    <text x="244" y="460" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Containers · High Concurrency Deploy</text>',
        f'    <rect x="174" y="480" width="140" height="22" rx="4" fill="#2496ed" fill-opacity="0.15" stroke="#2496ed" stroke-width="1"/>',
        f'    <text x="244" y="495" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#2496ed">MODULE // 03 of 05</text>',
        f'  </g>',

        f'  <!-- 04. TYPESCRIPT (9s - 12s) -->',
        f'  <g id="logo-typescript" opacity="0">',
        f'    <animate attributeName="opacity" dur="15s" repeatCount="indefinite" keyTimes="0;0.58;0.60;0.78;0.80;1" values="0;0;1;1;0;0"/>',
        f'    <svg x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" viewBox="0 0 256 256">',
        f'      {ts_inner}',
        f'    </svg>',
        f'    <text x="244" y="435" text-anchor="middle" class="mono" font-size="15" font-weight="700" fill="#3178c6">TYPESCRIPT RUNTIME</text>',
        f'    <text x="244" y="460" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Strict Type Safety &amp; Clean Code</text>',
        f'    <rect x="174" y="480" width="140" height="22" rx="4" fill="#3178c6" fill-opacity="0.15" stroke="#3178c6" stroke-width="1"/>',
        f'    <text x="244" y="495" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#3178c6">MODULE // 04 of 05</text>',
        f'  </g>',

        f'  <!-- 05. 🇵🇪 BANDERA DE PERÚ // PERÚ ES CLAVE (12s - 15s) -->',
        f'  <g id="logo-peru" opacity="0">',
        f'    <animate attributeName="opacity" dur="15s" repeatCount="indefinite" keyTimes="0;0.78;0.80;0.98;1" values="0;0;1;1;0"/>',
        f'    <!-- Glowing Frame for Flag -->',
        f'    <g transform="translate(154, 220)">',
        f'      <rect x="-4" y="-4" width="188" height="128" rx="15" fill="none" stroke="{peru_red}" stroke-width="2.5" opacity="0.8"/>',
        f'      <g clip-path="url(#peruClip)">',
        f'        <!-- Red Stripe 1 -->',
        f'        <rect x="0" y="0" width="60" height="120" fill="#D91023"/>',
        f'        <!-- White Stripe -->',
        f'        <rect x="60" y="0" width="60" height="120" fill="#FFFFFF"/>',
        f'        <!-- Red Stripe 2 -->',
        f'        <rect x="120" y="0" width="60" height="120" fill="#D91023"/>',
        f'      </g>',
        f'    </g>',
        f'    <!-- Telemetry Label -->',
        f'    <text x="244" y="435" text-anchor="middle" class="mono" font-size="16" font-weight="900" fill="{peru_red}" letter-spacing="1.5">🇵🇪 PERÚ ES CLAVE 🇵🇪</text>',
        f'    <text x="244" y="460" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Powered by Ceviche &amp; High Concurrency 🐟⚡</text>',
        f'    <rect x="164" y="480" width="160" height="22" rx="4" fill="{peru_red}" fill-opacity="0.18" stroke="{peru_red}" stroke-width="1"/>',
        f'    <text x="244" y="495" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{peru_red}">LOCAL_NODE // 05 of 05 ⚡</text>',
        f'  </g>',

        f'  <!-- Cyber HUD Brackets on corners -->',
        f'  <path d="M55 146 V134 H67" stroke="{cyan_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M433 146 V134 H421" stroke="{cyan_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M55 502 V514 H67" stroke="{pink_accent}" stroke-width="2" fill="none"/>',
        f'  <path d="M433 502 V514 H421" stroke="{pink_accent}" stroke-width="2" fill="none"/>',

        f'  <!-- Bottom Telemetry in Visual Frame -->',
        f'  <text x="49" y="542" class="mono" font-size="11" fill="{muted_text}">DEV_CORE:</text>',
        f'  <text x="120" y="542" class="mono" font-size="11" fill="{text_white}" font-weight="700">DORIAM FLORES</text>',
        f'  <text x="245" y="542" class="mono" font-size="11" fill="{muted_text}">ROLE:</text>',
        f'  <text x="285" y="542" class="mono" font-size="11" fill="{cyan_accent}">SR. BACKEND</text>',
        f'  <text x="49" y="562" class="mono" font-size="10" fill="{green_accent}">HIGH AVAILABILITY &amp; SUB-SECOND LATENCY</text>',

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
    print(f"Generated Peru-enabled banner: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == '__main__':
    base_dir = r"C:\Users\Door\Documents\github-doriam-profile"
    assets_dir = os.path.join(base_dir, "assets")

    for suffix in ["", ".v2", ".v3", ".v4"]:
        generate_animated_banner(
            os.path.join(assets_dir, f"banner-dark{suffix}.svg"),
            filter_id=f"glow_banner_dark{suffix.replace('.', '_')}",
            is_dark=True
        )
        generate_animated_banner(
            os.path.join(assets_dir, f"banner-light{suffix}.svg"),
            filter_id=f"glow_banner_light{suffix.replace('.', '_')}",
            is_dark=False
        )
