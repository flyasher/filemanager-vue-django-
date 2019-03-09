# FileManager by <a href="https://github.com/talented">Talented</a>

<div align="center">
  <!-- <a href="https://www.paypal.me/kevinpeters96/1"><img src="https://img.shields.io/badge/Donate-Paypal-003087.svg?style=flat" alt="badge Donate" /></a>
  <a href="https://steamcommunity.com/tradeoffer/new/?partner=68364320&token=CzTCv8JM"><img src="https://img.shields.io/badge/Donate-Steam-000000.svg?style=flat" alt="badge Donate" /></a> -->
  <a href="https://github.com/igeligel/personal-site/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-1da1f2.svg?style=flat" alt="badge License" /></a>
</div>

<div style="text-align:center"><img src ="./Screenshot.png" /></div>

## Description

> A file manager web app with Django rest framework in backend and Vue.js in frontend with ag-grid data tables integration.

## System Requirements
* Python 3.6+
* pip
* virtualenv
* Node.js

## Dependencies
See [requirements.txt](https://github.com/talented/filemanager/blob/master/requirements.txt) for more information.

## Build Instructions

1. Clone the repository and get into the directory
```
git clone https://github.com/talented/FileManager.git
cd filemanager
```
2. Create a virtual environment
```
(OSX)
python3 -m venv .env

(Linux)
virtualenv .env
```

3. Activate virtual environment
```
. .venv/bin/Activate
```

4. Install modules by running 'requirements.txt'
```
pip install -r requirements.txt
```

5. Setup for vue.js
```
npm install
```

## How To Start

1.  Run `npm run build`
2.  Run `python manage.py migrate`
3.  Run `python manage.py runserver`
4.  Open your browser using the url: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


<!-- ## Examples

<!-- * [Official site](https://www.kevinpeters.net/) -->

<!-- ## Resources -->

<!-- ### Motivation

Wanted to try out [nuxt.js](https://nuxtjs.org/) and created a new portfolio because the old one was really bad.

## License

_File manager_ is realeased under the MIT License.

## This readme is powered by vue-readme

Check out vue-readme [[Website](https://igeligel.github.io/vue-readme) | [GitHub](https://github.com/igeligel/vue-readme)] -->
