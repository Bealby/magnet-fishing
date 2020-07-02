# Magnet Fishing

---

The aim of this Website is provide a platform forum, of Magnet Fishing Catches,
for this energising sport so that enthuisasits can create a community and
develop their interest.

The Website is specifically aimed at the Magnet-Fishing community in
Stockholm. It is a niche sport but growing extensively and
it is hoped that this Website will help particpates come together, and
fill a well needed gap.

## Demo

---

## UX

---

### Strategy

The main focus of this Website is for the adventurous who are
looking for a new exciting hobbie to particpate in and share
their finds with their local community. This Website
will enable prticipants to interact, share and communicate - 
expanding the sport of Magnet fishing.

The Website needs to be efficient on mobile devices, as well
as functional and easy to use, allowing partipants to share
finds while on the move through Stockholm. The data needs to
be displayed concisely and clearly, with the ability to add data
in an easy fahsion. 

The desktop and tablet versions will provide a more visual
and expansive user experience that can be perused in a 
more comfort able enviironmet after a long day.

#### User Stories

- "I would like to know what others are doing in the local areas of Stockholm."

- "It would be interesting to know locations where others have been, so I can try my luck!"

- "It would be helpful to know what types of magnets people are using. Tips of the trade."

- "It would be great to connect with others. To meet up and Magnet-Fish together"

- "I would like to be able to add finds to the app during my Magnet Fishing, so it should be
    easy to use on my mobile"

### Scope

To meet the goals of the users the Website needs to be
intuitive and easy to use. It needs to stand out and excite
particpation and provide intersting data for the Magnet-Fishing
community.

Photos will be displayed of Magnets and Magnet finds. 

A Map will be provided to display the areas of 
Stockholm, with the a Webpage displaying all participants 
catches by location. 

### Structure

The Website's will have a standard main logo and navigation bar
layered on top of a photo image that's spread across the entire width
and height of the page. 

The naviagtion bar will have a the links `Home`, `Catch Log`, 
`Add Catches`, and `Contact`, with a separate `Edit` page.

The `Home` page will give an introduction about Magnet fishing
and the functionalities available to use on the Website.

The `Catch Log` page will list participants catches, sorted by date.
Each particpatnts log can be deleted and edited as they wish.

The `Add Catches` and `Edit Catches` pages will have a clear, easy
to use form displayed that can tabulate all data and display for
other's to view. An Map will be provided to help define the area of Stockholm
particpants have been Magnet Fishing in. 

The `Contact` page will be used for any users who wish to get in 
contact and ask questions about the Website or interact respectively.

### Skeleton

Please find my Wireframes for Desktop, Tablet and Mobile
[here](https://github.com/Bealby/Milestone-Project-3/blob/master/documentation/wireframes/magnet-fishing-wireframes.pdf)

### Surface

### Surface

The Website will have a fishing style colour theme to it, with the main
colors centered around red, `rgb(254, 17, 71)`, and blue, `rgb(26, 16, 112)`.

The text will be white, `rgb(255,255,255)`, and placed against a background
color of blue, `rgb(26, 16, 112)` for clarity of read.

The `hover` colour used for the links will be of a light grey colour,
`rgb(190, 190, 190)` and red *rgb(254, 17, 71, .7), to help inform users
that the links are clickable.

The main fonts used for this Website will be `'Source Serif Pro', serif`
and `'Stardos Stencil', cursive` - the later font bringing the sailing theme
to front. All fonts were obtained from `Google Fonts`.


## Features

---

The Main Web page consists of four separate sections; `Home`; `Catch Log` (`Edit Catch Log`);
`Add Catches` and `Contact`.

A Logo will be prominant top, center of each Webpage and will be clickable and direct back to `Home`.

The Navbar and content will be displayed in an inner container, over a
a scrolling `background` image.

Much of the layout of the Website used the `Bootstrap Grid System` of `containers`,
`rows` and `columns`; styled by css. This allowed the Website to be clearly
structured and for the content to be responsive.

### Features of the Website

#### Main Page

**Navigation Bar:**

- **Desktop:** The navigation bar will be centered and placed under the 
'Magnet Fishing Stockholm' logo. It will hav a left and right padding so that it
does not span full width of page. The Navbar links will be centred and spaced for clarity
witn the stencil font `'Stardos Stencil', cursive` being used to give the sailing feel to the 
Website. 

The font color used for the links will be white, `rgb(255,255,255)`, which best offsets the red background. 
The Links, when hovered over will turn the shade of grey, `rgb(190, 190, 190, 1)`. A fitting offset color that
that is subtle and does not distract.

- **Smaller Devices:**
    For tablets and mobiles the text is reduced in size using `Media Queries`, along with the 
    the 'Magnet Fishing Stockholm' logo, for easier viewing on smaller devices.

    For mobile devices the `Bootstrap` function was used to collaspe the navbar, displaying
    a `Hamburger` icon of the color white, `rgb(255,255,255)`.


**Sections:**

- **Home:** The Home page will consist of rows of two columns, with an image and text
    side by side. The first row displaying an image of a Magnet used with text introducing the 
    sport of Magnet Fishing.

    The second row displaying an image of a recent 'catch' with text describing what the
    Website is about and how to use it.

    A small section at the end titled `Videos`, will have an embedded image from `You Tube`
    of a recent 'catch' in Stockholm.

    The text used in the `Home`page will be `'Source Serif Pro', serif` of the color white,
    `rgb(255,255,255)`, over a blue background, `rgb(26, 16, 112)`, for clarity of reading.

- **Smaller Devices:**
    For smaller devices the rows will be one column only for the images and text, with a neat
    flip function from `Bootstrap`, `flex-column-reverse flex-lg-row`, used to ensure
    that the text starts first before image. 

- **Catch Log:** The `Catch Log`page will display all particpantds catches in an Accordion style
  collapse feature privided by Bootstrap. Each row of the Accordion will display the location and 
  date of catch. With a top and bottom spacing to distinguish btween them. 

  `Font Awesome`icons are used to provid intuitive decision making, into either collapsing Accordion rows for
  more information or for editing and deleting conversly. 

  Once again The text used in the `Home`page will be `'Source Serif Pro', serif` of the color white,
    `rgb(255,255,255)`, over a blue background, `rgb(26, 16, 112)`, for clarity of reading.

    The Edit and Delete icons will have a hover affect of grey, `rgb(190, 190, 190, 1)`, and darker red, `rgb(254, 17, 71, .7)`
     for intuitive knowledge that they can be clicked accrodingly. 

     For smaller devices the Acordion columns with contract and the Edit and Delete buttons
     will shift to the right for clarity of viewing.

- **Add_Catches:** This page will give the user the opportunity to inout their catch to the 
    Catch Log. Each field of the form will be highlighted with a red border, `rgb(254, 17, 71, 1)`, using css styling
    to infomr users the field they are in. 
    
    there are drop down features for fields to help users choose the right Magnet and Area. 
    
    For the choose Area field a Modal feature form Bootstrap can be clicked and an image pop up of the areas in 
    Stockholm to help the user identify the place where they have gone Magnet Fishing. 

    A submit button centred at the end of the form, when hovered over and clicked, automatically updates `Catch Log`. 

- **Edit_Catches:** the is also a Edit Catches page which mirriros the Add Catche page. When this Edit feature button is cloicked 
    in Catch_log the fields originally chosen will be displayed in the form fields for reference. 


for mobile smaller device, the form fields are reduced to one column only using the Botstrap propery feature. This helps
users inout data in aneasier mnanner on smaller devices. 


- **Contact:** 

A simple contact form that requires all fields to be added including correct email format. A send button when clicked, will cleqr form and prodce and 
alert of message has failed on succeded.


### Features Left to Implement

Below are a list of features I feel would be beneficial to add to the Website
at a later date when more data/ information can be provided:

**Login and Security Feature:**
It would be wise to implement a Login feature to the Website as well as have individual securty for 
each particpants Catches so that other's can not delete or edit them. Also having particpants emails
displayed is not ideal. an option to click on another particpants name to then send them a direct email 
or better still a chat facilicity.

**Upload of Images:**
A useful feature to implement would be the option to upload images to particpants Catch Log. This would 
great enhance the impact and viewing pleasure for uses.

**New Sections:**
There are a number of very beneficial sections to add, which could include a News Blog to update particpants
of changes new rules; a section on specific infomraiton on Magnet Fishing (Ropes to use, Magnets steength advice)
General asvice and support. FAQs.

**Expansion of Website:**
the Website could very easily be expanded to other outer Areas of Stockholm, and expanded throughout Stockholm
itself.


















Support Collapsible 
https://www.w3schools.com/howto/howto_js_collapsible.asp


placeholder date not working
https://stackoverflow.com/questions/20321202/not-showing-placeholder-for-input-type-date-field


https://sweetalert.js.org/guides/#getting-started