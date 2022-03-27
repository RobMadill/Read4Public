<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RobMadill/Read4Public">
    <img src="https://user-images.githubusercontent.com/19481324/158642612-e676c8ff-6e5f-40b7-9539-f7f95d419034.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Read4Public</h3>

  <p align="center">
    With this script you can tweet out your favourite phrase or word from a book every time it appears!
    <br />
    <a href="https://github.com/RobMadill/Read4Public"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/RobMadill/Read4Public">View Demo</a>
    ·
    <a href="https://github.com/RobMadill/Read4Public/issues">Report Bug</a>
    ·
    <a href="https://github.com/RobMadill/Read4Public/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
       <li><a href="#dependencies">Dependencies</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



<p align="right">(<a href="#top">back to top</a>)</p>

### Built With
* [Python - 3.8](https://www.python.org/)

#### Dependencies
* [Tweepy](https://docs.tweepy.org/en/stable/)
* [Argeparse](https://docs.python.org/3/library/argparse.html)

<p align="right">(<a href="#top">back to top</a>)</p>


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/RobMadill/Read4Public
   ```
2. Install Tweepy library 
   ```sh
   pip install tweepy
   ```
3. Twitter authentication - `config.py` file contains API Keys and Tokens
   ```python
   auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
   auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

1. Add `config.py` file
   ```python
   auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
   auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
   ```
2. Use main.py with required arguments
   ```sh
   main.py -c The_Idiot_Part_One.txt -k Idiot
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Rob Madill - [@linkedin](https://www.linkedin.com/in/robert-madill/) - robertmadill17@gmail.com

Project Link: [https://github.com/RobMadill/Read4Public](https://github.com/RobMadill/Read4Public)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Othneil Drew - README template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/RobMadill/Read4Public.svg?style=for-the-badge
[contributors-url]: https://github.com/RobMadill/Read4Public/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RobMadill/Read4Public.svg?style=for-the-badge
[forks-url]: https://github.com/RobMadill/Read4Public/network/members
[stars-shield]: https://img.shields.io/github/stars/RobMadill/Read4Public.svg?style=for-the-badge
[stars-url]: https://github.com/RobMadill/Read4Public/stargazers
[issues-shield]: https://img.shields.io/github/issues/RobMadill/Read4Public.svg?style=for-the-badge
[issues-url]: https://github.com/RobMadill/Read4Public/issues
[license-shield]: https://img.shields.io/github/license/RobMadill/Read4Public.svg?style=for-the-badge
[license-url]: https://github.com/RobMadill/Read4Public/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/robert-madill/
