# Countries Data Management and Visualization

This project provides tools to scrape, manage, and visualize data about countries. It includes two Python scripts: 
- `world_countries_scraper.py`: Scrapes country data from a website.
- `countries_manager.py`: Allows for filtering, sorting, saving, and visualizing country data.

---

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
  - [Scraping Data](#scraping-data)
  - [Managing Data](#managing-data)
  - [Visualizing Data](#visualizing-data)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### `world_countries_scraper.py`
- Scrapes the following data from [Scrape This Site](https://www.scrapethissite.com/pages/simple/):
  - Country Name
  - Capital
  - Population
  - Area (in km²)
- Saves the scraped data to a CSV file for analysis.

### `countries_manager.py`
- **Filter Data**:
  - Filter countries by population or area.
  - Search for countries starting with a specific letter.
- **Sort Data**:
  - Sort by any column (e.g., population, area) in ascending or descending order.
- **Add Calculations**:
  - Add a population density column (people per square kilometer).
- **Visualizations**:
  - Generate bar plots of countries by population.
  - Customize visualizations with Seaborn and Matplotlib.

---

## Setup

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or later
- Required Python packages (see Dependencies below).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/countries-data.git
   cd countries-data

