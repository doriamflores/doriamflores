import math
import os

def generate_radar(
    labels, values, filename, title, filter_id, accent_color="#00f3ff", fill_color="rgba(0, 243, 255, 0.25)", is_dark=True
):
    bg_color = "#0a0c14" if is_dark else "#f8fafc"
    card_border = "#1f2338" if is_dark else "#e2e8f0"
    grid_color = "#1a1e30" if is_dark else "#cbd5e1"
    text_color = "#94a3b8" if is_dark else "#475569"
    title_color = "#00f3ff" if is_dark else "#0284c7"
    if accent_color == "#ff007f":
        title_color = "#ff007f" if is_dark else "#db2777"

    width, height = 440, 390
    cx, cy = 220, 215
    radius = 120
    n = len(labels)
    angle_step = 2 * math.pi / n

    # Concentric levels
    levels = [0.25, 0.50, 0.75, 1.0]

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        f'    <filter id="{filter_id}" x="-20%" y="-20%" width="140%" height="140%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '  </defs>',
        f'  <rect width="{width}" height="{height}" rx="12" fill="{bg_color}" stroke="{card_border}" stroke-width="1.5"/>',
        f'  <text x="{width//2}" y="36" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="14" font-weight="700" fill="{title_color}" letter-spacing="1">⚡ {title} ⚡</text>',
        f'  <line x1="30" y1="52" x2="{width-30}" y2="52" stroke="{grid_color}" stroke-width="1"/>'
    ]

    # Draw polygon web levels (Hexagons)
    for lvl in levels:
        r = radius * lvl
        pts = []
        for i in range(n):
            a = -math.pi / 2 + i * angle_step
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            pts.append(f"{x:.1f},{y:.1f}")
        pts_str = " ".join(pts)
        svg_parts.append(f'  <polygon points="{pts_str}" fill="none" stroke="{grid_color}" stroke-width="1" stroke-dasharray="3,3" opacity="0.8"/>')

    # Draw spokes and labels
    for i in range(n):
        a = -math.pi / 2 + i * angle_step
        x = cx + radius * math.cos(a)
        y = cy + radius * math.sin(a)
        svg_parts.append(f'  <line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{grid_color}" stroke-width="1"/>')

        # Label position
        lx = cx + (radius + 28) * math.cos(a)
        ly = cy + (radius + 18) * math.sin(a)
        anchor = "middle"
        if math.cos(a) > 0.3:
            anchor = "start"
        elif math.cos(a) < -0.3:
            anchor = "end"

        val_pct = int(values[i] * 100)
        svg_parts.append(
            f'  <text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-family="JetBrains Mono, monospace" font-size="11" fill="{text_color}" font-weight="500">{labels[i]} <tspan fill="{accent_color}" font-weight="700">[{val_pct}%]</tspan></text>'
        )

    # Calculate data points
    data_pts = []
    for i in range(n):
        a = -math.pi / 2 + i * angle_step
        r = radius * values[i]
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        data_pts.append((x, y))

    poly_pts_str = " ".join([f"{x:.1f},{y:.1f}" for x, y in data_pts])

    # Draw data polygon
    svg_parts.append(f'  <polygon points="{poly_pts_str}" fill="{fill_color}" stroke="{accent_color}" stroke-width="2.5" filter="url(#{filter_id})"/>')

    # Draw vertex dots
    for x, y in data_pts:
        svg_parts.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{accent_color}" stroke="{bg_color}" stroke-width="1.5"/>')

    # Footer note
    svg_parts.append(f'  <text x="{width//2}" y="{height - 15}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="{text_color}" opacity="0.6">status: verified_production · tps: ultra_high</text>')
    svg_parts.append('</svg>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg_parts))
    print(f"Generated: {filename}")

if __name__ == '__main__':
    out_dir = r"C:\Users\Door\Documents\github-doriam-profile\assets"

    # Radar 1: Backend Architecture & Systems
    backend_labels = ["Microservicios", "Event-Driven", "Cloud AWS", "DB & Cache", "IA Agents", "High TPS APIs"]
    backend_vals = [0.96, 0.90, 0.88, 0.94, 0.88, 0.95]

    generate_radar(
        backend_labels, backend_vals,
        os.path.join(out_dir, "radar-backend-dark.svg"),
        "BACKEND ARCHITECTURE SIGNALS",
        filter_id="glow_backend_dark",
        accent_color="#00f3ff",
        fill_color="rgba(0, 243, 255, 0.22)",
        is_dark=True
    )
    generate_radar(
        backend_labels, backend_vals,
        os.path.join(out_dir, "radar-backend-light.svg"),
        "BACKEND ARCHITECTURE SIGNALS",
        filter_id="glow_backend_light",
        accent_color="#0284c7",
        fill_color="rgba(2, 132, 199, 0.20)",
        is_dark=False
    )

    # Radar 2: Core Tech Stack
    stack_labels = ["TypeScript", "NestJS", "Node.js", "Python", "SQL / NoSQL", "Docker / Linux"]
    stack_vals = [0.95, 0.96, 0.95, 0.85, 0.92, 0.90]

    generate_radar(
        stack_labels, stack_vals,
        os.path.join(out_dir, "radar-stack-dark.svg"),
        "CORE RUNTIME & LANGUAGE STACK",
        filter_id="glow_stack_dark",
        accent_color="#ff007f",
        fill_color="rgba(255, 0, 127, 0.22)",
        is_dark=True
    )
    generate_radar(
        stack_labels, stack_vals,
        os.path.join(out_dir, "radar-stack-light.svg"),
        "CORE RUNTIME & LANGUAGE STACK",
        filter_id="glow_stack_light",
        accent_color="#db2777",
        fill_color="rgba(219, 39, 119, 0.20)",
        is_dark=False
    )
