<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
  

<!-- ABOUT THE PROJECT -->
## About The Project

A simple web application that works like a pokedex. The user can type the Pokemon name and the application will show information about that pokemon in a pokedex-like template.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PokeAPI](https://pokeapi.co/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip
  ```sh
  Debian/Ubuntu: apt install python3-pip	
  CentOS and RHEL: yum install python-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gugarrido/Pokemon-Project.git
   ```

2. Create Python Virtual Environment 
  ```sh
  python3 -m venv venv 
  ```
     
3. Install PIP packages
   ```sh
   pip install -r requirements.txt
   ```

4. Create a sqlite3 database inside the folder `database`

<!-- USAGE EXAMPLES -->
## Usage

1. Activate Python venv
  ```sh
  Unix or MacOS: source venv/bin/activate
  Windows: tutorial-env\Scripts\activate.bat
  ```

2. Start flask web server
  ```sh
  python python app.py  
  ```

3. Navigate to ```http://127.0.0.1:5000/```


<!-- ROADMAP -->
## Roadmap

Future roadmap includes:

1. Implement Flask-Limiter
2. Re-design form html page - Maybe move the form to the pokedex page in a way that the user doesn't need to go back to the home page
3. Implement some usage to the pokedex buttons


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Gustavo Garrido Souto - [linkedin](https://www.linkedin.com/in/gustavo-garrido-953747148/)

Project Link: [https://github.com/gugarrido/Pokemon-Project](https://github.com/gugarrido/Pokemon-Project)


