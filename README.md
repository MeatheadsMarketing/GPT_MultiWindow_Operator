# 🧠 GPT MultiWindow Operator

**A multi-threaded, shortcut-enhanced assistant suite for running multiple GPT agents in parallel — with logs, validation, PDF reporting, and Streamlit-based control center.**

---

## 🚀 Features

- 🧵 **Multi-GPT Execution**: Run 3+ GPT assistants side-by-side
- 📊 **Thread Commander**: Live logs, health summaries, prompt tagging
- 🧠 **Shortcut Launcher**: Fire off modular commands like `#M`, `#X`, `#A`, `#V`
- 📤 **Digest Tools**: Auto-generate PDF reports + sync to Slack, Notion, GitHub
- 🗂️ **Directory + Execution Validators**: Avoid silent errors with `#RTE`
- 🔁 **Weekly Schedulers**: Cron-based digest generation + delivery

---

## 📂 Folder Structure
```
MultiWindow_GPT_ProductionSuite_v1.0-FINAL/
├── multi_thread_launcher.py
├── thread_configs.json
├── thread_commander_tab.py
├── shortcut_dispatcher.py
├── shortcut_launcher_tab.py
├── weekly_digest_generator.py
├── digest_github_notion_push.py
├── slack_digest_notifier.py
├── cronjob_weekly_digest.sh
├── streamlit_run_suite.sh
├── git_commit_and_tag.sh
├── repo_push.sh
├── .gitignore
├── version_manifest.json
├── CHANGELOG.md
├── README.md
└── thread_logs/
```

---

## 🔧 Quickstart

```bash
chmod +x streamlit_run_suite.sh
./streamlit_run_suite.sh
```

```bash
chmod +x git_commit_and_tag.sh repo_push.sh
./git_commit_and_tag.sh
./repo_push.sh
```

---

## 🧠 Shortcut Commands
| Shortcut | Purpose |
|----------|---------|
| `#M` | Manipulate vague prompts into elite execution |
| `#X` | Execute GPT's own strategy recursively |
| `#A` | Apply auto-enhancements and patch missing logic |
| `#V` | Validate all assistant components |
| `#RTE` | Diagnose terminal run errors (wrong path, missing file) |

---

## 📬 Outputs
- 📝 Markdown logs per thread
- 📤 Push-to-Notion + GitHub
- 📩 Slack + Email alert triggers (optional)

---

## 🔒 License
MIT — Built for streamlining elite GPT workflows.

---

## 💡 Contributed by [MeatheadsMarketing](https://github.com/MeatheadsMarketing)
