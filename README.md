# LeadFinder(Demo)

## Try it instantly in Google Colab!

Python | Playwright | Pandas | AsyncIO | MIT

**No installation required.**

👉 **[Open the demo in Google Colab](https://colab.research.google.com/drive/1kwApfSHD_no4KHo62Y2_VYJz5uaPGDlc#scrollTo=dzZoyeUKKEpd)**

LeadFinder(Demo) is a Python-based Google Maps scraper designed to collect publicly available business information and transform it into a structured dataset for lead generation, market research, and data analysis.

The project was built with a strong focus on clean architecture, modularity, and maintainability, separating data extraction from data processing to make future improvements easier.

---

> **Disclaimer:** This project is intended for educational purposes, portfolio demonstration, and market research. Users are responsible for complying with Google's Terms of Service and all applicable laws.

---

## Stacks

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="50"/>
</p>

---

## Features

* Search any Google Maps query.
* Automatically scroll through search results.
* Open each business page.
* Extract business information.
* Clean and normalize extracted data.
* Return structured data ready for export.

---

### Currently Extracted Data

* Business Name
* Google Maps URL
* Rating
* Plus Code
* Location
* Latitude
* Longitude

---

## Project Structure

```text
LeadFinder/
│
├── maps_scraper.py          # Main extraction workflow
├── loader.py           # Google Maps scrolling logic
├── data_cleaning.py    # Data parsing and normalization
├── config.py           # Project configuration
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RafaelKobayashiSantos/LeadFinder-Demo-.git
cd LeadFinder-Demo-
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
playwright install chromium
```

---

## Usage

```python
from scraper import scraper

results = await scraper("restaurants in cotia")
```

The scraper returns a structured dataset that can easily be converted into a Pandas DataFrame or exported as XLSX (Excel by default).

---

## Technologies

* Python
* Playwright
* AsyncIO
* Pandas
* Regular Expressions (Regex)

---

## Why this project?

LeadFinder was created to demonstrate practical software engineering and data engineering concepts, including:

* Asynchronous web scraping
* Data cleaning and normalization
* Modular project architecture
* ETL-style data processing
* Browser automation using Playwright

Instead of simply collecting information, the project focuses on transforming raw web data into a clean and structured dataset that can support business intelligence and lead generation workflows.

This project reflects how I approach real-world automation problems: by building maintainable, modular, and reusable solutions rather than one-off scripts.

---

## Future Improvements

* Phone number extraction
* Website extraction
* Instagram and social media detection
* Business category classification
* User interface
* CSV / Excel / JSON export options
* Docker support
* Streamlit demo
* Unit tests

---

## License

This project is available for educational and portfolio purposes.