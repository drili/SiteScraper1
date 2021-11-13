<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability...
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
-->


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project can fetch URL's from any section of a website, and further use these URL's to fetch the HTML-structure that you specify and exported automatically as a .csv file with the contents.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This project is built with the code languages and frameworks/libraries.

* [Python](#)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This project uses several python packages that you must install in order to run this project.

### Prerequisites

List of python packages: (use npm, examples listed from python code)
* packages
     ```sh
     import requests
     from bs4 import BeautifulSoup
     import re
     import csv
     import bleach
     import lxml.html.clean as clean
     ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone this repo.
     ```sh
     git clone https://github.com/drili/SiteScraper1.git
     ```
3. Install the packages listed under 'Prerequisites'
4. Open `url_scraper.py` and change the URL (variable -> URL)
     ```py
     URL = "https://www.example.dk/blog"
     ```
5. Inside `url_scraper.py`, change the "js-render-wrapper" class to the respective class that you wish to target.
6. Inside `url_scraper.py`, change parameters of the following code, to your respective URL:
     ```py
     lines_txt.append("https://www.example.dk/blog" + a['href'])
     ```
7. Open `scraper.py`, change parameters of the following code, to your respective class that you wish to target:
     ```py
     content_elements = soup.find_all("div", class_="learnworlds-section-content")
     ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

To be updated...

_For more examples, please refer to the [Documentation](#)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

### Version 1.1
- [x] Fetch data and import automatically to a newly generated CSV file.
- [x] Add CSV support with correct encoding.
- [x] Add headers to CSV with modified parameters.
- [ ] Add input fields to python files, so users can define required variable values inside of the command-prompt.

### Version 1.2
- [ ] Turn project into .exe program, so users can insert values inside of a GUI.
    - [ ] Being able to define every single dynamic value and parameters

For further information, visit [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!--
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
-->
