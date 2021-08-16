# justAbbyH Stories

[justAbbyH Stories](https://just-abby-h.herokuapp.com/) was designed and built by Thomas Haysom in order to promote and potentially generate financial support for the writing of his wife, Abby Haysom who is an amateur author and English teacher in Maryland, USA. The website is designed to offer a convenient and scalable platform conbined with an easy to use interface, for readers and followers of the author to find out more about her work and download and read her latest stories in full. This project also constitutes the final project for the developer on the Code Institute Full Stack Diploma. 

## Table of contents

1. [UX](#ux)
	* Goals
	* User Stories
	* Design Choices
	* Wireframes: [**Link to wireframes album**](https://ibb.co/album/bz6ZZy)
2. [Features](#features)
	* Exisiting features
	* Features left to implement
3. [Information Architecture](#information-architecture)
	* Data models
4. [Technologies Used](#technologies-used)
	* Tools and libraries
	* Languages
5. [Testing](#testing)
	* See separate [**TESTING.md**](./TESTING.md) file
6. [Deployment](#deployment)
	* Local
	* Heroku
7. [Credits](#credits)
	* Content and media
	* Code
	* Acknowledgements
8. [Contact](#contact)
<hr>

# UX

## Goals

### Visitor goals

The target audience:

* Friends, family, social media followers and colleagues of the author.
* Students of the author.
* Readers of short stories and fiction.
* Other authors.
* Publishers and literary agents.

User goals:

* To find and enjoy reading short stories.
* To find out more about the author.
* To support an author seeking to expand her readership.
* To find out price and access benefits to decide whether to subscribe.
* To make an easy, safe and secure one time subscription payment to access all content.
* To download content to read offline at own convenience.
* To create an account to easily access full story content by logging in.

The justAbbyH website meets these needs because:

* The website is designed to provide a simple interface and helpful feedback messages so the user can find relevant information and perform the desired actions.
* Navigation layout and styling is intuitive and fits with conventions on all device sizes.
* Samples of stories are displayed to all users so they can make an informed decision on whether to make a payment to access full value on site.
* Stories are hosted by AWS so they will always be quickly accessible to subscribed users anywhere in the world.
* The site uses Stripe with webhooks for secure payments to ensure payment is not taken or user data retained without the user having access to the content they have paid for.

### Site owner goals

The goals of the author:

* To create, update and delete stories to curate the site content.
* To view details of subscribed users to contact them or perform business analysis.
* To help build reputation and awareness in a wider online community of readers.
* To provide a platform for existing followers to access and enjoy story content.
* To incentivise visitors to pay a small amount to support time and commitment of writing.
* To connect to fans and other authors through linked social media channels to build subscriber base and connections.
* To provide an online presence to refer potential publishers and agents to.

## User Stories

New user:

1. As a new user, I want to be able to find out information about the author, so that I can decide whether I want to subscribe.
2. As a new user, I want to be able to see a selection of stories by the author, so that I can decide whether I want to subscribe.
3. As a new user, I want to be able to contact the author and to connect via social media, so that can deicde whether I want to subscribe. 
4. As a new user, I want to be informed about benefits subscribing and how to subscribe, so that I can decide whether I want to, and I know how to subscribe.
5. As a new user, I want to be able to view a preview of at least one story, so that I can decide whether I want to subscribe.
6. As a new user, I want to be able to make a simple, scure payment to initiate a subscription, so that I can access author's stories.
7. As a new user, I want to be shown feedback on the status of my payment and subscription, so that I am resassured I have been provided with what I have paid for and I know what further action to take if necessary.

Subscribed user:

8. As a subscribed user, I want to be able to browse all stories by the author, so that I can decide which stories I want to read.
9. As a subscribed user, I want to be able to view information about a particular story, so that I can decide whether I want to read the story.
10. As a subscribed user, I want to download a pdf of a full story, so that I can read the full story at my convenience.
11. As a subscribed user, I want to be able to login to the site after subscribing, so that I can access existing and newly published stories.

Site owner:

12. As the site owner, I want to be able to add stories to the site, so that I can publish new stories when I write them and increase the amount of content available to subscribers.
13. As the site owner, I want to be able to edit and delete stories, so that I can make necessary updates and curate the content available.

As any type of user:

14. As a user, I want to naviagate a site that is attractive, well structured and user friendly on all device sizes easily navigate the site and achieve my goals. 
15. As a user, I want to receive feedback messages from the site to inform me if my action was usccessful or an error has occurred, so that I am reassured my interactions are have the desired effect and what to do next if not.

## Design Choices

The site is designed to have a modern, warm, professional feel and to appeal to predominantly to young adult/adult users who are regular readers. The focus is the quality of the writing and therefore there are minimal distractions, bright colors or 'gimmicky' features which may detract from the serious, creative brand of the author. The design intends to evoke a literary/scholarly feel while remaining accesible and welcoming to all. 

### Websites of inspiration

* [The Cover Stories - Caro Claire Burke](https://www.caroclaireburke.com/) - website of young American author who has a social media presence alongside a website with a subscription based model. This author writes short story fiction and has a similar profile to Abby Deatherage. Website uses a small and sober color palette - black and white with a dull pink for call to action components and contrasting backgrounds.  

* [Maggie Shipstead](https://www.maggieshipstead.com/)

* [Celeste Ng](https://celesteng.com)

### Fonts

* Primary font used for headings, navigation and body is [Benne](https://fonts.google.com/specimen/Benne?category=Serif&preview.text=Abby%20Haysom&preview.text_type=custom&preview.size=42&width=4#standard-styles). This font was chosen for it's uncluttered visual simplicity and clean aesthetic. 

* Minor font used to provide a handwritten, stylized feel for certain elements across the site was [Over the Rainbow](https://fonts.google.com/specimen/Over+the+Rainbow?category=Handwriting&preview.text=Abby%20Haysom&preview.text_type=custom&preview.size=42). For example, this is used in the logo in the main navbar on all pages.


### Colors

<a href="https://ibb.co/hfSjd4M"><img src="https://i.ibb.co/nCFv1Y0/just-Abby-H-website-colorscheme.png" alt="just-Abby-H-website-colorscheme" border="0"></a>

* The two main colors are a very dark blue and a slight off white. These contrast strongly and are used and are used as predominent respective foreground/background colors across the site. 

* An Opal color is used as an alternative background color and font color in places across the site for the purposes of variety and calling user attention. It is also as the color for button elements. It contrasts well with both the dark blue and off white colors. 

* This color scheme provides a clean, uncluttered and professional feel while conveying some warmth via the muted Opal blue. The overall tone is subtle and balanced so the user's attention is focussed on the content and the viewing experience is comfortable. 

### Styling, effects and icons

* Lots of space around centered elements and text is used on all pages of the site so the user can enjoy an uncluttered and comfortable browsing experience on all device sizes.
* Individual stories on the list stories page are presented with their images in familiar, clean, boxed elements on the page with a subtle and comfortable hover fade effect. Buttons and links also exhibit the same hover fade effect for consistency of interaction across all elements of the site. 
* Favicon icon
* Social media icons (Instagram)
* Menu icon
* Close (times) icon
* Confirmation icon
* Edit icon



## Wireframes

**Notes**
* Wireframes were completed on paper, by hand instead of using a wireframing tool for this project. This was the advice of my mentor to help visualize and plan more clearly how the layout of pages will appear on different screen sizes and ratios. 
* Bootstrap's 12 column grid system was used to plan the layout and spacing of elements in wireframes. 
* iPhone 12 screen dimensions were used for 'mobile' wireframe templates (146x73mm approx).
* Ipad (2020) screen dimensions were used for tablet wireframe templates (173x250mm approx).
* 275mm (full width of available paper) was used for desktop wireframe width.
* If layout and design does not change significantly on a larger version wireframe, the larger screen version wireframe is shown on the smaller version template. 

[**Link to wireframes album**](https://ibb.co/album/bz6ZZy)
 
# Features

## Existing features

### Features on every page

#### Navbar

#### Footer

#### Messages

### Home

### About

### Subscribe 

### Login 

### Subscription created 

### Stories 

### Story details 

### Add story 

### Edit story

## Features left to implement

* Featured/sample stories: section on homepage displaying latest/featured stories.
* Reviews: subscribed users can create, edit and delete reviews for stories. Top reviewed stories displayed on homepage. Review details are displayed on story details page. Reviews Model with a many to one relationship to Stories Model.
* Stories page filters and sort functionality: UI elements on stories page to filter stories by genre, reading time or reviews. A sort select element with options to sort stories. Pagination of stories so list on any one page does not become too long. 
* Login is centered modal on all pages instead of separate page.
* Account page: allows user to edit account details and cancel subscription (functionality to remove user from list of registered users at end of current subscription period).
* Recurring payments subscription: instead of a onetime payment, user signs up for monthly subscription periods with recurring payments using Stripe.
* Footer: author contact and social media info and information about site developer with links to developer online presence
* Section on homepage displaying latest social media posts of author: connect to twitter/instagram API to pull up to date posts. 
* Display similar stories on story detail page: list or carousel of other stories of same genre in database.
* Password reset function: link on login page to request an email to reset password sent to registered email address.
* Email newsletter: when user subscribes they are automatically (unless opt out) subscribed to emails that inform when new stories are posted. There is also a separate signup box to enter email address on homepage.
* Automated testing of Python functions and modules with unit tests within Django framework. Use of [Travis](https://www.travis-ci.com/) for continuous integration with deployed Heroku application.
* A selected full story downloadable for free by all users from homepage. 
* A blog page which displays the authors latest blog posts.

# Information Architecture

### Databases used

* SQL category databases were used since Django's ORM framework is designed to work them. 
* [sqlite3](https://www.sqlite.org/index.html) was used as the database for the application during local development since it is lightweight and configured by default in Django's initial settings. 
* [PostgreSQL](https://www.postgresql.org/) was used as the database for the application when deployed on Heroku. It was set up as a Heroku add-on to the application using the Heroku GUI. 

### Data Models

#### User model

The User model employed in this project is the `models.User` model built into django and is provided by `django.contrib.auth`.
See the official Django [docs](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/) for more details on this model.

#### Story model

The Story model is within the stories app and holds all required data about a story, including image and file fields.

| Name | Key in DB | Options | Field Type
| --- | --- | --- | --- |
| Title | `title` | `max_length=254` | `CharField` |
| Genre | `genre` | `choices=GENRE_CHOICES`, `max_length=254`, `default=''` | `CharField` |
| Publish Date | `publish_date` | `auto_now_add=True` | DateField |
| Description | `description` | `default=''` | `TextField` |
| Featured | `featured` | `default=False` | BooleanField |
| Reading Time (Minutes) | reading_time_mins | `null=True` | `PositiveIntegerField` |
| Reading Time String | `reading_time_string` | `max_length=254`, `default=''` | `CharField` |
| Image | `image` | `upload_to='story_images/'`, `storage=PublicFileStorage()` | `ImageField` |
| Image Credit | `image_credit` | `max_length=254`, `blank=True`, `default=''` | `CharField` |
| Pdf file | `pdf` | `upload_to='story_pdfs/'`, `storage=PrivateFileStorage()` | `FileField` |


* Genre choices are defined within the Story model.
* The Story Model uses the Pillow library to store image files in an AWS S3 bucket in production.
* Custom storage classes `PublicFileStorage` and `PrivateFileStorage` (derived from `S3Boto3Storage`) used for `image` and `pdf` fields in production are defined in `custom_storages` module.

#### Subscription model

The Subscription model is within the subscription app and holds all the required data about a subscription, including the relationship to the user model to which it belongs. 

| Name | Key in DB | Options | Field Type
| --- | --- | --- | --- |
| User | `user` | `on_delete=models.CASCADE` | `OneToOneField` to `User` |
| Start Date | `start_date` | `auto_now_add=True` | `DateField` |
| Country | `country` | `blank_label='Country'` | `CountryField` |
| City | `city` | `max_length=100`, `default=''` | `CharField` |
| Stripe Payment ID | `stripe_pid` | `max_length=254`, `unique=True`, `default=''` | `CharField` |


* `CountryField` class imported from `django_countries.fields`
* `Subscription` model instance cannot exist without unique `User` foreign key (but `User` instance can exist without corresponding `Subscription` instance - e.g staff users).


# Technologies Used

### Tools and libraries

* [Gitpod](https://gitpod.io/): IDE used for development.
* [Heroku](https://www.heroku.com/): cloud platform used to deploy application.
* [Django](https://www.djangoproject.com/): web framework used.
* [Stripe](https://stripe.com): process secure payments and trigger actions via webhooks.
* [AWS S3](https://aws.amazon.com/): serve static files including images and store user uploaded images and pdfs
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): AWS SDK for python to interact with AWS S3 buckets from application code.
* [django-storages](https://django-storages.readthedocs.io/en/latest/): custom storage backend for Django to use with AWS S3 buckets. 
* [Gunicorn](https://pypi.org/project/gunicorn/): WSGI HTTP Server used by Heroku.
* [Pillow](https://pillow.readthedocs.io/en/stable/): imaging library for processing image files to store in database.
* [Psycopg2](https://pypi.org/project/psycopg2/): Python adaptor for PostgreSQL database.
* [PIP](https://pip.pypa.io/en/stable/installing/): installation of packages.
* [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03): version control.
* [GitHub](https://github.com/): remote repository for application code.
* [Google Sheets](https://www.google.co.uk/sheets/about/): for planning project and organizing project information.
* [django-environ](https://django-environ.readthedocs.io/en/latest/): configure environment variables for Django application.
* [django-countries](https://pypi.org/project/django-countries/): provide country choices for forms and `CountryField` for models.
* [dj-database-url](https://pypi.org/project/dj-database-url/): use simple `DATABASE_URL` string to configure Django application.
* [JQuery](https://jquery.com): to simplify DOM manipulation and XHR requests.
* [Bootstrap](https://www.bootstrapcdn.com/): to build a responsive UI efficiently.
* [Google Fonts](https://fonts.google.com/): to provide and serve fonts used on site pages.
* [Imgbb](https://imgbb.com) used to store and serve images related to documentation that were not uploaded by users and not entered into the database.

### Languages

* Python (with built in libraries) was used as the language for all backend logic for the application.
* HTML, CSS and Javascript were used to provide the user interface layout, styles and client side logic for the application. 

# Testing

See separate [**TESTING.md**](./TESTING.md) file.

# Deployment

### Deploy and run project locally

**Prerequisites**

* Code editor such as [Gitpod](https://gitpod.io/) or [Visual Studio Code](https://code.visualstudio.com/) which offers ability to run a local server.
* A browser to execute the front end code. [Google Chrome](https://www.google.com/intl/en_uk/chrome/) is recommended. 
* [Python3](https://www.python.org/), [Pip](https://pypi.org/project/pip/) and [Git](https://git-scm.com/) installed on computer. 
* Free test account set up with [Stripe](https://stripe.com/). Webhook endpoint url configured in Stripe dashboard using local server domain: `https://<local_domain>/subscribe/webhooks/` and necessary environment variables set up and retrieved in application as per documentation. 

1. Run the following command in a clean workspace terminal to download the project code:
```
git clone https://github.com/thaysom22/justAbbyH.git
```
2. Install all required modules by running the command in the terminal:
```
pip install -r requirements.txt
```
3. The project dependencies include `django-environ` so create a file in the project root directory `.env` and include the following environment variables:
```
DEVELOPMENT=true
SECRET_KEY=<key>
STRIPE_PUBLIC_KEY=<key>
STRIPE_SECRET_KEY=<key>
STRIPE_WH_SECRET=<key>
CURRENT_SITE_DOMAIN=<domain>
```
*  `SECRET_KEY` is required by Django framework for certain functionalities. 
* `DEVELOPMENT` is set only within development environment and does not exist in production version - it controls whether `DEBUG` is set to `True` or `False` (`DEBUG` should ALWAYS be `False` in production otherwise sensitive information and server code can be exposed).
* `CURRENT_SITE_DOMAIN` should be the root domain of the local server you will be using.
4. Run the following command in the terminal to execute the existing app migrations and configure the database template (this should also create the local database file in the project root directory):
```
python3 manage.py migrate
```
5. Run the following command in the terminal to create a superuser account to access the admin panel and manipulate the database:
 ```
python manage.py createsuperuser
```
6. Now, run the application locally with the following command in the terminal:
```
python3 manage.py runserver
```
7. Once the application is running in the browser, append `/admin` path to the local url provided and login using your superuser credentials. Create at least one instance of `Story` within the new database.
8. Remove the `/admin` path from the url to return to main page in browser and the application will function as expected.

### Deploy project to Heroku

This is the process followed by the developer to deploy the application to [Heroku](https://www.heroku.com/).
Note: other cloud hosting providers (PaaS) such as [AWS Elastic Container 2](https://aws.amazon.com/ec2/) can be used for deployment but the process described below is specific to to Heroku.

**Prerequisites**

In addition to prerequisites outlined above for local deployment:
* Accounts set up with the following services:
	* [AWS S3](https://aws.amazon.com/):
		* Create and name two s3 buckets. 
		* Configure one bucket to allow public access to it's objects and host and serve static files. Create folders `media/public/` and `static/` at top level in bucket. Configure permissions to allow all s3 actions publically.
		* Create IAM user and attach policy with permssions to perform all s3 actions on objects within both private and public s3 buckets.
		* Configure other bucket to block all public access to it's objects. Create folder `media/private/` at top level in bucket. Configure permissions to allow IAM user to perform all s3 actions on objects in bucket.
	* [Stripe](https://stripe.com/):
		* Webhook endpoint url configured in Stripe dashboard using **production** server domain: `https://<production_domain>/subscribe/webhooks/` and necessary environment variables set up and retrieved in application as per documentation. 
	* [Gmail](https://mail.google.com/): create account and follow steps in help centre to configure security settings and obtain necessary environment variables to use gmail account as smtp server.
	* [GitHub](https://github.com/): create account to store code remotely.

How to configure and set up/retrieve all the necessary environment variables for these services is detailed in the respective documentation.

1. With codebase running in IDE, run the following command in the terminal to create/update `requirements.txt` file:
```
pip freeze > requirements.txt
```
2. Create `Procfile` in project root directory containing the following command:
```
web: gunicorn justAbbyH.wsgi:application
```
3. Run `git add` and then `git commit` in the terminal to save these changes followed by `git push` to send the codebase to GitHub. 
4. Create a new app on [Heroku dashboard](https://dashboard.heroku.com/apps). Set name of app and appropriate region for your location.
5. From Heroku dashboard, connect app to Github repository and change deployment method to deploy from appropriate Github branch.
6. From Heroku dashboard resources section, provision 'Heroku Postgres' addon (hobby dev version). 
7. From Heroku dashboard, go to settings > Reveal Config Vars. Add the following config key-value pairs to set up the environment variables for the app in production:

| Key | Value |
| --- | --- |
| USE_AWS | true |
| USE_SMTP | true |
| SECRET_KEY | < django secret key > |
| STRIPE_PUBLIC_KEY | < stripe public key > |
| STRIPE_SECRET_KEY | < stripe secret key > |
| STRIPE_WH_SECRET | < stripe webhook signing key > |
| PRODUCTION_HOST | < domain of heroku application > |
| AWS_ACCESS_KEY_ID | < id of access key for AWS IAM user > |
| AWS_SECRET_ACCESS_KEY | < secret key for AWS IAM user > |
| DATABASE_URL | < postgres database url > |
| EMAIL_HOST_USER | < gmail account email > |
| EMAIL_HOST_PASSWORD | < gmail account password > |
| AWS_STORAGE_PUBLIC_BUCKET_NAME | < AWS s3 public bucket name > |
| AWS_STORAGE_PRIVATE_BUCKET_NAME | < AWS s3 private bucket name > |
8. From IDE terminal:
    * Enter the heroku postres shell 
    * Migrate the database models 
    * Create superuser account for new postgres database
    
     Instructions for these steps can be found [here](https://devcenter.heroku.com/articles/heroku-postgresql).
 9. From the Heroku dashboard, deploy the application and wait for the build process to complete (any problems can be identified by viewing the logs section).
 10. Open the running app in the browser and append `/admin` path to the local url provided and login using your superuser credentials. Create at least one instance of `Story` within the new database.
11. Remove the `/admin` path from the url to return to main page in browser and the application will function as expected.


# Credits

### Content and media

* Text content on website; selection of colors, images and fonts; story data (descriptions, choice of images and actual pdf creative content) by Abby Haysom. 

### Code

1.  [download_story view](https://djangoadventures.com/how-to-create-file-download-links-in-django/)
2. [Stripe UI](https://stripe.com/docs/payments/integration-builder)
3. [S3Boto3Storage source code](https://github.com/jschneier/django-storages/blob/master/storages/backends/s3boto3.py#L194)
4. [separate s3 public and private storages](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)
5. [generating presigned urls with boto3 AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html)
6. [jquery ajax api docs](https://api.jquery.com/jquery.ajax/)
7. [encodeURI to send query parameters in GET request to server](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
8. [urllib.parse.unquote to decode url query parameters in python view](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote)
9. [send activation email](https://studygyaan.com/django/how-to-signup-user-and-send-confirmation-email-in-django)
10. [customize story admin display to present signed url for fileField](https://realpython.com/customize-django-admin-python/)
11. [make div square with pure css using ::after element](https://spin.atomicobject.com/2015/07/14/css-responsive-square/)
12. [spinner animation css after subscribe form submit](https://loading.io/css/)
13. [hide * appended to form labels for required fields by django-crispy-forms](https://stackoverflow.com/questions/61058107/remove-char-from-the-required-field-label-in-form)
14. [story title heavy text shadow effect css](https://www.massmediums.com/blog/134-create-great-looking-pure-css-text-shadows.html)
### Acknowledgements

1. [Django login/out tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
2. [Stripe Integration tutorial](https://stripe.com/docs/payments/integration-builder)
3. [Simple is better than complex - blog tutorials on django](https://simpleisbetterthancomplex.com/)
4. [Django official docs](https://docs.djangoproject.com/)
5. [AnnaCI MS4 project README - for guidance on structure and content of README and TESTING files](https://github.com/AJGreaves/thehouseofmouse/README.md)

# Contact

Please contact me by email: `thaysom22@gmail.com`
