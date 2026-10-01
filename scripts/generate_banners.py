import os

def create_banner(filename, is_dark=True):
    width, height = 960, 220
    bg_color = "#08090e" if is_dark else "#f8fafc"
    border_color = "#00f3ff" if is_dark else "#0284c7"
    text_main = "#ffffff" if is_dark else "#0f172a"
    sub_color = "#00f3ff" if is_dark else "#0284c7"
    accent_pink = "#ff007f" if is_dark else "#db2777"
    grid_stroke = "#141829" if is_dark else "#e2e8f0"
    tag_bg = "#111422" if is_dark else "#e2e8f0"
    tag_text = "#00ff9f" if is_dark else "#059669"
    dim_text = "#64748b" if is_dark else "#94a3b8"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img">
  <defs>
    <linearGradient id="cyberGradBanner_{"dark" if is_dark else "light"}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{sub_color}"/>
      <stop offset="50%" stop-color="#b026ff"/>
      <stop offset="100%" stop-color="{accent_pink}"/>
    </linearGradient>
    <linearGradient id="glowLine_{"dark" if is_dark else "light"}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{sub_color}" stop-opacity="0"/>
      <stop offset="30%" stop-color="{sub_color}" stop-opacity="1"/>
      <stop offset="70%" stop-color="{accent_pink}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{accent_pink}" stop-opacity="0"/>
    </linearGradient>
    <filter id="bannerGlow_{"dark" if is_dark else "light"}" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" rx="14" fill="{bg_color}"/>

  <!-- Cyber Grid Pattern -->
  <g stroke="{grid_stroke}" stroke-width="1" opacity="0.65">
    <line x1="0" y1="40" x2="{width}" y2="40"/>
    <line x1="0" y1="80" x2="{width}" y2="80"/>
    <line x1="0" y1="120" x2="{width}" y2="120"/>
    <line x1="0" y1="160" x2="{width}" y2="160"/>
    <line x1="0" y1="200" x2="{width}" y2="200"/>

    <line x1="80" y1="0" x2="80" y2="{height}"/>
    <line x1="160" y1="0" x2="160" y2="{height}"/>
    <line x1="240" y1="0" x2="240" y2="{height}"/>
    <line x1="320" y1="0" x2="320" y2="{height}"/>
    <line x1="400" y1="0" x2="400" y2="{height}"/>
    <line x1="480" y1="0" x2="480" y2="{height}"/>
    <line x1="560" y1="0" x2="560" y2="{height}"/>
    <line x1="640" y1="0" x2="640" y2="{height}"/>
    <line x1="720" y1="0" x2="720" y2="{height}"/>
    <line x1="800" y1="0" x2="800" y2="{height}"/>
    <line x1="880" y1="0" x2="880" y2="{height}"/>
  </g>

  <!-- Border Frame -->
  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="13" fill="none" stroke="url(#cyberGradBanner_{"dark" if is_dark else "light"})" stroke-width="1.8"/>

  <!-- Top Cyber Status Bar -->
  <text x="35" y="28" font-family="'JetBrains Mono', monospace" font-size="11" fill="{dim_text}">NODE_ID: LIMA_PE</text>
  <text x="160" y="28" font-family="'JetBrains Mono', monospace" font-size="11" fill="{sub_color}">// ARCHITECTURE: EVENT_DRIVEN</text>
  <text x="{width-180}" y="28" font-family="'JetBrains Mono', monospace" font-size="11" fill="{tag_text}" font-weight="700">SYS_STATUS: ONLINE ⚡</text>

  <!-- Glowing Horizontal Divider -->
  <line x1="20" y1="38" x2="{width-20}" y2="38" stroke="url(#glowLine_{"dark" if is_dark else "light"})" stroke-width="1.5"/>

  <!-- Main Hero Title -->
  <g transform="translate(40, 98)">
    <!-- Brand Logo Icon -->
    <rect x="0" y="-36" width="46" height="46" rx="8" fill="{tag_bg}" stroke="{sub_color}" stroke-width="1.5"/>
    <text x="23" y="-8" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="900" fill="{sub_color}">D</text>
    
    <!-- Title Text -->
    <text x="64" y="-8" font-family="'JetBrains Mono', 'Segoe UI', sans-serif" font-size="34" font-weight="800" fill="{text_main}" letter-spacing="1.5">
      DORIAM FLORES <tspan fill="{accent_pink}">.DEV</tspan>
    </text>

    <!-- Subtitle Role -->
    <text x="66" y="22" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" fill="{sub_color}" letter-spacing="1">
      ⚡ SENIOR BACKEND ARCHITECT &amp; AI INTEGRATOR
    </text>
  </g>

  <!-- Floating Cyber Badges / Stack Tags -->
  <g transform="translate(40, 160)">
    <!-- Tag 1 -->
    <rect x="0" y="0" width="135" height="28" rx="6" fill="{tag_bg}" stroke="{sub_color}" stroke-width="1"/>
    <text x="67" y="18" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="{sub_color}" font-weight="600">⚡ MICROSERVICES</text>

    <!-- Tag 2 -->
    <rect x="145" y="0" width="130" height="28" rx="6" fill="{tag_bg}" stroke="{accent_pink}" stroke-width="1"/>
    <text x="210" y="18" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="{accent_pink}" font-weight="600">🤖 AI &amp; LLM AGENTS</text>

    <!-- Tag 3 -->
    <rect x="285" y="0" width="115" height="28" rx="6" fill="{tag_bg}" stroke="#ffe600" stroke-width="1"/>
    <text x="342" y="18" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#ffe600" font-weight="600">☁ AWS CLOUD</text>

    <!-- Tag 4 -->
    <rect x="410" y="0" width="145" height="28" rx="6" fill="{tag_bg}" stroke="{tag_text}" stroke-width="1"/>
    <text x="482" y="18" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="{tag_text}" font-weight="600">🚀 HIGH CONCURRENCY</text>

    <!-- Tag 5 -->
    <rect x="565" y="0" width="140" height="28" rx="6" fill="{tag_bg}" stroke="#b026ff" stroke-width="1"/>
    <text x="635" y="18" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#b026ff" font-weight="600">📦 EVENT-DRIVEN</text>
  </g>

  <!-- Right Decorative Hexagon & Telemetry -->
  <g transform="translate(810, 60)" opacity="0.9">
    <polygon points="50,0 100,28 100,85 50,114 0,85 0,28" fill="none" stroke="{sub_color}" stroke-width="1.5"/>
    <polygon points="50,15 85,35 85,78 50,98 15,78 15,35" fill="{tag_bg}" stroke="{accent_pink}" stroke-width="1"/>
    <text x="50" y="62" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" fill="{tag_text}">200 OK</text>
  </g>
</svg>'''

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated banner: {filename}")

if __name__ == '__main__':
    out_dir = r"C:\Users\Door\Documents\github-doriam-profile\assets"
    create_banner(os.path.join(out_dir, "banner-dark.svg"), is_dark=True)
    create_banner(os.path.join(out_dir, "banner-light.svg"), is_dark=False)
