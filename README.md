# Magnet Fishing

---

The aim of this Website is to provide a platform for fellow Magnet Fishers
to socialise, share fishing experiences and catches, so that enthusiasts
can create a community and further develop their interest in this emerging
sport.

The Website is specifically aimed at the Magnet Fishing community in
Stockholm. It is an embryonic sport but growing extensively, and
it is hoped that this Website will help participates come together,
and fill a well needed gap.

## Demo

---

## UX

---

### Strategy

The main focus of this Website is for the adventurous who are
looking for a new exciting hobbie to participate in and share
their finds with their local community. The Website
will enable participants to create, read, update and delete (CRUD),
their Magnet Fishing catches.

The Website needs to be efficient on mobile devices, as well
as functional and easy to use. This will allow participants to share
finds while Magnet Fishing in Stockholm. The data needs to
be displayed concisely and clearly, with the ability to engage
in CRUD operations out in the field.

The desktop and tablet versions will provide a more visual
and expansive user experience that can be used in a
more comfortable environment after a long day Magnet Fishing.

#### User Stories

- "I would like to know what others are doing in the local
    areas of Stockholm."

- "It would be interesting to know locations where others
    have been, so I can try my luck!"

- "It would be helpful to know what types of magnets people
    are using. Tips of the trade."

- "It would be great to connect with others. To meet up and
    Magnet Fish together and share finds!"

- "I would like to be able to add finds to the app during my
    Magnet Fishing, so it should be easy to use on my mobile"

### Scope

To meet the goals of the users the Website needs to be
intuitive and easy to use. It needs to stand out and excite
participation and provide interesting data for the Magnet Fishing
community.

Photos and videos will be displayed of an example of a
Fishing Magnet with rope, along with examples of finds
after a Magnet Fishing session.

Forms to 'add' and 'edit' catches will be essential for CRUD
purposes and allow for a well structured 'Catch Log'.

A contact page will be implemented for communication and
questions.

### Structure

The Website will have a standard main logo and navigation bar
layered on top of a photo image that's spread across the entire width
and height of the page.

The navigation bar will include the links `Home`, `Catch Log`,
`Add Catches`, and `Contact`, with a separate `Edit` page.

The `Home` page will give an introduction about Magnet fishing
and the functionalities available to use on the Website.

The `Catch Log` page will list participants magnet catches.
Each participants log can be deleted/edited as they wish.

The `Add Catches` and `Edit Catches` pages will have a clear, easy
to use form displayed that can tabulate all data and display for
others to view. A Map will be provided to help define the area of
Stockholm participants have been Magnet Fishing in.

The `Contact` page will be used for any users who wish to get in
contact and ask questions about the Website or interact respectively.

### Skeleton

Please find my Wireframes for Desktop, Tablet and Mobile
[here](https://github.com/Bealby/Milestone-Project-3/blob/master/documentation/wireframes/magnet-fishing-wireframes.pdf)

### Surface

The Website will have a 'fishing' style theme to it, with the
main colours centred around red, `rgb(254, 17, 71)`, and blue,
`rgb(26, 16, 112)`.

The text will be white,`rgb(255,255,255)`, and placed against a
background colour of blue, `rgb(26, 16, 112)`, for clarity of read.

The `hover` colour used for the links will be of a light grey
colour, `rgb(190, 190, 190)`, and red `rgb(254, 17, 71, .7)`,
to help inform users that the links are clickable.

The main fonts used for this Website will be
`'Source Serif Pro', serif` and `'Stardos Stencil', cursive` -
the later font bringing the sailing theme to the forefront.

## Features

---

The Main Web page consists of four separate sections; `Home`,
`Catch Log` (`Edit Catch Log`), `Add Catches` and `Contact`.

A Logo will be displayed prominently at the top and centre of each
Webpage and be clickable to direct you to back
to `Home`. This logo helps define the Website and will be the
first observation for users entering site, promoting this new sport.

The Navbar and content of each Webpage will be displayed in
an inner `container`, over an outer `container`, allowing content
to flow against a fixed background image when scrolling.

The headers for each page will have a 'Call for action' to draw
users to engage with the content.

Much of the layout of the Website used the `Bootstrap Grid System`
of `containers`, `rows` and `columns`; styled by css. This allowed
the Website to be clearly structured and for the content to be
responsive.

### Features of the Website

#### Main Page

**Navigation Bar:**

- **Desktop:**

The navigation bar will be centred and placed
under the 'Magnet Fishing Stockholm' logo. It will have a left
and right padding so that it does not span the full width of
the Webpage.

The Navbar links will be centred and spaced for clarity, with
the stencil font, `'Stardos Stencil', cursive`, being used to
provide the 'Sailing' feel to the Website.

The font colour used for the links will be white,
`rgb(255,255,255)`, which offset well against the red
background of, `rgb(254, 17, 71, .8)`, that has a slight
opacity.

The Links, when hovered over will turn a shade of grey,
`rgb(190, 190, 190, 1)`. A suitable offset colour that does
not distract or overwhelm.

- **Smaller Devices:**

For tablets and mobiles the text is reduced in size
using `Media Queries`, along with the 'Magnet
Fishing Stockholm' logo. This allows for easier
viewing and better fitting for smaller devices.

For mobile devices the `Bootstrap` function was used
to collapse the navbar, displaying a `Hamburger` icon
of the colour white, `rgb(255,255,255)`, using css
styling.

**Sections:**

- **Home:**

The Home page will consist of rows of two columns,
with an image and text side by side. The first row displaying
an image of a Magnet used, with text introducing the
sport of Magnet Fishing.

The second row displaying an image of a recent 'Catch' with
text describing what the Website is about and how to use it.

A small section at the end titled `Video`, will have an
embedded image from `You Tube` of an example find in Stockholm.

The text used in the `Home` page will be,
`'Source Serif Pro', serif`. The colour will be white,
`rgb(255,255,255)`, over a blue background, `rgb(26, 16, 112)`,
for clarity of reading.

- **Smaller Devices:**

For smaller devices the rows will be one column only for the
images and text, with a neat flip function from `Bootstrap`,
`flex-column-reverse flex-lg-row`, used to ensure
that the text starts first before image.

- **Catch Log:**

The `Catch Log` page will display all participants
catches in an `Accordion` collapse feature provided by
Bootstrap. Each row of the `Accordion` will display the location
and date of participants catches. With a top and bottom spacing between
each row to distinguish between them.

`Font Awesome` icons are used to provide intuitive decision
making, into either collapsing the `Accordion` for more information;
or for editing and deleting catch log data respectively.

The text used in the `Catch Log` page will be
`'Source Serif Pro', serif`, of the colour white,
`rgb(255,255,255)`, over a blue background, `rgb(26, 16, 112)`,
for clarity of reading.

The Edit and Delete icons will have a hover effect of grey,
`rgb(190, 190, 190, 1)`, and darker red, `rgb(254, 17, 71, .7)`
respectively for users to intuitively click.

For smaller devices the `Accordion` columns will contract and the
`Edit` and `Delete` buttons will shift to the left for clarity of
viewing.

- **Add Catches/ Edit Catches:**

This page will give the user the opportunity to
input their catches to the Catch Log. Each field of the form will be
highlighted with a red border, `rgb(254, 17, 71, 1)`, using
css styling, to inform users which field they are on.

There are drop down select features for fields to help users choose
the right 'Magnet' and 'Area' respectively.

To help users define which area of Stockholm they Magnet Fished a
`Modal` feature, provided by `Bootstrap`, when clicked will pop-up
and image of 'Areas' in Stockholm that are possible to select.

A submit button, centred at the end of the form, when hovered over and
clicked, automatically updates the `Catch Log`, and directs you there
accordingly.

For smaller device, the form fields are reduced to one column
using the `Bootstrap` property feature. This helps
users input data in a user-friendly manner.

For mobile devices, on the left of each 'Call for action'
header, a left-chevron icon will be displayed using
[Font Awesome](https://fontawesome.com/). This allows the
user to quickly go back if they decide not to 'Add' or 'Edit'
catches. 

- **Contact:**

A simple contact form, that requires all fields to be added
correctly, including email format, is used. A send button, when
clicked, will clear the form and an alert will pop up with
either a 'Message Sent' or Message Failed'. This feature was
provided by sing `swal`. An
alert feature provided by [Sweet Alert](https://sweetalert.js.org/).

### Features Left to Implement

Below is a list of features I feel would be beneficial to
add to the Website at a later date when more data/
information can be provided:

**Security Feature**
Security is required to be strengthened for
each user, so that others cannot delete or edit their logs.
Displaying users’ emails displayed is also not ideal; a
better option would be to include a chat forum.

**Login Facility**
It would be wise and more user friendly to include a login
feature with associated passwords.

**Upload of Images**
A useful feature to implement would be to allow users to
upload their own images. This would greatly enhance the
impact, encourage sharing, and add to the viewing pleasure.

**Add a Rules and Guidance section**
A section could be added to keep participants up-to-date on
rule changes, useful “hot tips”, safety issues and any
locality warning notices.

**Frequently Asked Questions (FAQs)**
Adding a FAQ section would encourage new magnet fisherman,
and engender confidence and the pleasure it can bring.

**Latest News and News Blogs**
As the popularity of the sport increases there will be a need
to harness debate and a thirst for “Latest News”. This could
become a popular element of the site. 

**Cloning of the Website to other Geographic Areas**
The website has been developed for magnet fishermen in Stockholm.
There is no reason why it could not be set up for other Swedish
conurbations or even beyond.

**Use the Website to hold competitions**
To help grow the Magnet Fishermen community and social mixing,
the website, with minor adjustments, could be used to run
Competitions on certain stretches of water. Winners, catches
and prizes could be readily announced.

**Develop the “Catch Log”**
It would better user experience to have a feature to order
Catches by either date, area or name. Including also a search
feature to find certain information. 'Likes' and 'Comment' could
also be available for better interaction.

**Create a Magnet Fishing Membership Club(s)**
Membership clubs could be established by developing the website.
This would entail establishing processes to have members join,
payment systems, regular formal bulletins etc. Eventually the
site could be the main supporting vehicle for a National Magnet
Fishing Club with Club Chairman, Secretary and Committee!

**Create a link to a real-time weather forecasting site**
Creating such a link would be a service to the user.

**Include a “Safety” section on the Navbar**
Magnet fishing has its dangers: deep water; excited children; 
slippery surfaces for example. Warnings of such dangers could be
given in a “safety” section on the Navbar.

## Testing

---

### Automated Testing

[W3C](https://validator.w3.org/) - All HTML files with their data were directly
    inputted in the Mark-Up Validation Service.
    The results:`Document checking completed. No errors or warnings to show.`

[WSC](https://jigsaw.w3.org/css-validator/) - CSS data was directly inputted in
    the CSS Validation Service. The results: `Congratulations! No Error Found.`

[PEP8](http://pep8online.com/) - Python script - `app.py`- was run through PEP8 online
    for PEP8 requirements. Results: `All Right` (Adheres to PEP requirements)

[Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
A feature in Chrome Developing Tools - Lighthouse Audit - was carried out
on Mobile and Desktop to assess **Performacne**, **Accesibility**,
**Best Practices**, **CEO** and **Progressive Web App**.

- **Mobile:** An overall average of 86% was received.
- **Desktop:** An overall average of 80% was recieved.

`Performance` 


[Validate Javascript](https://validatejavascript.com/) - 

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)

### Non-Automated Testing

#### Background Image
- Ensure Background image is fixed and scrolls correctly for all devices 

#### Navigation Bar Links & Logo

- Click through `Home`, `Catch Log`, `Maps`, and `Contact` links,
  ensuring each, when hovered over turn light grey, and direct you to the
  correct sections
- Click each navigation link and randomaly navigate to other links
- On each navigstion link, ensure when the logo is clicked, that
  redirects `Home`.
- Ensure navigation collapse Bootstrap feature kicks in on smaller devices
  and the links continue to work correctly as process above.

#### Home Page

- Ensure a centred header is displayed for all devices
- For Desktop devices ensure the `Home` page is divided into two columns
  with first row of an image and text box, and the second row of a text box and image
- Ensure that the third row includes a single column that includes a video
- Ensure video plays
- For smaller devices ensure the `Home` page is divided into one column of the order
  text box, image, text box, image. All centred on page.
- For smaller device ensure video is aligned on one single column. Centred and that plays

#### Catch Log/ Edit Catches

- Ensure a centred header is displayed for all devices
- Click on `Accordion`cards and ensure each collpses and uncollapses
  accordingly. 
- Click randomly through `Accordion` cards and ensure as one card collapses another
  card uncollapses
- For each `Accordion`card collapsed ensure that data is shown correctly.
 - One column for `Name`, `Email` and `Location`, respectively. 
   The second column for `Magnet` and `Catches` respectively.
- For example `Accordion` cards ensure each can be deleted when clicking the 
  `Delete`icon.
  - ensure delete hovers dark red
- For each `Accordion` card click on the `Edit` icon and ensure directs it
  you to `edit_catch_log.html`
  - ensure Edit hovers grey
- Ensure `Edit` page has fields filled in from data shown in Catch Log page.
- Ensure all fields have placeholder names
- Ensure all fields can be inputted and that the select features for `Magnet`and
`Area` collapse with correct options to choose from work
- Ensure `Modal` map icon, when clicked, pops-up a map, which can then be closed
- ensure Modal hovers grey 
- Ensure `Date` fields allow for date picking and display correct date format. 
- Enusre form fields are layout correctly for desktop devices. The first row
  should be two columns for 'Name' and 'Email, and the second row 3 columns for
  'Magnet', Area and Map. 
- Ensure remaing field are centered and in one single column.
- Change some fields in `Edit`page and click on `Submit`. You should be directed
 back to Catch Log. Ensure fields have been updated
  - Click on Home link and re-eneter Catch Log to ensure edit changes have been made are
- try same procidure above but with different card sin Catch Log..
- For smaller devices all form fields should be centred in one single column.
- For smaller devices run through step above.

#### Add Catches
- Ensure a centred header is displayed for all devices
- Ensure `Add Catches` page have all fields placeholder names
- Ensure all fields can be inputted and that the select features for `Magnet`and
`Area` collapse with correct options to choose from work
- Ensure `Modal` map icon, when clicked, pops-up a map, which can then be closed
- ensure Modal hovers grey 
- Ensure `Date` fields allow for date picking and display correct date format. 
- Enusre form fields are layout correctly for desktop devices. The first row
  should be two columns for 'Name' and 'Email, and the second row 3 columns for
  'Magnet', Area and Map. 
- Ensure remaing field are centered and in one single column.
- Add a number of catches in page  and click on `Submit`. You should be redirected
 back to Catch Log. Ensure new added catches on displayed on Catch Log. 
 - Click on Home and re-eneter Catch Log to ensure new enetirs are there.
- try same procidure above but with different card sin Catch Log..
- For smaller devices all form fields should be centred in one single column.
- For smaller devices run through step above.

#### Contact
- Ensure a centred header is displayed for all devices
- Ensure form and fields iare centred for all devices
- Ensure all fields are required by typing in a name
but correct email and comment. Click Send. Pop up 'Please
fill in this field`
- Typing in an email but correct name and comment. Click Send.
Pop up 'Please include @ sign'
- Typing in an comment but correct name and email. Click Send.
Pop up 'Please
fill in this field`
- input all fields with correct naem, email format and Message. Click send.
Pop Up Window "Message Sent - We will be in touch soon!
- Turn off internet connection. fill in all correct fields. press send.
"Message Fail "Please check connection and try again"
  - ensure send icon hovers grey 
  - for smaller devices please run thorugh steps above. 

#### Footer

Ensure that Copyright text in footer is centred for all devices.

#### Desktop Browesers

- Chrome: Website renders well on all screen sizes.
- Safari: Website renders well on all screen sizes.
- Firefox: Website renders well on all screen sizes.
- Edge: Website renders well on all screen sizes.

#### Mobile and Tablet Devices

- The Website was tested on tablets and a variety of
  mobiles, including iPhone and Samsung. The results were
  satisfactory for all devices and continued to acheive the
  UX and UI goals.

#### User Testing

- Family and friends were asked to use the finished Website to test
  usability and comment on whether they felt it met their needs as discussed
  in the Strategy section - [User Stories](#user-stories).

- iphone 8 - Chrome: Good
- iphone xs - Chrome: Good
- iphone xs - Safari: Good
- iphone 8 - Chrome: Good
- iphone 8 - Safari: Good
- iphone 8 - Chrome: Good
- iphone 11 - Safari: Good
- iphone 11 - Safari: Good
- Samsung 7 - Chrome: Good

#### User Experience

- Overall the Website fulfiled user expectations. They found theWebsite informtive and enticing
  and the information provided in the Catch Log to be satisfactory. It allowed users to have knowledge
  of where other particpants have Maget Fished and tabulated finds in a concise and easy to use manner.

- It was noted that even though email addresses were provided a more security based feature would be better
suited for the user and have more of a chat function to communicate with others and not just by email. 

- Tips and more detailed information was perhaps limited and did not provide the useful tips and guidance but
    this has be addressed 'Features Left to Add and can be expanded later in the future.

- Users wanted to be able to inout Cathes on their mobile while Magnet Fishing. To help in the usability and
 convienience of being out in the field a left cheron was added to mobile devices to be able to go back quickly to Catch Log.
 

#### Fixes

- When carrying out User Testing it was made apparant that the background image which was set up, was working for
most phones except for iphone - specifially Safarai. The BAckground-imagew became more blurry as the more content was addeded to page. 
This was particular IOS issue and was fixed by firstly declaring the body and html to be 100% wide and 100% tall,
`html, body{width: 100%; height: 100%;}`. The scrolling is then done by the container and not the body, which in
turn means wrapping the container with the following parimenters, `#wrapper{width: 100%; height: 100%; overflow: scroll;}`.

This fix was provided and supported by
[Stackoverflow](https://stackoverflow.com/questions/41436892/background-attachment-fixed-doesnt-work-on-ios)

- The `Accordion` collapse feature in Catch Log page was, upon clicking the card, collapsing all cards at once. 
Since eash Card had the same data-target and the same div id all of them were collapsing all together.
This was fixed by using the loop index from the jinja for loop. `data-target="#collapse{{ loop.index }}"` 
and `div id="collapse{{ loop.index }}"`. Inspriaration for this fix was supported by Keven at Code-Institute Support. 


## Technolgies Used

---

The following technolgies were used in this project:

**IDE:**
- [GitPod](https://gitpod.io/workspaces/) - A platform used for hard coding
   of Website

**Hosting/ Deployment**
- [Heroku](https://id.heroku.com/) - Heroku is a cloud platform as a service supporting several programming languages.
- [GitHub](https://github.com/)** - Used to store repository and deploy Website

**Languages:**
- [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language of Website
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used to style
   HTML elements
- [Python](https://www.python.org/) - A programming language that lets you work quickly
   and integrate systems more effectively
- [JavaScript](https://www.javascript.com/) - Used in collabration with
   Bootstrap to collaspe Navigation Bar for small devices and Google Maps

**Databases**
- [MongoDB](https://www.mongodb.com/) - MongoDB is a general purpose, document-based, distributed database built for modern application developers

**Language Validators:**
- [W3C](https://validator.w3.org/) - Used to validate HTML code
- [WSC](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [Validate Javascript](https://validatejavascript.com//) - Used to validate javascript
- [Pep8 online](http://pep8online.com/) - Validator for Python code
- [Markdown Lint](https://github.com/Bealby/markdownlint) - Used for validation
    checks on README.md content

**Libraries:**
- [Google Fonts](https://fonts.google.com/) - Programme used to import main
   fonts in Website: **Playfair Display** and **Calligraffitti**
- [Font Awesome](https://fontawesome.com/) - Programme used to import icons
   for Footer in Website: **far-envelope** and **fas fa-phone**

**Tools**
- [Balsamiq Wireframes](https://balsamiq.com/wireframes/desktop/)** - Allowed
   preliminary designs to be drawn up of Website
- [Adobe Photoshop](https://www.adobe.com//) - Fixing size images
- [Adobe Illuetrator](https://www.adobe.com//) - Fixing Logo - Magnet Fishing Stockholm
- [Sweet Alert](https://sweetalert.js.org/) - Used for alerts in contact form
- [Responsive Design](http://ami.responsivedesign.is/) - Free software
    to generate Mockup of Website on different devices
- [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
    Helped to improve the quality of Website
- [Chrome Developer Tools](https://www.google.com/chrome/dev/Google) - A useful
   developing tool in Chrome to edit pages and diagnose problems

**Frameworks**
- [BOOTSTRAP](https://getbootstrap.com/) - A famework for building responsive
   Websites where the powerful Grid system was used along with styling
- [jQuery](https://jquery.com/) - Used to implement Navigation Collaspe feature
   JavaScript Plugin
- [Popper](https://popper.js.org/) - Used to implement Navigation Collaspe
   feature JavaScript Plugin
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework written in Python
- [Emailjs](https://www.emailjs.com/) - For sending email directly From JavaScript







