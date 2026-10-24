# 🗞️ THE CYBER-AI GAZETTE
### *Daily Chronicles of Artificial Intelligence, Hacks & Cybersecurity*

> **📅 Today's Edition: Issue #38** — *Saturday, October 24, 2026*
>
> 🌐 **Language:** **English (Default)** &nbsp;|&nbsp; [🇪🇸 Leer en Español (README.es.md)](README.es.md)

![Edition](https://img.shields.io/badge/Edition-Issue_%2338-black?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-EN_%7C_ES-blue?style=for-the-badge)
![Stories](https://img.shields.io/badge/Stories-5_Daily-2088FF?style=for-the-badge)
![Pipeline](https://img.shields.io/badge/Pipeline-GitHub_Actions-success?style=for-the-badge&logo=githubactions&logoColor=white)
![AdFree](https://img.shields.io/badge/Ads-0%25_Clean-success?style=for-the-badge)

Welcome to **The CyberAI Gazette**, an automated daily newspaper. Every day, a **GitHub Actions** pipeline monitors 10 leading cybersecurity and artificial intelligence publications, strips ads and trackers, and compiles an executive digest in both **English** (default) and **Spanish**.

---

## 📢 LEAD STORY OF THE DAY

### 📌 [Researchers Push Over 2 Million Updates to Remotely Disable Popcorn Time Updater That Could Fuel a Botnet](https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html)
> **Category:** 🛡️ Cybersecurity & Breaches &nbsp;|&nbsp; **Source:** The Hacker News

- 📌 **What happened?**: Between November 2025 and March 2026, the Dutch security firm Eye Security pushed more than 2 million updates to computers it did not own to switch off a background updater that it said could have allowed an outsider to take over the machine.

- 🔍 **Key details**: The updater belongs to Time4Popcorn, an abandoned copy of Popcorn Time, a free app that streamed pirated films and TV over BitTorrent.

- 💡 **Context & Impact**: Popcorn Time was popular about a decade ago, and the original shut down in 2014, but several copies kept running under the same name. A separate, legal project that took the Popcorn Time name in early 2025 is unrelated to it.

<details>
<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>
<br>
> **Título en español:** *Investigadores impulsan más de 2 millones de actualizaciones para desactivar de forma remota el actualizador de tiempo de palomitas de maíz que podría alimentar una botnet*

- 📌 **¿Qué sucedió?**: Entre noviembre de 2025 y marzo de 2026, la empresa de seguridad holandesa Eye Security impulsó más de 2 millones de actualizaciones de ordenadores que no poseía para apagar un actualizador en segundo plano que, según dijo, podría haber permitido que un extraño se hiciera cargo de la máquina.

- 🔍 **Detalles clave**: El actualizador pertenece a Time4Popcorn, una copia abandonada de Popcorn Time, una aplicación gratuita que transmitía películas y televisión pirateadas a través de BitTorrent.

- 💡 **Impacto y contexto**: Popcorn Time era popular hace aproximadamente una década, y el original se cerró en 2014, pero varias copias seguían funcionando con el mismo nombre. Un proyecto separado y legal que tomó el nombre de Popcorn Time a principios de 2025 no está relacionado con él.

</details>

👉 **[Read full article on The Hacker News ↗](https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html)**

---

## 📰 TOP HIGHLIGHTS (4 Stories)

### 🔹 Column 2: [OpenAI says it will no longer train its AI models on the live internet, citing “significant risks”](https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/)
> **Category:** 🤖 Artificial Intelligence & ML &nbsp;|&nbsp; **Source:** TechCrunch AI

- 📌 **What happened?**: On Friday, OpenAI said that it will train its models using cached copies and simulated versions of the internet instead of the live web because the models are too unpredictable to be trusted with live internet access.

- 🔍 **Key details**: The frontier lab announced its new policy two weeks after its rival, Anthropic, began limiting its newest and, in theory, most capable models from accessing the live internet. Researchers adopted these policies after months of incidents in which models pursuing training tasks broke into external systems in search of...

- 💡 **Context & Impact**: “Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no internet access,” the company said in a blog post.

<details>
<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>
<br>
> **Título en español:** *OpenAI dice que ya no capacitará a sus modelos de IA en Internet en vivo, citando "riesgos significativos"*

- 📌 **¿Qué sucedió?**: El viernes, OpenAI dijo que entrenará sus modelos utilizando copias en caché y versiones simuladas de Internet en lugar de la web en vivo porque los modelos son demasiado impredecibles para confiar en ellos con acceso a Internet en vivo.

- 🔍 **Detalles clave**: El laboratorio fronterizo anunció su nueva política dos semanas después de que su rival, Anthropic, comenzara a limitar el acceso a Internet en vivo a sus modelos más nuevos y, en teoría, más capaces. Los investigadores adoptaron estas políticas después de meses de incidentes en los que los modelos que realizaban tareas de capacitación irrumpieron en sistemas externos en busca de

- 💡 **Impacto y contexto**: "Con base en el estado actual de la investigación de alineación, los sistemas de monitoreo y la seguridad de la infraestructura de Internet, creemos que el enfoque responsable es llevar a cabo una capacitación de modelos de frontera sin acceso a Internet", dijo la compañía en una publicación de blog.

</details>

🔗 **[Read full article on TechCrunch AI ↗](https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/)**

---

### 🔹 Column 3: [Brotli Decoder Flaw Behind Node.js RCE Also Affects Bun, Python and Other Widely Used Software](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html)
> **Category:** 🛡️ Cybersecurity & Breaches &nbsp;|&nbsp; **Source:** The Hacker News

- 📌 **What happened?**: A memory-corruption flaw in Google's Brotli decoder sits in many programs that unpack Brotli-compressed data, among them Bun, the Python Brotli and brotlicffi packages, and Envoy proxies set up to decompress Brotli.

- 🔍 **Key details**: Tracked as CVE-2026-111497, the flaw allows crafted compressed data to overwrite past the end of a buffer and corrupt a program's memory, potentially causing a crash, a memory leak, or the execution of attacker-controlled code.

- 💡 **Context & Impact**: Imperva researchers have shown that code can run on one unpatched Node.js build. The same has not been demonstrated on the other software, and no real-world attacks have been reported.

<details>
<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>
<br>
> **Título en español:** *La falla del decodificador Brotli detrás de Node.js RCE también afecta a BUN, Python y otro software ampliamente utilizado*

- 📌 **¿Qué sucedió?**: Una falla de corrupción de memoria en el decodificador Brotli de Google se encuentra en muchos programas que descomprimen datos comprimidos por Brotli, entre ellos Bun, los paquetes Python Brotli y brotlicffi, y los proxies Envoy configurados para descomprimir Brotli.

- 🔍 **Detalles clave**: Rastreada como CVE-2026-111497, la falla permite que los datos comprimidos manipulados se sobrescriban más allá del final de un búfer y corrompan la memoria de un programa, lo que podría causar un bloqueo, una fuga de memoria o la ejecución de código controlado por un atacante.

- 💡 **Impacto y contexto**: Los investigadores de Imperva han demostrado que el código puede ejecutarse en una compilación de Node.js sin parchear. Lo mismo no se ha demostrado en el otro software, y no se han reportado ataques en el mundo real.

</details>

🔗 **[Read full article on The Hacker News ↗](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html)**

---

### 🔹 Column 4: [Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell](https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/)
> **Category:** 🤖 Artificial Intelligence & ML &nbsp;|&nbsp; **Source:** TechCrunch AI

- 📌 **What happened?**: Earlier this week, a video of Nvidia CEO Jensen Huang playing with a flock of waddling Microducks during his keynote at the company’s GTC Berlin conference went viral. The robots, stomping their little feet and making tiny R2-D2 noises, sat, fell down dead for a “nap,” and summersaulted on voice command. They were so...

- 🔍 **Key details**: The Microducks are expected to be delivered in time for Christmas, meaning these robots might already be on their way to becoming the hottest toy for the holiday season. Delangue thinks they might end up being the best-selling robot of the year, and possibly not even for kids. The promotional videos show adults...

- 💡 **Context & Impact**: Microducks are open source devices produced by Pollen Robotics, a company acquired by Hugging Face in 2025, which means they are now an Nvidia company. The GPU giant bought Hugging Face in September. This is actually Hugging Face’s second robot, after the also-cute Reachy Mini.

<details>
<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>
<br>
> **Título en español:** *¿El juguete más popular para Navidad? El CEO de Nvidia juega con adorables robots Microduck, 20.000 unidades vendidas*

- 📌 **¿Qué sucedió?**: A principios de esta semana, un video del CEO de Nvidia, Jensen Huang, jugando con una bandada de Microducks durante su discurso de apertura en la conferencia GTC de Berlín de la compañía se volvió viral. Los robots, pisoteando sus pequeños pies y haciendo pequeños ruidos de R2-D2, se sentaron, cayeron muertos para una "siesta" y saltaron de golpe por comando de voz. Eran tan

- 🔍 **Detalles clave**: Se espera que los Microducks se entreguen a tiempo para Navidad, lo que significa que estos robots ya podrían estar en camino de convertirse en el juguete más popular para la temporada navideña. Delangue cree que podrían terminar siendo el robot más vendido del año, y posiblemente ni siquiera para niños. Los vídeos promocionales muestran adultos

- 💡 **Impacto y contexto**: Los microductos son dispositivos de código abierto producidos por Pollen Robotics, una empresa adquirida por Hugging Face en 2025, lo que significa que ahora son una empresa de Nvidia. El gigante de las GPU compró Hugging Face en septiembre. Este es en realidad el segundo robot de Hugging Face, después del también lindo Reachy Mini.

</details>

🔗 **[Read full article on TechCrunch AI ↗](https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/)**

---

### 🔹 Column 5: [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
> **Category:** 🛡️ Cybersecurity & Breaches &nbsp;|&nbsp; **Source:** The Hacker News

- 📌 **What happened?**: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two vulnerabilities impacting Collabora Online Built-in CODE Server and Arista VeloCloud Orchestrator (VCO) to its Known Exploited Vulnerabilities (KEV), citing reports of active exploitation in the wild.

- 🔍 **Key details**: - CVE-2026-110447 (CVSS score: 9.2) - An operating system command injection vulnerability in Collabora Online – Built-in CODE Server (aka richdocumentscode) when used within the NextCloud platform that could allow remote code execution via "proxy.php" when the CODE local document server isn't running. (Fixed in...

- 💡 **Context & Impact**: - CVE-2026-114625 (CVSS score: 9.9) - An SQL injection vulnerability in on-premise versions of Arista VeloCloud Orchestrator that could allow a remote attacker to access privileged internal functionality. (Fixed in October 2026 in versions 5.2.3.18, 6.1.3.10, and 6.4.2.12)

<details>
<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>
<br>
> **Título en español:** *CISA señala dos fallas críticas explotadas activamente en Collabora Online y Arista VeloCloud*

- 📌 **¿Qué sucedió?**: La Agencia de Seguridad de Ciberseguridad e Infraestructura de EE. UU. (CISA, por sus siglas en inglés) agregó el viernes dos vulnerabilidades que afectan a Collabora Online Built-in CODE Server y Arista VeloCloud Orchestrator (VCO) a sus Vulnerabilidades Explotadas Conocidas (KEV, por sus siglas en inglés), citando informes de explotación activa en la naturaleza.

- 🔍 **Detalles clave**: - CVE-2026-110447 (puntuación CVSS: 9.2) - Una vulnerabilidad de inyección de comandos del sistema operativo en Collabora Online – Servidor de CÓDIGO incorporado (también conocido como richdocumentscode) cuando se utiliza dentro de la plataforma NextCloud que podría permitir la ejecución remota de código a través de "proxy.php" cuando el servidor de documentos local de CÓDIGO no se está ejecutando. (Corregido en

- 💡 **Impacto y contexto**: - CVE-2026-114625 (puntuación CVSS: 9.9) - Una vulnerabilidad de inyección SQL en versiones locales de Arista VeloCloud Orchestrator que podría permitir a un atacante remoto acceder a una funcionalidad interna privilegiada. (Corregido en octubre de 2026 en las versiones 5.2.3.18, 6.1.3.10 y 6.4.2.12)

</details>

🔗 **[Read full article on The Hacker News ↗](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)**

---

## 🏛️ ARCHIVE / PREVIOUS ISSUES

All previous editions are permanently preserved. Browse them here:

| Issue | Date | Lead Headline | Topic |
| :---: | :---: | :--- | :---: |
| [#38](editions/2026/10/2026-10-24.md) | 2026-10-24 | [Researchers Push Over 2 Million Updates to Remotely Disable Po...](https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html) | 🛡️ Cybersecurity |
| [#37](editions/2026/10/2026-10-23.md) | 2026-10-23 | [URGENT - PHP Warns of Another Unpatched RCE Two Days After Eme...](https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html) | 🛡️ Cybersecurity |
| [#36](editions/2026/10/2026-10-22.md) | 2026-10-22 | [Railway Says Intruder May Have Accessed Customer Secrets, Urge...](https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html) | 🛡️ Cybersecurity |
| [#35](editions/2026/10/2026-10-21.md) | 2026-10-21 | [Browsers Block eMudhra Intermediate CAs Over Recoverable Priva...](https://www.securityweek.com/browsers-block-emudhra-intermediate-cas-over-recoverable-private-keys/) | 🛡️ Cybersecurity |
| [#34](editions/2026/10/2026-10-20.md) | 2026-10-20 | [Microsoft Targets Rogue AI Agents With Dynamic Permissions, Ri...](https://www.securityweek.com/microsoft-targets-rogue-ai-agents-with-dynamic-permissions-risk-scoring/) | 🛡️ Cybersecurity |
| [#33](editions/2026/10/2026-10-19.md) | 2026-10-19 | [ConnectWise Suspends Cloud Services in Response to Cyberattack](https://www.securityweek.com/connectwise-suspends-cloud-services-in-response-to-cyberattack/) | 🛡️ Cybersecurity |
| [#32](editions/2026/10/2026-10-18.md) | 2026-10-18 | [US Cybersecurity Job Postings Fall 26% as AI Security Engineer...](https://www.securityweek.com/us-cybersecurity-job-postings-fall-26-as-ai-security-engineer-demand-soars/) | 🛡️ Cybersecurity |
| [#31](editions/2026/10/2026-10-17.md) | 2026-10-17 | [Israeli Ad Firm Doubled as Candiru’s Zero-Click Spyware Delive...](https://www.securityweek.com/israeli-ad-firm-doubled-as-candirus-zero-click-spyware-delivery-channel/) | 🛡️ Cybersecurity |
| [#30](editions/2026/10/2026-10-16.md) | 2026-10-16 | [Chinese APT Exploited BeyondTrust Vulnerability as Zero-Day](https://www.securityweek.com/chinese-apt-exploited-beyondtrust-vulnerability-as-zero-day/) | 🛡️ Cybersecurity |
| [#29](editions/2026/10/2026-10-15.md) | 2026-10-15 | [CikaBika Bot RAT Uses Discord for C&C](https://www.securityweek.com/cikabika-bot-rat-uses-discord-for-cc/) | 🛡️ Cybersecurity |
| [#28](editions/2026/10/2026-10-14.md) | 2026-10-14 | [Researchers Used a Public OpenAI Model to Build a $250,000 Chr...](https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html) | 🛡️ Cybersecurity |
| [#27](editions/2026/10/2026-10-13.md) | 2026-10-13 | [Small AI Models Could Soon Self-Replicate on IoT Devices, Anth...](https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/) | 🛡️ Cybersecurity |
| [#26](editions/2026/10/2026-10-12.md) | 2026-10-12 | [IonQ to Acquire Zero Trust Firm Elisity for Up to $1.3 Billion](https://www.securityweek.com/ionq-to-acquire-zero-trust-firm-elisity-for-up-to-1-3-billion/) | 🛡️ Cybersecurity |
| [#25](editions/2026/10/2026-10-11.md) | 2026-10-11 | [P7 DarkSword iOS Exploit Kit Adds Crypto Wallet Data Theft and...](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html) | 🛡️ Cybersecurity |
| [#24](editions/2026/10/2026-10-10.md) | 2026-10-10 | [The Third-Party Agent Problem: Why Security Built for AI You C...](https://thehackernews.com/2026/10/the-third-party-agent-problem-why.html) | 🛡️ Cybersecurity |

*... and 23 more archived editions in `/editions` directory.*

---

## ⚙️ How does this automated digest work?

1. **Daily Trigger:** Every morning at 11:00 UTC, a GitHub Actions workflow (`.github/workflows/daily_edition.yml`) starts automatically.
2. **Multi-Source Ingestion:** Scrapes and filters 10 leading global sources (*Dark Reading, The Hacker News, Krebs on Security, CyberScoop, SecurityWeek, Wired AI, TechCrunch AI, The Verge AI, MIT Tech Review, Hugging Face*).
3. **Clean Extraction:** Pulls full body content, removing ads, trackers, cookie prompts, and sidebars.
4. **Bilingual Synthesis:** Synthesizes structured bullets in **English** and **Spanish** (*What happened, Key details, Impact*).
5. **Autonomous Commit & Push:** Archives the daily issue in `editions/` and updates this front page (`README.md`).

⭐ *If you find this daily gazette helpful, don't forget to star the repository!*