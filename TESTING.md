# justAbbyH Stories - TESTING

[README](./README.md)

[View website on Heroku](https://just-abby-h.herokuapp.com/)

## Table of Contents

1. [Automated testing](#automated-testing)
	* Validation services
	* Note on testing for this project
2. [User stories testing](#user-stories-testing)
3. [Manual testing](#manual-testing)
4. [Bugs discovered](#bugs-discovered)
	* Solved bugs
	* Unsolved bugs
5. [Other testing](#other-testing)

## Automated testing

#### Validation Services

* [W3C Markup Validation]() for HTML.
* [W3C CSS Validation]() for CSS.
* [JSHint]() for JavaScript.

#### Note on testing for this project

With more time and experience I would like to write Python unit tests for the code in Django apps for this project aiming for highest coverage as possible. I would also have liked to include Jasmine unit tests for the significantly complex Javascript functions in Stripe.js file.

In the interests of time and to focus my efforts on the areas that the project assessment criteria reward, I decided that unit testing was not a priority for this project submission but should certainly be added in future. Ideally, I would have followed a Test Driven Development (TDD) approach of writing failing tests befoe implementing respective functions: however time did not allow for this project. This is a process I will seek to follow in my future Django devlopement work. 

## User stories testing

This section goes through all user stories from the [README](./README.md) file and confirms they are satisfied.

New user:

1. As a new user, I want to be able to find out information about the author, so that I can decide whether I want to subscribe.

* The about page is linked from the navigation menu and the footer from the homepage and every page except subscribe pages. 
* The about page displays a picture and short biography. 
* The navigation menu also displays social media links.

2. As a new user, I want to be able to see a selection of stories by the author, so that I can decide whether I want to subscribe.

* The stories page is linked from the navigation menu and the footer from the homepage and every page except subscribe pages. 
* The stories page is also linked from a main section of the homepage via a prominent button.
* The stories page displays all stories in database as image links with titles. The user can scroll through this list and click on any image to open up a details page for the selected story which displays reading time, publish date and a description.

3. As a new user, I want to be able to contact the author and to connect via social media, so that can decide whether I want to subscribe. 

* The footer is displayed on the homepage and all pages except subscribe pages and contains social media links. 
* The expanded navbar on mobile/tablet also dislays social media links.
* The about page displays social media and an email link.

4. As a new user, I want to be informed about benefits subscribing and how to subscribe, so that I can decide whether I want to, and I know how to subscribe.

* Subscribe links are displayed prominently to unsubscribed users in the navigation, footer and in a main section of the homepage. 
* When an unsubscribed user clicks on an individual story link they are shown a link to subscribe to get access. 
* The subscribe page dipslays information about payment amount and benefits clearly at top of page.

5. As a new user, I want to be able to make a simple, secure payment to initiate a subscription, so that I can access author's stories

* The subscribe page contains a single form with a prominent button to subscribe
* The user is then shown a subscription successful page with information instructing them to access email and follow an activation link to login.

6. As a new user, I want to be shown feedback on the status of my payment and subscription, so that I am resassured I have been provided with what I have paid for and I know what further action to take if necessary.

* The subscribe form button is disabled until valid payment information is entered. The user is shown realtime feedback before form submit if there are errors with payment information. When the payment information is valid, the user is shown the charge amount and the button is enabled. 
* When valid subscribe form is submitted, the user is shown an overlay with a repeating animation and is informed that their payment is being processed. If the process is successful the user is shown a subscription successful page and given instructions for how to activate their account via email link.
* If there is an error from Stripe  with authorizing user's payment on the client the overlay is removed and the user is shown the specific error message from Stripe beneath payment input. 
* If there is an invalid input or server error when creating the inactive user and associated subscription in database or when deleting the previously created inactive user (if payment client has failed) then the subscribe page is reloaded with an appropriate error messages displayed.
* If required fields are left blank the standard browser tool tips are displayed and the subscribe form will not submit.

Subscribed user:

7. As a subscribed user, I want to be able to browse all stories by the author, so that I can decide which stories I want to read.

* As above (2).
* Subscribed user is shown download story link when they click on a specific story link

8. As a subscribed user, I want to be able to view information about a particular story, so that I can decide whether I want to read the story.

* Links to all stories are displayed on stories page and when subscribed user clicks on any story they are shown a page for that particular story with reading time, publish date, download story link and description of story.

9. As a subscribed user, I want to download a pdf of a full story, so that I can read the full story at my convenience.

* Each individual story details page has a download link to a pdf document hosted on AWS for the story. This can be downloaded by the user for later use. 
* The link expires after 5 mins so it cannot be shared but the user can click the download story link again to generate a fresh link if they wish to access the story again.

10. As a subscribed user, I want to be able to login to the site after subscribing, so that I can access existing and newly published stories.

* The navigation bar displayed on the homepage and all other pages except subscribe pages has a link to login page where subscribed user can input credentials. 
* Logged in users are shown 'download story' link on individual story pages 

Site owner:

11. As the site owner, I want to be able to add stories to the site, so that I can publish new stories when I write them and increase the amount of content available to subscribers.

* logged in staff status users are shown a link to add story in navigation bar
* add story page has a form where fields for story can be inputted and a submit button to save story to database so it will appear on stories list page.

12. As the site owner, I want to be able to edit and delete stories, so that I can make necessary updates and curate the content available.

* logged in staff status users are shown an edit icon on each individual story detail page linking to edit story page
* edit story page displays a form which is prefilled with current field values from database which the user can update
* form has a submit button to save story changes to database so they will take effect on stories list and details pages
* edit story page has a delete story link to endpoint on server that removes story from database (first triggers a broswer confirm dialoge box)

As any type of user:

13. As a user, I want to naviagate a site that is attractive, well structured and user friendly on all device sizes easily navigate the site and achieve my goals. 

* navigation is laid out clearly and consistently in an familiar way on all device sizes
* color scheme and fonts are consistent across site
* plenty of padding and margins create a comfortable and visually appealing user experience
* where appropriate: layout, spacing, sizing of text and elements on page adjusts for device size
* interactive elements exhibit unobtrusive, familiar and helpful effects

14. As a user, I want to receive feedback messages from the site to inform me if my action was unsuccessful or an error has occurred, so that I am reassured my interactions are have the desired effect and what to do next if not.

* server sends messages to be displayed at top of page whenever an error occurs or a user needs feedback or information about a previous action.
* messages are displayed prominently but unobtrusively at top of page
* messages can be hidden by clicking a dismiss icon or they time out.

## Manual testing

Manual testing of all elements and functionality of site was carried out in Chrome and Safari browsers using mobile, tablet and desktop emulators in dev tools on a chromebook and also on an iPhone.

### Elements on every page

#### Navbar

* on all pages (except subscribe pages) of site navbar is expanded and nav links display horizontally at top right of page on desktop device and collapse to three dot menu icon on mobile and tablet devices.
* nav links display change of color on hover on all pages. 
* link corresponding to active page has underline effect on appropriate links
* correct set of nav links display when user in session is anonymous/authenticated/staff
* 'AbbyH Stories' text link displays at top left of all pages
* all links in navbar work as expected and navigate to expected urls successfully.
* on mobile/tablet devices clicking on menu icon triggers full page expanded menu and is replaced by a different dismiss icon. clicking this icon closes the full page menu as expected.
* 'AbbyH Stories' text link is hidden when expanded navigation menu is shown
* Expanded full page nav menu on mobile/tablet shows same links as shown in top right on desktop for anonymous/authenticated/staff users
* Links in expanded nav menu show hover and active underline effects on all pages
* If shown, subscribe button is shown above all other links arranged in a column in centre of page
* Instagram and Twitter social media link icons are shown beneath internal nav links and exhibit change of color on hover. Links open in new tab and direct to expected location on all pages.
* Expanded nav menu is full height of viewport on all mobile/tablet devices and does not scroll.
* Font color of links in navigation has sufficient contrast with background on all pages at all times 

#### Footer

* Displays subscribe button link only to anonymous users
* Displays story, about and Twitter/Instagram nav links on all pages and device sizes centred horizontally. These links all direct to expected locations and social media links open in new tab.
* Footer is contasting color to section about and 33.3% of device height

#### Messages

* Messages display beneath navbar at top of page when an error or invalid action occurs
* Messages disappear automatically after a delay
* Each message has a clickable dismiss icon that when clicked causes the message to hide.

#### Buttons

* Redirect to correct locations when clicked
* Exhibit an increased brightness when hovered 

### Homepage

* is accessible to all anonymous, authenticated and superusers.

#### Main hero image with Read Now link

* main hero image section displays appropriate landscape/portrait image on larger/smaller device sizes respectively
* main hero image section exhibits 3 second zoom animation on page load on all devices
* main hero image background is 100% of viewport height and width on all device sizes
* 'read now' button link displays near bottom of image (and is visible on page load on all devices) and redirects correctly to subscribe page for anonymous users and to stories page instead for authenticated users.

#### Website introduction and stories link

* section is 90% of viewport height on all devices
* text scales with device size and does not overflow
* 'stories' button link displays near bottom of section and redirects correctly to stories page

### About page

* is accessible to all anonymous, authenticated and superusers.

#### Headline creative summary section

* Section displays with light-blue background color at 90% viewport height for all device sizes.
* header fonts have sufficient contrast on background color of this section
* Font does not overflow and scales with device size

#### Author photo and bio section with contact links

* Author image displays clearly above short bio/contact links on mobile/tablet and adjacent to short bio/contact links on desktop. Image scales to maintain close to original proportions on all device sizes. 
* Short bio text is legible, does not overflow and size scales with device width.
* Contact links display below short bio, are sufficiently spaced and padded and exhibit change in color from dark blue to light blue on hover on desktop. Clicking on each socail media link icon opens up appropriate external link in a new tab. Clicking on email link icon opens up template email in new tab.


### Subscribe page

* is accessible to all anonymous users. is not accessible to authenticated and superusers - these users are redirected to homepage with a message shown in messages section.

#### Instruction headline

* Displays clearly at 33.3% viewport height on all device sizes and font size scales with device size
* Section has light blue background and header fonts have sufficient contrast on this background 


#### Subscribe form

* On page load each input field displays at a comfortable width on every device size and does not exceed a max width on desktop. Each field displays a label above the input area and no text or placeholder in the input area.
* Username and password fields display help text below input area.
* Country select element displays 'select country' placeholder with gray color, when clicked a dropdown list of country options displays (select country original value is disabled) and when an option is clicked the dropdown list hides and the selected value appears in the input area in darker color font matching other inputs' text color.
* Stripe card element displays with gray color placeholders for: card number, expiry date, CVC and postcode; and card icon on left.
* Submit button displays at bottom of form and is disabled and faded on page load.
* The submit button does not enable unless user inputs valid card number and expiration date in the future. If the user leaves card number or expiration date incomplete or invalid or cvv/postcode incomplete the submit button remains disabled and an appropriate error message displays below card element. If the card information is valid and complete the submit button enables and and info message containing the amount to be charged displays beneath the card element. If any of the card inputs again become invalid/incomplete the submit button re-disables, info message hides and error message displays.
* When required (non card) input fields are left empty or do not satisfy default browser validation the form will not submit and show default browser help messages.
* If all the form inputs are valid from browser's perspective, the page sends a request to 'create-inactive-user' endpoint on server: if form data fails server validation from this endpoint a 400 response is received and error messages are displayed below invalid fields as well as an error message indicating there are form errors beneath the submit button at the bottom of the form.
* If form data passes server validation a 200 response from 'create-inactive-user' endpoint is received and a full screen overlay is shown with a pulsing ripple icon and 'payment processing' message. While this is displaying a call to the Stripe API is made from the client to confirm the payment information entered. 
* If this is successful (the payment input authorizes) then the user is redirected to the 'subscription created' page and an INACTIVE user with the information from the subscribe form is in the database and related subscription (the session user remains anonymous). A payment_intent.succeeded webhook is sent by stripe and received a success reponse indicating the user was sent an activation email.
* If this payment is declined by the Stripe API then overlay hides and subscribe form is shown again with card error message shown just above submit button and scrolled into view.
* if card requires extra authorization, the modal from stripe appears on top of payment processing overlay - if this extra authentication fails user is returned to subscribe form with 'card authorization failed' error message displayed and scrolled into view. if extra authorization passes then user is redirected to 'subscription created page' and inactive user is added to database as described above.
* if card payment fails for any reason there is no respective inactive user remaining in the database at the end of process (call to 'delete-inactive-user' endpoint is made with successful response)


### Subscription created page

* accessible to all users 

#### page content

* data in url query parameters passed in url redirected to from subscribe page is displayed correctly in message on page.
* contact link is displayed in text and exhibits change in color on hover. clicking on link opens new tab to templte email with expected content

#### account activation link function

* when subscription form is validated and payment is successful then user is redirected to 'subscription created' page and an email is sent to the email address provided in the subscribe form. This email contains the expected template text; an activation link url with an encoded user id and token; a link to the homepage and the username. Stripe dashboard logs show a payment_intent.succeeded webhook was sent and received a successful response indicating webhook handler has sent activation email to user's email.
* clicking the activation link after accessing the email in the respective email account directs user to login page and a message is shown in messages section at top of page informing that the account was activated successfully. The respective user now has `is_active` flag set to `True` in the database. Entering the username and password provided in the subscribe form results in successful login.
* Trying to access the same activation link more than once results in the server redirecting to the homepage and a message informing the user that the link is invalid/expired/already used. This also happens if the activation link is invalid (i.e if a user tries to access the server endpoint manually without correct token code)


### Login page

* is only accessible to anonymous users. authenticated users are redirected to 'stories' page
* username and password field inputs display with labels and without placeholders
* sumbit button with text 'log in' displays below inputs
* attempting to submit form with one or both fields empty results will not submit and browser default help messages are shown
* If both inputs contain data, the form submits. If one or both fields are determined invalid on the server, page reloads and an error message is displayed for the form (not indicating with field(s) are incorrect for security reasons)


### Stories page

* accessible to all users
* story image links are displayed in appropriate layout on mobile/tablet/desktop device sizes
* links exhibit box shadow effect on hover
* all stories in database are displayed
* clicking on each link directs to the expected 'details' page for that story
* title fonts are readable over the image
* image is slighly darkened by transluscent overlay to improve contrast 


### Story details page

* page is asscessible to all users
* download story link is only shown to authenticated users. clicking this link opens a url pointing to the pdf document of the full story in a private AWS S3 bucket. the url is signed to restrict access and times out after 5 mins (if the same url is visited after 5 mins have elapsed the request is denied access). if the address of the object is requested without an appended signature then access is denied. therefore, there is no way for a non staff user to access the pdf object in the S3 bucket without accessing the download_story endpoint which is accessible only to authenicated users (anonymous users are redirected to login page)
* edit story link icon is only shown to staff/super users
* anonymous users are shown  the text "To access this story please subscribe" with link to subscribe page in place of download story button. This link directs to subscribe page.
* title is shown with text shadow effect, square image is shown, correct values for reading time and publish date fields description text are shown for each story in database.
* content is centered horizontally and has maximum width on wider device screens

### Add story page

* page only accessible to staff/super users - anonymous users are redirected to login page
* form field inputs all display clearly with labels and no placeholders
* If required field is left blank or fails browser validation then browser shows default help message on field input
* When form is submitted by clikcing submit button, button disables and text changes from 'save' to 'processing'.
* If form data fails server validation, appropriate error messages are displayed adjacent to form fields in red and an error message is displayed beneath submit button, button is reenabled
* if form submits successfully, story instance with correct field values is added to database and story image and pdf objects are added to public and private s3 buckets respectively. user is redirected to respective story_details page with a message that the story has been added successfully.
* 

### Edit story page

* page only accessible to staff/super users - anonymous users are redirected to login page

### Delete story functionality

* url only accessible to staff/super users - anonymous users are redirected to login page

### 404 page

* page is accessible to all users


## Bugs discovered

#### Solved bugs

* form input elements too wide on large devices. fix: set max-width value on containers for all forms on site.
* ambiguous error message for 'activate_user' endpoint. changed to inform that link could be already used, expired or invalid.
* inactive user not being deleted during payment process when payment fails on client so the subscribe page just reloads and the inactive user is not reoved from the database and specific error message is not shown to user. fix: endpoint name corrected in ajax call from subscribe.js function.
* Country field and card element placeholder color different to other input elements on non Chrome browsers. Fix: added css to set all same color.
* story form takes a long time to submit and form fields and button remain active while request is processing. Fix: added javascript to disable submit button and add readonly attribute to input fields (note unfixed aspect: select element does not respond to readonly attribute)
* subscribe form not displaying error feedback when user/subscription data is not validated successfully by backend. Fix: added javascript to collect form errors from server json response and loop over these errors to add to DOM. 
* subscribe form 'payment processing' overlay is shown before payment process begins. Fix: defined a different option to disable form while request to create user is sent then overlay is shown only if this request returns successfully.
* image credit field displays label and placeholder when empty in edit story form. Fix: all placeholders for fields were removed to improve UX which fixed this issue.
* elements on site with a background image (homepage hero images, author photo, story images) take along time to load and show as an unattractive gray color in container element while loading. Fix: replace images with compressed versions using online compressor tool. (note unfixed aspect: story images are staff user determined and therefore slow loading cannot be easily prevented if images are large - site author has been advised to mitigate this)
* authenticated user can access login view and see page. fix: replaces all auth views with just login and logout class-based views and passed `redirect_authenticated_user=True` parameter to `LoginView`.
* Instagram link in footer does not open in new tab. Fix: `target="blank"` attribute added.
* Read now button on homepage obscured by browser controls on mobile. Fix: moved button further from bottom of viewport.
* 404 page displays subscribe link to authenticated users. Fix: if cluase added to 404 template to only display this link if user is anonymous.  
* when subscribe form is submitted with errors in the user or subscription form inputs, the submit button disables and errors shown adjacent to respective fields but it is not clesr to the user that there are errors if the respectiv inputs are not in viewport (it appears as if page has frozen). fix: added an error message to inform user there are errors in from to correct directly below the submit button.
* when form passes validation (after previously failing and showing errors) but card payment is not authorized, form is shown again (overlay hides) with previous irrelevant error messages remaining. fix: added JS to clear non card errors from form when confriming card payment since user and subscribe forms have already validated. 
* when form passes validation (after previously failing and showing errors) but card payment is not authorized, form is shown again (overlay hides) but viewport is at top of document so card errors cannot be seen by user and it is unclear what the problem is! fix: added JS to scroll card error messages into view after card payment fails.
* rendering of error messages on login form inconsistent with other forms on site (errors listed at top) fix: error messages moved to below submit button in red font.

#### Unsolved bugs

* django default widget for story.pdf file input field displays a non signed aws s3 url as 'currently' value: therefore permission to get object is denied by AWS. This was not fixed as it was taking too much time to properly update the widget appearing in edit story form  and admin given the project deadline and this bug will only effect staff/superusers so will have limited impact. The user can still view object on the change list page in admin which provides a signed s3 url via application's 'download_story' view. 
* on iphone 12 safari browser the ripple loading animation on subscribe page is jerky and runs too quickly. Not fixed due to time constraints.
* broswer console shows 'input elements should have autocomplete attributes'
* '*' asterisks after some required fields on subscribe form do not hide on mobile browser
* subscription created page is accessible to all users at all times - ideally a call to this url would redirect unless coming from subscribe page after just creating a new subscription. This is harmless as no senstive information can be exposed (user data all comes in url query parameters from subscribe page redirect) and users cannot use it to gain access to stories or activate an inactive account without first subscribing (since this is done by a webhook from Stripe not by 'subscription-created' endpoint logic).
* Story pdfs and images remain in AWS s3 bucket after respective story modelf fields are updated/story instance is deleted- ideally these objects would be replaced/deleted to make most efficient use of s3 bucket space. However, given the small scale and likely limited use of the application this was not a priority given the project's time constraints.

## Other testing

* The author used the website to view, add, edit and delete stories and tested the subscription process over a number of days during the testing process.
