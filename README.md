# Magnet Fishing

---

The aim of this Website is to provide a platform for fellow Magnet Fisherman
to socialise, share fishing experiences and catches, so that enthusiasts
can create a community and further develop their interest in this emerging
sport.

The Website is specifically aimed at the Magnet Fishing community in
Stockholm. It is a embryonic sport but growing extensively, and
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

Photos and videos will be displayed of an example of a Magnet
along with examples of finds after a Magnet Fishing session.

Forms to add and edit catches will be essential for CRUD
purposes and allow for a well structured Catch Log.

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

The Main Web page consists of four separate sections; `Home`;
`Catch Log` (`Edit Catch Log`); `Add Catches` and `Contact`.

A Logo will be displayed prominently at the top and centre of each
Webpage and be clickable to direct you to back
to `Home`. This logo helps define the Website and will be the
first observation for users entering site, promoting this new sport.

The Navbar and content of each Webpage will be displayed in
an inner `container`, over an outer `container`, allowing content
to flow against a fixed background image when scrolling.

Much of the layout of the Website used the `Bootstrap Grid System`
of `containers`, `rows` and `columns`; styled by css. This allowed
the Website to be clearly structured and for the content to be
responsive.

### Features of the Website

#### Main Page

**Navigation Bar:**

- **Desktop:**

The navigation bar will be cantered and placed
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
an image of a Magnet used with text introducing the
sport of Magnet Fishing.

The second row displaying an image of a recent 'catch' with
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

The text used in the `Home` page will be
`'Source Serif Pro', serif`, of the colour white,
`rgb(255,255,255)`, over a blue background, `rgb(26, 16, 112)`,
for clarity of reading.

The Edit and Delete icons will have a hover effect of grey,
`rgb(190, 190, 190, 1)`, and darker red, `rgb(254, 17, 71, .7)`
respectively for users to intuitively click.

For smaller devices the `Accordion` columns will contract and the
`Edit` and `Delete` buttons will shift to the right for clarity of
viewing.

- **Add_Catches:**

This page will give the user the opportunity to
input their catches to the Catch Log. Each field of the form will be
highlighted with a red border, `rgb(254, 17, 71, 1)`, using
css styling to inform users which field they are on.

There are drop down select features for fields to help users choose the
right 'Magnet' and 'Area' respectively.

To help users define which area of Stockholm they Magnet Fished a
`Modal` feature, provided by `Bootstrap`, when clicked will pop-up
and image of areas in Stockholm that are possible to select.

A submit button centred at the end of the form, when hovered over and
clicked, automatically updates the `Catch Log`.


Chevron - for back

- **Edit_Catches:**

There is also an `Edit Catches` page
which mirrors the `Add Catch` page. When this Edit feature
button is clicked on the `Catch Log` page,
fields will display original choices for ease of reference.

For smaller device, the form fields are reduced to one column
using the `Bootstrap` property feature. This helps
users input data in a user friendly manner.


Chevron - for back

- **Contact:**

A simple contact form that requires all fields to be added
and that a correct email format is used. A send button, when
clicked, will clear the form and alert users if the message has been
sent or failed.

SWAL Sweet Alert

### Features Left to Implement

Below is a list of features I feel would be beneficial to
add to the Website at a later date when more data/
information can be provided:

**Login and Security Feature:**

It would be wise to implement a Login feature to the Website,
as well individual security for each user, so that others can
not delete or edit their logs. Having users’ emails
displayed is not ideal also. A  better option would be to include
a chat forum.

**Upload of Images:**
A useful feature to implement would be for users to upload images
This would greatly enhance the impact and viewing pleasure.

**New Sections:**

There are a number of very beneficial sections to add, which could
include a 'News Blog' to update participants
of changes in rules etc; a guide and useful tips section and a section
for FAQs.

**Expansion of Website:**
The Website could very easily be expanded to other outer Areas of
Stockholm, as well as expanded throughout Sweden.

**Catch Log:**
Sorting and appending using python??????



**Support Collapsible**
https://www.w3schools.com/howto/howto_js_collapsible.asp

**placeholder date not working**
https://stackoverflow.com/questions/20321202/not-showing-placeholder-for-input-type-date-field

## Technolgies Used

---

The following technolgies were used in this project:

**Sections:**

- **[Balsamiq Wireframes](https://balsamiq.com/wireframes/desktop/)** - Allowed
   preliminary designs to be drawn up of Website
- **[GitHub](https://github.com/)** - Used to store repository and deploy Website
- **[GitPod](https://gitpod.io/workspaces/)** - A platform used for hard coding
   of Website




- [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language of Website
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used to style
   HTML elements
- [BOOTSTRAP](https://getbootstrap.com/) - A famework for building responsive
   Websites where the powerful Grid system was used along with styling
- [Google Fonts](https://fonts.google.com/) - Programme used to import main
   fonts in Website: **Playfair Display** and **Calligraffitti**
- [Font Awesome](https://fontawesome.com/) - Programme used to import icons
   for Footer in Website: **far-envelope** and **fas fa-phone**
- [JavaScript](https://www.javascript.com/) - Used in collabration with
   Bootstrap to collaspe Navigation Bar for small devices and Google Maps
- [W3C](https://validator.w3.org/) - Used to validate HTML code
- [WSC](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [jQuery](https://jquery.com/) - Used to implement Navigation Collaspe feature
   JavaScript Plugin
- [Popper](https://popper.js.org/) - Used to implement Navigation Collaspe
   feature JavaScript Plugin
- [Markdown Lint](https://github.com/Bealby/markdownlint) - Used for validation
    checks on README.md content
- [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
    Helped to improve the quality of Website
- [Chrome Developer Tools](https://www.google.com/chrome/dev/Google) - A useful
   developing tool in Chrome to edit pages and diagnose problems
- [Responsive Design](http://ami.responsivedesign.is/) - Free software
    to generate Mockup of Website on different devices
- [Validate Javascript](https://validatejavascript.com//) - Used to validate javascript
- [Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial)
   For API key and Javascript Map options