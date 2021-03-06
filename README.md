# justAbbyH Stories

###############################################################################
login details for code institute assessor - provided in project submission form
###############################################################################

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

6. As a new user, I want to be able to make a simple, secure payment to initiate a subscription, so that I can access author's stories.
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

* Navbar has 'AbbyH Stories' link to homepage with handwritten style font on all pages on left. The color depends on the underlying background color to provide sufficient contrast.
* To logged out users the navbar displays links for : Home, Stories, About, Login and Subscribe (subscribe link is a button). To authenticated users without extra permissions: Home, Stories, About and Logout. To authenticated staff and superusers: Home, Stories, Add Story, About and Logout. 
* On desktop all links display horizontally at top right of page. Color of links depends on the underlying background color to provide sufficient contrast. Links change color on hover.
* On tablet/mobile navbar displays clickable icon instead of links which triggers full page nav menu with off-white background color where respective links for each type of user are displayed vertically above social media icon links. If shown, subscribe link is shown as button above other links. A clickable dismiss button is shown in top right and 'AbbyH Stories' link remains at top left of page. 
* The navbar is shown on all pages except subscribe pages where it might distract from the payment/account activation process.
* For home, stories, login, add story and about pages: a subtle bottom border (color dependent on background color) is shown beneath corresponding nav link when respective page is active.


#### Footer

* Footer is shown on every page except subscribe pages where it might distract from the payment/account activation process.
* Background color of footer is light blue and always different from background color of element immediately above.
* Footer contains links to stories and about pages and social media icon links which change color on hover.
* For logged out users footer also displays a subscribe link as a button.

#### Messages

* Messages container element is part of everypage but is only shown if messages are sent from server after previous request.
* Messages appear as full screen width elements with text centered and a clickable times icon to hode the message.
* Messages hide automatically after a delay.

#### Buttons

* Larger size than other links, off white font color and light blue background with subtle border radius smoothing.
* Used to draw user's attention to key interactions on a page.
* Exhibit increased brightness on hover.

### Home page

![Homepage](https://i.ibb.co/3fLPkQy/reviews.png)

#### Main hero image with Read Now link

* Image is always 100% of viewport height and width.
* Different image (portrait/landscape) shown on mobile vs. tablet/desktop to achieve best image resolution for device dimensions. 
* Image has subtle zoom in effect for a short period when page is loaded. 
* A link to subscribe page (button) with text 'Read Now' is displayed near bottom of image.

#### Website introduction and stories link

* Section is always 90% of viewport height and 100% of width.
* Contains an short textual summary of the website's purpose
* A link to stories page (button) with text 'Stories' is displayed near bottom of section.

### About page

#### Headline creative summary section

* Section is always 90% of viewport height and 100% of width.
* Section has a light blue background color and white font color. Font size is large for visual impact.

#### Author photo and bio section with contact links

* On desktop author image and bio/contact links section are displayed size by side. On mobile/tablet author image is displayed above bio/contact links section. 
* Author image is always square and scales with device size. 
* Bio/contact links section contains short bio and social media and email links which open external tabs and change color on hover.

### Subscribe page

#### Instruction headline

* Section is always minimum of 33.3% of viewport height and 100% of width.
* Section has a light blue background color and white font color. Font size is large for visual impact.
* Text explains how to access stories and the benefit of subscribing.

#### Subscribe form

* Contains fields to create a new user account and subscription in database and a Stripe card element to process a clientside Stripe payment. 
* Fields all contain placeholders with grey font color which are replaced by darker text when not empty
* Country input is a select element which has a list of options provied by django-countries package.
* Card element from Stripe has a card icon which indicates the type of card based on the card number prefix.
* When a card number/expiration date/cvv number is entered but is incomplete or invalid a message with red font color is displayed beneath Card element input with error message and icon. When these inputs are valid a black info message displays a reminder of the amount of the payment to be made.
* Form contains a large submit button (with text 'subscribe') which is disabled on load and when the card element input is invalid and enables when input is valid. When clicked the subscribe page content is hidden by a full page overlay with a repeating ripple animation and 'your payment is processing' text.
* Submitting form first creates an inactive user and associated subscription in database via ajax request to server endpoint using form data; if this succeeds then an attempt to charge the user's card is made by the client; if this succeeds then the inactive user instance is activated by another ajax request to a different server endpoint; finally the page redirects to the 'subscription created' page. 
* If create inactive user fails the overlay hides and error message(s) are shown to the user on form.
* If create inactive user succeeds and payment fails a request is made to delete inactive user endpoint: if this request succeeds the overlay hides and payment error message from Stripe is shown on card element; if this request fails the page reloads and shows error message from server in messages element at top of page. Stripe will continue to send `paymentIntent.paymentFailed` webhooks to a webhook handler endpoint on server to confirm/retry deletion of the inactive user from database (this is primarily important to avoid username clashes)
* If create inactive user succeeds and payment succeeds on client then page is redirected to subscription created page with some subscription form input field key-value pairs appended as url query parameters. An email is sent to the email address provided in the relevant subscribe form input which contains a link (with encoded user id and activation token appended) to a server endpoint 'activate_user' which changes the user instance's `is_active` flag to `True` and redirects to login page if the link is valid or redirects to homepage with error message displayed in messages if link is invalid/expired/already used.

### Subscription created page

* Displays one section containing information that an email with an activation link has been sent to user's email.
* Link to email author (opens in new tab)

### Login page

* One section containing fields username and password and submit button.
* If submit is unsuccessful page reloads and displays form errors. 

### Stories page

* Contains one section which displays all stories in database. 
* Each story is displayed as a square image (image field of model served from AWS) with a translucent dark overlay and the story title field value text displayed over image in white (for maximum contrast) cursive font. The image shows a subtle box shadow on hover. Clicking on an image link takes user to the individual story details page for the respective story.
* Story image links are displayed as a single column on mobile, two columns on tablet and three columns on desktop device.

### Story details page

* Title of story is displayed at top of page with a subtle font shadow effect above square story image which scales with viewport size.
* Reading time and date published Story field values are displayed in small font beneath image.
* If user is logged out the text: "To access this story please subscribe" is displayed above a light blue horizontal rule divider. "Subscribe" is a link to subscribe page which has a light blue color and color darkens on hover. 
* If user is authenticated and does not have staff status a 'download story' link button is displayed above the divider instead. This link opens in a new tab and directs to a signed AWS S3 bucket url to access a private object in the bucket which is a pdf of the full story. This url is valid for 5 minutes. This pdf cannot be accessed by a non authenticated user.
* If user is authenticated and has staff/superuser status, an edit icon link to edit the story is displayed above the download story button. Edit link chnages from light blue to dark blue color on hover.
* Text from story's description field is displayed beneath the horizontal rule divider.

### Add story page

* Add story form contains fields to create a new Story instance in database.
* All fields (except pdf, image and featured) contain placeholders with grey font color which are replaced by darker text when not empty. pdf, image and featured fields display labels.
* Image and pdf fields contain Django file upload widgets to select a file from system file broswer.
* Submit button - if form is valid user is redirected to new story detials page of new story and an info message is displayed at top of page informing user that story was created. If form is not valid page is relaosed with form error messages displayed.

### Edit story page

* As above for 'Add Story Page` but input fields are prefilled with current field values from database as placeholders. All fields display labels for identification when they have current value as placeholder.
* Text at top of page: "You are editing: `story.title`".
* 'Save changes' button to submit form. 
* 'Delete story' link with red font color which darkens on hover to delete story endpoint. Link deletes story from database.

### 404 page

* displays navbar and footer
* displays 'home', 'stories', 'subscribe' (if user is anonymous) and 'about' links centered in a column in center of page - these nav links all exhibit color change on hover and direct to expected locations. 

## Features left to implement

* Reviews: subscribed users can create, edit and delete reviews for stories. Top reviewed stories displayed on homepage. Review details are displayed on story details page. Reviews Model with a many to one relationship to Stories Model.
* Stories page filters and sort functionality: UI elements on stories page to filter stories by genre, reading time or reviews. A sort select element with options to sort stories. Pagination of stories so list on any one page does not become too long. 
* Login form is displayed as centered modal on all pages instead of on separate page.
* Account page: allows user to edit account details and cancel subscription (functionality to remove user from list of registered users at end of current subscription period).
* Recurring payments subscription: instead of a onetime payment, user signs up for monthly subscription periods with recurring payments using Stripe.
* Section on homepage displaying latest social media posts of author: connect to twitter/instagram API to pull up to date posts. 
* '# list' as Story model field and displayed below image for each story on story details page and/or below title over image for each story link on stories page.
* Display similar stories on story detail page: list or carousel of other stories of same genre in database.
* Password reset function: link on login page to request an email to reset password sent to registered email address.
* Email newsletter: when user subscribes they are automatically (unless opt out) subscribed to emails that inform when new stories are posted. There is also a separate signup box to enter email address on homepage.
* Automated testing of Python functions and modules with unit tests within Django framework. Use of [Travis](https://www.travis-ci.com/) for continuous integration with deployed Heroku application.
* A selected full story downloadable for free by all users from homepage. 
* A blog page which displays the authors latest blog posts.
* Show preview of featured stories to unsubscribed users. These stories are displayed in a section on homepage and are labelled as 'featured' on list stories page.
* Improve the visual appearance of pop up boxes/messages.

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
| Title | `title` | `max_length=254`, `default=''` | `CharField` |
| Genre | `genre` | `choices=GENRE_CHOICES`, `max_length=254`, `default=''` | `CharField` |
| Publish Date | `publish_date` | `auto_now_add=True` | DateField |
| Description | `description` | `default=''`, `validators=[MaxLengthValidator(10000),MinLengthValidator(50),]` | `TextField` |
| Featured | `featured` | `default=False` | BooleanField |
| Reading Time (Minutes) | reading_time_mins | `null=True`, `validators=[MaxValueValidator(60000),MinValueValidator(1)]` | `PositiveIntegerField` |
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
| Country | `country` | `blank_label='Select country'` | `CountryField` |
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
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) package was used to improve appearance of all forms on site.
* [coolors.co](https://coolors.co/) was used to select color pallette for site.
* [Font Awesome](https://fontawesome.com/) was used for icons on site.
* [GitHub](https://github.com/) was used as remite repository for version control and automatic deployment to Heroku.
* [Git](https://git-scm.com/) was used for version control locally.
* [autopep8](https://pypi.org/project/autopep8/) code formatter tool used recursively on project directory with `--aggressive` flag to format all python files to pep8 standards.


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
* Free test account set up with [Stripe](https://stripe.com/). Webhook endpoint url configured in Stripe dashboard using local server domain: `https://<local_domain>/subscribe/webhooks/` and necessary environment variables set up for application as per documentation. 

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
* `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` from Stripe account.
* `STRIPE_WH_SECRET` from webhook endpoint information configured within Stripe account.
* `DEVELOPMENT` is set only within development environment and does not exist in production version - it controls whether `DEBUG` is set to `True` or `False` (`DEBUG` should ALWAYS be `False` in production otherwise sensitive information and server code can be exposed).
* `CURRENT_SITE_DOMAIN` should be the root domain of the local server you will be using.
4. Run the following command in the terminal to execute the existing app migrations and configure the database template (this should also create the local database file in the project root directory):
```
python3 manage.py migrate
```
5. Run the following command in the terminal to create a superuser account in the newly created local database:
 ```
python manage.py createsuperuser
```
6. Now, run the application locally with the following command in the terminal:
```
python3 manage.py runserver
```
7. Once the application is running in the browser, append `/admin` path to the local url provided and login using your superuser credentials. Create at least one instance of `Story` within the new database (this can also be done by logging in on the site and going to 'Add Story' in navbar).
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

* Text content on website, selection of colors, images and fonts; story data (descriptions, choice of images and actual pdf stories) by the author Abby Haysom. 

* Images used on homepage were used freely without attribution under the [Unsplash lisence](https://unsplash.com/license).

* Photo of Abby Haysom used on about page was taken my the website developer.

### Code

1. [download_story view](https://djangoadventures.com/how-to-create-file-download-links-in-django/)
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
15. [keep empty folder in vc commits](https://stackoverflow.com/questions/4250063/how-to-gitignore-all-files-folder-in-a-folder-but-not-the-folder-itself)
16. [update default django UserAdmin model](https://stackoverflow.com/questions/2552516/changing-user-modeladmin-for-django-admin)

### Acknowledgements

1. [Django login/out tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
2. [Stripe Integration tutorial](https://stripe.com/docs/payments/integration-builder)
3. [Simple is better than complex - blog tutorials on django](https://simpleisbetterthancomplex.com/)
4. [Django official docs](https://docs.djangoproject.com/)
5. [AnnaCI MS4 project README - for guidance on structure and content of README and TESTING files](https://github.com/AJGreaves/thehouseofmouse/README.md)

# Contact

Please contact me by email: `thaysom22@gmail.com`
