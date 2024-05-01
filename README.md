# **Connect API**

## Table of Contents

- [Objective](objective)
- [Links to deployed Project](#links-to-deployed-project)
- [Features](#features)
    * [Models](#models)
- [Design](#design)
    * [Aim](#aim)
    * [Scope](scope)
    * [Structure](structure)
- [Agile Methodology](#agile-methodology)
- [Languages](#languages)
- [Frameworks and Libraries](#frameworks-and-libraries)
- [Tools and Technologies](#tools-and-technologies)
- [Testing and Validation](#testing-and-validation)
- [Bugs and Fixes](#bugs-and-fixes)
- [Connecting to the API](#connecting-to-the-api)
- [Deployment](#deployment)
- [Cloning this repository](#cloning-this-repository)
- [Forking a branch](#forking-a-branch)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Objective

The objective of the Connect API is to provide a backend database to create event information in my area. The database allows the functionality to create, view, edit and delete event information in the local area. A user who is going to be hosting an event can upload the event detials, which will include an image for the event, a description of the event including the date and time and an event category. Users can  follow the event hosts and they will be able to select if they are interested in the event or if they are going to attend the event. A user can comment on an event and leave a review once the event has past.

## Links to deployed Project

[Connect API Live link]()

[Connect App Live Link]()

## Features

### Models

#### Profile

owner - OnetoOneField
created_at - DateTimeField
updated_at - DateTimeField
name - CharField
bio - TextField
phone_number - IntegerField(optional)
email - EmailField(optional)
profile_picture - ImageField

## Design

### Aim

### Scope

### Structure

## Agile Methodology

## Languages

## Frameworks and Libraries

[Django 3.2](https://www.djangoproject.com/) high-level Python web framework used to develop this application.

[Django Rest Framework 3.14](https://www.django-rest-framework.org/) - A powerful a flexible toolkit for building Web APIs.

[Cloudinary 1.4 and Cloudinary storage 0.3](https://cloudinary.com/) - Allowing connection with Cloudinary.

[Pillow 8.2](https://pypi.org/project/pillow/8.2.0/) - A Python imaging library that includes image processing capabilities.

## Tools and Technologies

## Testing and Validation

## Bugs and Fixes

| Bug | Fix|
| --- | ---|
| After creating the profiles model, I tried to access the 'Profiles' section in the admin panel, but I was receiving an error: CLOUDINARY_STORAGE dictionary with CLOUD_NAME, API_SECRET and API_KEY in the settings or set CLOUDINARY_URL variable (or CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET variables). I checked mulitple times the cloudinary variable were setup correctly in env.py and settings.py. | I had stored the env.py file in the 'connect_api directory. Once I moved the file to the project root then I could access the profile section in the admin panel as expected. |

## Connecting to the API

## Deployment

## Cloning this repository

## Forking a branch

## Credits

## Acknowledgements
