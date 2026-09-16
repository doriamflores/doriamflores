// Doriam Flores - Minimalist CV & Tech Portfolio (Bilingual ES/EN)
let currentLang = localStorage.getItem("doriam_cv_lang") || "es";

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initLanguage();
  renderApp();
});

/* ==========================================================================
   Language Management (ES / EN)
   ========================================================================== */
function initLanguage() {
  const langTabs = document.querySelectorAll(".btn-lang-tab");
  
  updateLangTabUI();

  langTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const selected = tab.getAttribute("data-lang");
      if (selected !== currentLang) {
        currentLang = selected;
        localStorage.setItem("doriam_cv_lang", currentLang);
        updateLangTabUI();
        renderApp();
      }
    });
  });
}

function updateLangTabUI() {
  document.documentElement.setAttribute("lang", currentLang);
  document.querySelectorAll(".btn-lang-tab").forEach(tab => {
    if (tab.getAttribute("data-lang") === currentLang) {
      tab.classList.add("active");
    } else {
      tab.classList.remove("active");
    }
  });
}

function getActiveData() {
  return (typeof CV_DATA_I18N !== "undefined" && CV_DATA_I18N[currentLang]) 
    ? CV_DATA_I18N[currentLang] 
    : CV_DATA;
}

function renderApp() {
  const data = getActiveData();
  renderStaticUI(data);
  renderProfile(data);
  renderSkills(data);
  renderExperience(data);
}

function renderStaticUI(data) {
  const ui = data.ui;
  if (!ui) return;

  // Nav
  document.getElementById("navAbout").textContent = ui.navAbout;
  document.getElementById("navSkills").textContent = ui.navSkills;
  document.getElementById("navExperience").textContent = ui.navExperience;
  document.getElementById("btnExportPdfText").textContent = ui.exportPdf;
  const elOpen = document.getElementById("heroOpenToWork"); if (elOpen) elOpen.textContent = ui.openToWork;

  // Section Headers
  document.getElementById("tagAbout").textContent = ui.tagAbout;
  document.getElementById("titleAbout").textContent = ui.titleAbout;
  document.getElementById("tagSkills").textContent = ui.tagSkills;
  document.getElementById("titleSkills").textContent = ui.titleSkills;
  document.getElementById("subtitleSkills").textContent = ui.subtitleSkills;
  document.getElementById("tagExperience").textContent = ui.tagExperience;
  document.getElementById("titleExperience").textContent = ui.titleExperience;
  document.getElementById("subtitleExperience").textContent = ui.subtitleExperience;

  // Footer & Title
  const elRole = document.getElementById("footerRole"); if (elRole) elRole.textContent = data.profile.role;
  const elLoc = document.getElementById("footerLocation"); if (elLoc) elLoc.textContent = data.profile.location;
  document.getElementById("footerSubtitle").textContent = ui.footerText;
  document.getElementById("pageTitle").textContent = `${data.profile.shortName} | ${data.profile.role}`;
}

/* ==========================================================================
   Theme Toggle (Dark / Light) with Persistence
   ========================================================================== */
function initTheme() {
  const themeToggleBtn = document.getElementById("themeToggle");
  const themeIcon = document.getElementById("themeIcon");
  
  const savedTheme = localStorage.getItem("doriam_cv_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeIcon(savedTheme, themeIcon);

  themeToggleBtn.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("doriam_cv_theme", next);
    updateThemeIcon(next, themeIcon);
  });
}

function updateThemeIcon(theme, iconEl) {
  if (theme === "dark") {
    iconEl.innerHTML = `
      <circle cx="12" cy="12" r="5"></circle>
      <line x1="12" y1="1" x2="12" y2="3"></line>
      <line x1="12" y1="21" x2="12" y2="23"></line>
      <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
      <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
      <line x1="1" y1="12" x2="3" y2="12"></line>
      <line x1="21" y1="12" x2="23" y2="12"></line>
      <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
      <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
    `;
  } else {
    iconEl.innerHTML = `
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    `;
  }
}

/* ==========================================================================
   Render Profile, Summary & Contact
   ========================================================================== */
function renderProfile(data) {
  const p = data.profile;
  document.getElementById("profileName").textContent = p.fullName;
  document.getElementById("profileRole").textContent = p.role;
  document.getElementById("profileLocation").textContent = p.location;

  // Render Rich Summary
  const summaryEl = document.getElementById("profileSummary");
  if (typeof p.summary === "object") {
    summaryEl.innerHTML = `
      <div class="summary-card-content">
        <p class="summary-lead">${p.summary.lead}</p>
        ${p.summary.paragraphs.map(text => `<p class="summary-paragraph">${text}</p>`).join("")}
        <div class="summary-pillars">
          ${p.summary.pillars.map((pill, idx) => `
            <div class="summary-pillar-card pillar-${idx}">
              <div class="pillar-title">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>${pill.title}</span>
              </div>
              <p class="pillar-desc">${pill.desc}</p>
            </div>
          `).join("")}
        </div>
      </div>
    `;
  } else {
    summaryEl.textContent = p.summary;
  }  // Casual Top Contact Bar (Understated, clean inline links)
  const bar = document.getElementById("contactBar");
  bar.innerHTML = `
    <a href="${p.contact.github}" target="_blank" rel="noopener" class="casual-link" title="GitHub">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
      </svg>
      <span>GitHub</span>
    </a>

    <span class="casual-sep">·</span>

    <a href="${p.contact.linkedin}" target="_blank" rel="noopener" class="casual-link" title="LinkedIn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
        <rect x="2" y="9" width="4" height="12"></rect>
        <circle cx="4" cy="4" r="2"></circle>
      </svg>
      <span>LinkedIn</span>
    </a>

    <span class="casual-sep">·</span>

    <a href="${p.contact.whatsapp}" target="_blank" rel="noopener" class="casual-link" title="WhatsApp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
      </svg>
      <span>WhatsApp</span>
    </a>

    <span class="casual-sep">·</span>

    <a href="mailto:${p.contact.email}" class="casual-link" title="Email">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
        <polyline points="22,6 12,13 2,6"></polyline>
      </svg>
      <span>Email</span>
    </a>
  `;

  // Render Footer Socials
  renderFooterSocials(p);

  // Quick Metrics
  const metricsGrid = document.getElementById("metricsGrid");
  metricsGrid.innerHTML = p.highlights.map((m, idx) => `
    <div class="metric-card color-${idx}">
      <div class="metric-number">${m.number}</div>
      <div class="metric-label">${m.label}</div>
    </div>
  `).join("");
}

/* ==========================================================================
   Render Skills
   ========================================================================== */
function renderSkills(data) {
  const grid = document.getElementById("skillsGrid");
  grid.innerHTML = data.skills.map((cat, idx) => `
    <div class="skill-category-card cat-${idx}">
      <h3 class="skill-cat-title">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="16 18 22 12 16 6"></polyline>
          <polyline points="8 6 2 12 8 18"></polyline>
        </svg>
        ${cat.category}
      </h3>
      <div class="skill-badges-container">
        ${cat.items.map(item => `
          <span class="skill-badge" title="${item.level}">
            ${item.name}
          </span>
        `).join("")}
      </div>
    </div>
  `).join("");
}

/* ==========================================================================
   Render Experience with Technologies
   ========================================================================== */
function renderExperience(data) {
  const container = document.getElementById("experienceTimeline");
  const techLabel = data.ui ? data.ui.usedTechLabel : "Tecnologías clave utilizadas";

  container.innerHTML = data.experience.map((exp, idx) => `
    <div class="timeline-item item-${idx}">
      <div class="timeline-top">
        <h3 class="timeline-role">${exp.role} · <span class="timeline-company">${exp.company}</span></h3>
        <span class="timeline-period">${exp.period}</span>
      </div>
      <div class="timeline-badge-pill">${exp.badge}</div>
      <p class="timeline-desc">${exp.description}</p>
      <ul class="achievements-list">
        ${exp.achievements.map(a => `<li>${a}</li>`).join("")}
      </ul>
      ${exp.technologies && exp.technologies.length > 0 ? `
        <div class="timeline-tech-stack">
          <span class="timeline-tech-label">${techLabel}</span>
          <div class="timeline-tech-tags">
            ${exp.technologies.map(t => `<span class="exp-tech-pill">${t}</span>`).join("")}
          </div>
        </div>
      ` : ''}
    </div>
  `).join("");
}



/* ==========================================================================
   Render Footer Social Links (Clean, Balanced Pills)
   ========================================================================== */
function renderFooterSocials(profile) {
  const container = document.getElementById("footerSocials");
  if (!container) return;

  container.innerHTML = `
    <a href="${profile.contact.github}" target="_blank" rel="noopener" class="footer-social-pill" title="GitHub">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
      </svg>
      <span>GitHub</span>
    </a>

    <a href="${profile.contact.linkedin}" target="_blank" rel="noopener" class="footer-social-pill" title="LinkedIn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
        <rect x="2" y="9" width="4" height="12"></rect>
        <circle cx="4" cy="4" r="2"></circle>
      </svg>
      <span>LinkedIn</span>
    </a>

    <a href="${profile.contact.whatsapp}" target="_blank" rel="noopener" class="footer-social-pill" title="WhatsApp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
      </svg>
      <span>WhatsApp</span>
    </a>

    <a href="mailto:${profile.contact.email}" class="footer-social-pill" title="Email">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
        <polyline points="22,6 12,13 2,6"></polyline>
      </svg>
      <span>Email</span>
    </a>
  `;
}
