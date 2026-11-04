# BIM & MEP Automation Workflows

Open-source Revit Dynamo scripts, Python automation utilities, and BIM coordination workflows designed to streamline MEP modeling and design automation.

## 📌 Project Overview
This repository provides automated scripts and graph utilities aimed at eliminating repetitive tasks, optimizing pipe/duct parameter sync, and refining clash resolution workflows within Autodesk Revit.

### Key Features
- **Parameter Synchronization:** Automates room and space parameter transfers to connected MEP elements.
- **Clash Processing:** Utilities to parse and organize Navisworks clash reports for efficient coordination.
- **Data Cleanup:** Scripts for purging unused parameters and normalizing shared parameters across Revit families.

## 🛠️ Environment & Prerequisites
- **Autodesk Revit:** 2023 / 2024 / 2025 / 2026
- **Dynamo Core:** 2.x or higher (IronPython 2.7 / CPython 3 engines)
- **Packages Used:** Clockwork, Rhythm, custom Python nodes

## 📂 Repository Structure
```
├── dyn/           # Revit Dynamo graphs (.dyn)
├── python/        # Standalone Python scripts (.py) for Dynamo node blocks
├── samples/       # Sample datasets and test files
├── LICENSE        # MIT License
└── README.md      # Project documentation
```

## 🚀 Getting Started
1. Clone or download the repository:
   ```bash
   git clone https://github.com/Ronit-Sonawane/Ronit.git
   ```
2. Open Autodesk Revit and launch **Dynamo Player**.
3. Point Dynamo Player to the directory containing the desired script from `dyn/`.

## 🤝 Contributing
Contributions, bug reports, and feature requests for MEP automation workflows are welcome. Feel free to open an issue or submit a pull request!

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
