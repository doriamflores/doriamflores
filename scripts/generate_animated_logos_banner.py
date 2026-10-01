import os
import html

# Official Vector Paths (viewBox 0 0 24 24)
NESTJS_PATH = (
    "M14.131.047c-.173 0-.334.037-.483.087.316.21.49.49.576.806.007.043.019.074.025.117a.681.681 0 0 1 .013.112"
    "c.024.545-.143.614-.26.936-.18.415-.13.861.086 1.22a.74.74 0 0 0 .074.137c-.235-1.568 1.073-1.803 1.314-2.293"
    ".019-.428-.334-.713-.613-.911a1.37 1.37 0 0 0-.732-.21zM16.102.4c-.024.143-.006.106-.012.18-.006.05-.006.112-.012.161"
    "-.013.05-.025.1-.044.149-.012.05-.03.1-.05.149l-.067.142c-.02.025-.031.05-.05.075l-.037.055a2.152 2.152 0 0 1-.093.124"
    "c-.037.038-.068.081-.112.112v.006c-.037.031-.074.068-.118.1-.13.099-.278.173-.415.266-.043.03-.087.056-.124.093"
    "a.906.906 0 0 0-.118.099c-.043.037-.074.074-.111.118-.031.037-.068.08-.093.124a1.582 1.582 0 0 0-.087.13"
    "c-.025.05-.043.093-.068.142-.019.05-.037.093-.05.143a2.007 2.007 0 0 0-.043.155c-.006.025-.006.056-.012.08"
    "-.007.025-.007.05-.013.075 0 .05-.006.105-.006.155 0 .037 0 .074.006.111 0 .05.006.1.019.155.006.05.018.1.03.15"
    ".02.049.032.098.05.148.013.03.031.062.044.087l-1.426-.552c-.241-.068-.477-.13-.719-.186l-.39-.093"
    "c-.372-.074-.75-.13-1.128-.167-.013 0-.019-.006-.031-.006A11.082 11.082 0 0 0 8.9 2.855c-.378.025-.756.074-1.134.136"
    "a12.45 12.45 0 0 0-.837.174l-.279.074c-.092.037-.18.08-.266.118l-.205.093c-.012.006-.024.006-.03.012"
    "-.063.031-.118.056-.174.087a2.738 2.738 0 0 0-.236.118c-.043.018-.086.043-.124.062a.559.559 0 0 1-.055.03"
    "c-.056.032-.112.063-.162.094a1.56 1.56 0 0 0-.148.093c-.044.03-.087.055-.124.086-.006.007-.013.007-.019.013"
    "-.037.025-.08.056-.118.087l-.012.012-.093.074c-.012.007-.025.019-.037.025-.031.025-.062.056-.093.08"
    "-.006.013-.019.02-.025.025-.037.038-.074.069-.111.106-.007 0-.007.006-.013.012a1.742 1.742 0 0 0-.111.106"
    "c-.007.006-.007.012-.013.012a1.454 1.454 0 0 0-.093.1c-.012.012-.03.024-.043.036a1.374 1.374 0 0 1-.106.112"
    "c-.006.012-.018.019-.024.03-.05.05-.093.1-.143.15l-.018.018c-.1.106-.205.211-.317.304-.111.1-.229.192-.347.273"
    "a3.777 3.777 0 0 1-.762.421c-.13.056-.267.106-.403.149-.26.056-.527.161-.756.18-.05 0-.105.012-.155.018l-.155.037"
    "-.149.056c-.05.019-.099.044-.148.068-.044.031-.093.056-.137.087a1.011 1.011 0 0 0-.124.106c-.043.03-.087.074-.124.111"
    "-.037.043-.074.08-.105.124-.031.05-.068.093-.093.143a1.092 1.092 0 0 0-.087.142c-.025.056-.05.106-.068.161"
    "-.019.05-.037.106-.056.161-.012.05-.025.1-.03.15 0 .005-.007.012-.007.018-.012.056-.012.13-.019.167"
    "C.006 7.95 0 7.986 0 8.03a.657.657 0 0 0 .074.31v.006c.019.037.044.075.069.112.024.037.05.074.08.111"
    ".031.031.068.069.106.1a.906.906 0 0 0 .117.099c.149.13.186.173.378.272.031.019.062.031.1.05.006 0 .012.006.018.006"
    "0 .013 0 .019.006.031a1.272 1.272 0 0 0 .08.298c.02.037.032.074.05.111.007.013.013.025.02.031.024.05.049.093.073.137"
    "l.093.13c.031.037.069.08.106.118.037.037.074.068.118.105 0 0 .006.006.012.006.037.031.074.062.112.087a.986.986 0 0 0 .136.08"
    "c.043.025.093.05.142.069a.73.73 0 0 0 .124.043c.007.006.013.006.025.012.025.007.056.013.08.019-.018.335-.024.65.026.762"
    ".055.124.328-.254.6-.688-.036.428-.061.93 0 1.079.069.155.44-.329.763-.862 4.395-1.016 8.405 2.02 8.826 6.31"
    "-.08-.67-.905-1.041-1.283-.948-.186.458-.502 1.047-1.01 1.413.043-.41.025-.83-.062-1.24a4.009 4.009 0 0 1-.769 1.562"
    "c-.588.043-1.177-.242-1.487-.67-.025-.018-.031-.055-.05-.08-.018-.043-.037-.087-.05-.13a.515.515 0 0 1-.037-.13"
    "c-.006-.044-.006-.087-.006-.137v-.093a.992.992 0 0 1 .031-.13c.013-.043.025-.086.044-.13.024-.043.043-.087.074-.13"
    ".105-.298.105-.54-.087-.682a.706.706 0 0 0-.118-.062c-.024-.006-.055-.018-.08-.025l-.05-.018a.847.847 0 0 0-.13-.031"
    ".472.472 0 0 0-.13-.019 1.01 1.01 0 0 0-.136-.012c-.031 0-.062.006-.093.006a.484.484 0 0 0-.137.019c-.043.006-.086.012-.13.024"
    "a1.068 1.068 0 0 0-.13.044c-.043.018-.08.037-.124.056-.037.018-.074.043-.118.062-1.444.942-.582 3.148.403 3.787"
    "-.372.068-.75.148-.855.229l-.013.012c.267.161.546.298.837.416.397.13.818.247 1.004.297v.006a5.996 5.996 0 0 0 1.562.112"
    "c2.746-.192 4.996-2.281 5.405-5.033l.037.161c.019.112.043.23.056.347v.006c.012.056.018.112.025.162v.024"
    "c.006.056.012.112.012.162.006.068.012.136.012.204v.1c0 .03.007.067.007.098 0 .038-.007.075-.007.112v.087"
    "c0 .043-.006.08-.006.124 0 .025 0 .05-.006.08 0 .044-.006.087-.006.137-.006.018-.006.037-.006.055l-.02.143"
    "c0 .019 0 .037-.005.056-.007.062-.019.118-.025.18v.012l-.037.174v.018l-.037.167c0 .007-.007.02-.007.025"
    "a1.663 1.663 0 0 1-.043.168v.018c-.019.062-.037.118-.05.174-.006.006-.006.012-.006.012l-.056.186"
    "c-.024.062-.043.118-.068.18-.025.062-.043.124-.068.18-.025.062-.05.117-.074.18h-.007c-.024.055-.05.117-.08.173"
    "a.302.302 0 0 1-.019.043c-.006.006-.006.013-.012.019a5.867 5.867 0 0 1-1.742 2.082c-.05.031-.099.069-.149.106"
    "-.012.012-.03.018-.043.03a2.603 2.603 0 0 1-.136.094l.018.037h.007l.26-.037h.006c.161-.025.322-.056.483-.087"
    ".044-.006.093-.019.137-.031l.087-.019c.043-.006.086-.018.13-.024.037-.013.074-.02.111-.031.62-.15 1.221-.354 1.798-.595"
    "a9.926 9.926 0 0 1-3.85 3.142c.714-.05 1.426-.167 2.114-.366a9.903 9.903 0 0 0 5.857-4.68 9.893 9.893 0 0 1-1.667 3.986"
    "9.758 9.758 0 0 0 1.655-1.376 9.824 9.824 0 0 0 2.61-5.268c.21.98.272 1.99.18 2.987 4.474-6.241.371-12.712-1.346-14.416"
    "-.006-.013-.012-.019-.012-.031-.006.006-.006.006-.006.012 0-.006 0-.006-.007-.012 0 .074-.006.148-.012.223"
    "a8.34 8.34 0 0 1-.062.415c-.03.136-.068.273-.105.41-.044.13-.093.266-.15.396a5.322 5.322 0 0 1-.185.378"
    "4.735 4.735 0 0 1-.477.688c-.093.111-.192.21-.292.31a3.994 3.994 0 0 1-.18.155l-.142.124a3.459 3.459 0 0 1-.347.241"
    "4.295 4.295 0 0 1-.366.211c-.13.062-.26.118-.39.174a4.364 4.364 0 0 1-.818.223c-.143.025-.285.037-.422.05"
    "a4.914 4.914 0 0 1-.297.012 4.66 4.66 0 0 1-.422-.025 3.137 3.137 0 0 1-.421-.062 3.136 3.136 0 0 1-.415-.105h-.007"
    "c.137-.013.273-.025.41-.05a4.493 4.493 0 0 0 .818-.223c.136-.05.266-.112.39-.174.13-.062.248-.13.372-.204"
    ".118-.08.235-.161.347-.248.112-.087.217-.18.316-.279.105-.093.198-.198.291-.304.093-.111.18-.223.26-.334"
    ".013-.019.026-.044.038-.062.062-.1.124-.199.18-.298a4.272 4.272 0 0 0 .334-.775c.044-.13.075-.266.106-.403"
    ".025-.142.05-.278.062-.415.012-.142.025-.285.025-.421 0-.1-.007-.199-.013-.298a6.726 6.726 0 0 0-.05-.415"
    "4.493 4.493 0 0 0-.092-.415c-.044-.13-.087-.267-.137-.397-.05-.13-.111-.26-.173-.384-.069-.124-.137-.248-.211-.366"
    "a6.843 6.843 0 0 0-.248-.34c-.093-.106-.186-.212-.285-.317a3.878 3.878 0 0 0-.161-.155c-.28-.217-.57-.421-.862-.607"
    "a1.154 1.154 0 0 0-.124-.062 2.415 2.415 0 0 0-.589-.26Z"
)

LINUX_PATH = (
    "M12.504 0c-.155 0-.315.008-.48.021-4.226.333-3.105 4.807-3.17 6.298-.076 1.092-.3 1.953-1.05 3.02"
    "-.885 1.051-2.127 2.75-2.716 4.521-.278.832-.41 1.684-.287 2.489a.424.424 0 00-.11.135c-.26.268-.45.6-.663.839"
    "-.199.199-.485.267-.797.4-.313.136-.658.269-.864.68-.09.189-.136.394-.132.602 0 .199.027.4.055.536.058.399.116.728.04.97"
    "-.249.68-.28 1.145-.106 1.484.174.334.535.47.94.601.81.2 1.91.135 2.774.6.926.466 1.866.67 2.616.47.526-.116.97-.464 1.208-.946"
    ".587-.003 1.23-.269 2.26-.334.699-.058 1.574.267 2.577.2.025.134.063.198.114.333l.003.003c.391.778 1.113 1.132 1.884 1.071"
    ".771-.06 1.592-.536 2.257-1.306.631-.765 1.683-1.084 2.378-1.503.348-.199.629-.469.649-.853.023-.4-.2-.811-.714-1.376v-.097"
    "l-.003-.003c-.17-.2-.25-.535-.338-.926-.085-.401-.182-.786-.492-1.046h-.003c-.059-.054-.123-.067-.188-.135"
    "a.357.357 0 00-.19-.064c.431-1.278.264-2.55-.173-3.694-.533-1.41-1.465-2.638-2.175-3.483-.796-1.005-1.576-1.957-1.56-3.368"
    ".026-2.152.236-6.133-3.544-6.139zm.529 3.405h.013c.213 0 .396.062.584.198.19.135.33.332.438.533.105.259.158.459.166.724"
    "0-.02.006-.04.006-.06v.105a.086.086 0 01-.004-.021l-.004-.024a1.807 1.807 0 01-.15.706.953.953 0 01-.213.335"
    ".71.71 0 00-.088-.042c-.104-.045-.198-.064-.284-.133a1.312 1.312 0 00-.22-.066c.05-.06.146-.133.183-.198"
    ".053-.128.082-.264.088-.402v-.02a1.21 1.21 0 00-.061-.4c-.045-.134-.101-.2-.183-.333-.084-.066-.167-.132-.267-.132h-.016"
    "c-.093 0-.176.03-.262.132a.8.8 0 00-.205.334 1.18 1.18 0 00-.09.4v.019c.002.089.008.179.02.267-.193-.067-.438-.135-.607-.202"
    "a1.635 1.635 0 01-.018-.2v-.02a1.772 1.772 0 01.15-.768c.082-.22.232-.406.43-.533a.985.985 0 01.594-.2zm-2.962.059h.036"
    "c.142 0 .27.048.399.135.146.129.264.288.344.465.09.199.14.4.153.667v.004c.007.134.006.2-.002.266v.08c-.03.007-.056.018-.083.024"
    "-.152.055-.274.135-.393.2.012-.09.013-.18.003-.267v-.015c-.012-.133-.04-.2-.082-.333a.613.613 0 00-.166-.267"
    ".248.248 0 00-.183-.064h-.021c-.071.006-.13.04-.186.132a.552.552 0 00-.12.27.944.944 0 00-.023.33v.015c.012.135.037.2.08.334"
    ".046.134.098.2.166.268.01.009.02.018.034.024-.07.057-.117.07-.176.136a.304.304 0 01-.131.068 2.62 2.62 0 01-.275-.402"
    "a1.772 1.772 0 01-.155-.667 1.759 1.759 0 01.08-.668 1.43 1.43 0 01.283-.535c.128-.133.26-.2.418-.2zm1.37 1.706"
    "c.332 0 .733.065 1.216.399.293.2.523.269 1.052.468h.003c.255.136.405.266.478.399v-.131a.571.571 0 01.016.47"
    "c-.123.31-.516.643-1.063.842v.002c-.268.135-.501.333-.775.465-.276.135-.588.292-1.012.267a1.139 1.139 0 01-.448-.067"
    "3.566 3.566 0 01-.322-.198c-.195-.135-.363-.332-.612-.465v-.005h-.005c-.4-.246-.616-.512-.686-.71-.07-.268-.005-.47.193-.6"
    ".224-.135.38-.271.483-.336.104-.074.143-.102.176-.131h.002v-.003c.169-.202.436-.47.839-.601.139-.036.294-.065.466-.065z"
)

DOCKER_PATH = (
    "M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888"
    "c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185"
    "v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185"
    "v1.887c0 .102.082.185.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V6.29a.185.185 0 00-.185-.185H8.1a.185.185 0 00-.185.185"
    "v1.887c0 .102.083.185.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V6.29a.185.185 0 00-.185-.185H5.136a.186.186 0 00-.186.185"
    "v1.887c0 .102.084.185.186.186m5.893 2.715h2.118a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0 00-.185.185"
    "v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185"
    "v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.185.185 0 00.185-.185V9.006a.185.185 0 00-.184-.186h-2.12a.186.186 0 00-.186.186"
    "v1.887c0 .102.084.185.186.185m-2.92 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185"
    "v1.888c0 .102.082.185.185.185M23.763 9.89c-.065-.051-.672-.51-1.954-.51-.338.001-.676.03-1.01.087-.248-1.7-1.653-2.53-1.716-2.566"
    "l-.344-.199-.226.327c-.284.438-.49.922-.612 1.43-.23.97-.09 1.882.403 2.661-.595.332-1.55.413-1.744.42H.751a.751.751 0 00-.75.748"
    " 11.376 11.376 0 00.692 4.062c.545 1.428 1.355 2.48 2.41 3.124 1.18.723 3.1 1.137 5.275 1.137.983.003 1.963-.086 2.93-.266"
    "a12.248 12.248 0 003.823-1.389c.98-.567 1.86-1.288 2.61-2.136 1.252-1.418 1.998-2.997 2.553-4.4h.221c1.372 0 2.215-.549 2.68-1.009"
    ".309-.293.55-.65.707-1.046l.098-.288Z"
)

TYPESCRIPT_PATH = (
    "M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75"
    "c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2"
    "c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444"
    "s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253"
    "0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164"
    "5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38"
    "a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405"
    "-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201"
    "zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z"
)

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
        f'  <desc id="desc">Animated terminal profile cycling NestJS, Linux, Docker and TypeScript every 3 seconds.</desc>',
        '  <defs>',
        f'    <filter id="{filter_id}" x="-20%" y="-20%" width="140%" height="140%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
        '    <linearGradient id="cyberBorderAnim" x1="0%" y1="0%" x2="100%" y2="100%">',
        f'      <stop offset="0%" stop-color="{cyan_accent}"/>',
        f'      <stop offset="50%" stop-color="{purple_accent}"/>',
        f'      <stop offset="100%" stop-color="{pink_accent}"/>',
        '    </linearGradient>',
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

        f'  <!-- ==================== LEFT PANEL: ROTATING TECH LOGOS (3s CYCLE) ==================== -->',
        f'  <rect x="35" y="76" width="418" height="500" rx="8" fill="{panel_inner}" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <path d="M35 116 H453" stroke="{line_color}" stroke-width="1.5"/>',
        f'  <text x="49" y="101" class="mono" font-size="13" font-weight="700" fill="{cyan_accent}" letter-spacing="1">⚡ RUNTIME.ENGINE // MODULES</text>',
        f'  <text x="365" y="101" class="mono" font-size="11" fill="{pink_accent}">[3s_LOOP]</text>',

        f'  <!-- Visual Canvas for Logos -->',
        f'  <rect x="49" y="128" width="390" height="392" rx="8" fill="{panel_bg}" stroke="{line_color}" stroke-width="1"/>',

        f'  <!-- Futuristic Cyber Rings in Background -->',
        f'  <circle cx="244" cy="310" r="145" fill="none" stroke="{line_color}" stroke-width="1" stroke-dasharray="6,8" opacity="0.5"/>',
        f'  <circle cx="244" cy="310" r="115" fill="none" stroke="{cyan_accent}" stroke-width="1" stroke-dasharray="4,6" opacity="0.35">',
        f'    <animateTransform attributeName="transform" type="rotate" from="0 244 310" to="360 244 310" dur="20s" repeatCount="indefinite"/>',
        f'  </circle>',
        f'  <circle cx="244" cy="310" r="85" fill="none" stroke="{pink_accent}" stroke-width="1" stroke-dasharray="3,5" opacity="0.4">',
        f'    <animateTransform attributeName="transform" type="rotate" from="360 244 310" to="0 244 310" dur="15s" repeatCount="indefinite"/>',
        f'  </circle>',
    ]

    # Animation Cycle: 12 seconds total (4 logos * 3s each)
    # Logo 1: NestJS (0s - 3s)
    svg_parts.extend([
        f'  <!-- 01. NESTJS LOGO (0s - 3s) -->',
        f'  <g id="logo-nestjs">',
        f'    <animate attributeName="opacity" dur="12s" repeatCount="indefinite" keyTimes="0;0.02;0.23;0.25;0.98;1" values="1;1;1;0;0;1"/>',
        f'    <g transform="translate(164, 230) scale(6.66)">',
        f'      <path d="{NESTJS_PATH}" fill="#ea284e" filter="url(#{filter_id})"/>',
        f'    </g>',
        f'    <!-- Telemetry Label -->',
        f'    <text x="244" y="445" text-anchor="middle" class="mono" font-size="14" font-weight="700" fill="#ea284e">NESTJS FRAMEWORK</text>',
        f'    <text x="244" y="468" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Scalable Node.js Architecture</text>',
        f'    <rect x="184" y="485" width="120" height="20" rx="4" fill="#ea284e" fill-opacity="0.15" stroke="#ea284e" stroke-width="1"/>',
        f'    <text x="244" y="499" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#ea284e">ACTIVE // 01 of 04</text>',
        f'  </g>',

        f'  <!-- 02. LINUX LOGO (3s - 6s) -->',
        f'  <g id="logo-linux" opacity="0">',
        f'    <animate attributeName="opacity" dur="12s" repeatCount="indefinite" keyTimes="0;0.23;0.25;0.48;0.50;1" values="0;0;1;1;0;0"/>',
        f'    <g transform="translate(164, 230) scale(6.66)">',
        f'      <path d="{LINUX_PATH}" fill="{yellow_accent if is_dark else "#d97706"}" filter="url(#{filter_id})"/>',
        f'    </g>',
        f'    <!-- Telemetry Label -->',
        f'    <text x="244" y="445" text-anchor="middle" class="mono" font-size="14" font-weight="700" fill="{yellow_accent if is_dark else "#d97706"}">LINUX ENVIRONMENT</text>',
        f'    <text x="244" y="468" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Server CLI · Bash · POSIX Core</text>',
        f'    <rect x="184" y="485" width="120" height="20" rx="4" fill="{yellow_accent if is_dark else "#d97706"}" fill-opacity="0.15" stroke="{yellow_accent if is_dark else "#d97706"}" stroke-width="1"/>',
        f'    <text x="244" y="499" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{yellow_accent if is_dark else "#d97706"}">ACTIVE // 02 of 04</text>',
        f'  </g>',

        f'  <!-- 03. DOCKER LOGO (6s - 9s) -->',
        f'  <g id="logo-docker" opacity="0">',
        f'    <animate attributeName="opacity" dur="12s" repeatCount="indefinite" keyTimes="0;0.48;0.50;0.73;0.75;1" values="0;0;1;1;0;0"/>',
        f'    <g transform="translate(164, 230) scale(6.66)">',
        f'      <path d="{DOCKER_PATH}" fill="#2496ed" filter="url(#{filter_id})"/>',
        f'    </g>',
        f'    <!-- Telemetry Label -->',
        f'    <text x="244" y="445" text-anchor="middle" class="mono" font-size="14" font-weight="700" fill="#2496ed">DOCKER ENGINE</text>',
        f'    <text x="244" y="468" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Containers · Microservices Deployment</text>',
        f'    <rect x="184" y="485" width="120" height="20" rx="4" fill="#2496ed" fill-opacity="0.15" stroke="#2496ed" stroke-width="1"/>',
        f'    <text x="244" y="499" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#2496ed">ACTIVE // 03 of 04</text>',
        f'  </g>',

        f'  <!-- 04. TYPESCRIPT LOGO (9s - 12s) -->',
        f'  <g id="logo-typescript" opacity="0">',
        f'    <animate attributeName="opacity" dur="12s" repeatCount="indefinite" keyTimes="0;0.73;0.75;0.98;1" values="0;0;1;1;0"/>',
        f'    <g transform="translate(164, 230) scale(6.66)">',
        f'      <path d="{TYPESCRIPT_PATH}" fill="#3178c6" filter="url(#{filter_id})"/>',
        f'    </g>',
        f'    <!-- Telemetry Label -->',
        f'    <text x="244" y="445" text-anchor="middle" class="mono" font-size="14" font-weight="700" fill="#3178c6">TYPESCRIPT RUNTIME</text>',
        f'    <text x="244" y="468" text-anchor="middle" class="mono" font-size="11" fill="{muted_text}">Type-Safe Backend Engineering</text>',
        f'    <rect x="184" y="485" width="120" height="20" rx="4" fill="#3178c6" fill-opacity="0.15" stroke="#3178c6" stroke-width="1"/>',
        f'    <text x="244" y="499" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#3178c6">ACTIVE // 04 of 04</text>',
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
    print(f"Generated animated banner: {output_path} ({os.path.getsize(output_path):,} bytes)")

if __name__ == '__main__':
    base_dir = r"C:\Users\Door\Documents\github-doriam-profile"
    assets_dir = os.path.join(base_dir, "assets")

    for suffix in ["", ".v2", ".v3"]:
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
