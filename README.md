![A banner of site to add colour to readme.md](static/media/images/urais-kitchen-banner.jpg)

# Urai's Thai Kitchen
https://uriskitchen.herokuapp.com/

## Welcome Reader,

This is a description of this website and all I'ts workings.

## Project target:
---

Urai,s Thai Kitchen is a thai food delivery service for the hungry folk that like Thai food and of course an easy to use eye catching website to obtain such joys.
In this site the user can create an account so the next order will be easier with a simple login.
It,s also part of the Code Institute Fullstack Diploma Course and in this particular project using an Agile methodology I demonstrate the use of a database in two ways. Adding the menus via the admin section and summoning them back to the allocated pages with javascript. Saving the order in local storage and retrieving the order back to show my understanding of database usage.

I've given the user the ability to C.R.U.D. authentication to Create an order, Read back they,re order, Update it at any point until final purchase and of course Delete any items from that order until final purchase.

I've also added special role based authentication to a staff user to gain full access the admin section which again brings in the C.R.U.D.

---

##  Screen shots of the site and it's responsive abilities:


I used http://ami.responsivedesign.is/ to check what it would look like on all devices but the live heroku site refused to work so I used my workspace url which did work this is the work space url https://8000-spurtech-uriskitchen-pe75eqmz4aa.ws-eu46.gitpod.io/.
As you can see it's fully responsive right across all devices and adapts to any screen sizes.
![An image of the site on mulitple screen sizes](static/media/images/urais-kitchen-responsive.jpg)

---

## User stories in an Agile methodology:

### This shows the structure of what went into the project:

![User stories](static/media/images/user-stories1.jpg)
![User stories](static/media/images/user-stories2.jpg)
![User stories](static/media/images/user-stories3.jpg)
![User stories](static/media/images/user-stories4.jpg)

---

# UI/UX

 - As a first time user I would like a site that is eye catching and easy to use.

 - As a first time user I would like a site that is easy to use and quick to order food.

 - As a first time user I would like instructions to order food.

 - As a returning user I would like to login with my username and password so I don't need to keep putting in my details.

 - As a site user I would like complete control of my order if I need to remove or add any items.

 - As a site user I would like to be notified on how long it will take to deliver.

 - As a site user I would like a confirmation email of my order.

 - As a first time user I would like know that my details will secure.

 - As the site owner I would like like to add or delete items in the menus and update anything that requires it.

 - As a staff member I would like special access to the admin page.

 ### all of the above user stories were met 

 ---

## Wireframes:

The wire frames for the pages showcasing the bare structure of the site.

![Landing Page](static/media/images/urais-kitchen-home-wireframe.jpg)
### Links to the other pages:
- [Meals Page](static/media/images/urais-kitchen-meals-wireframe.jpg)
- [Dessert Page](static/media/images/urais-kitchen-desserts-wireframe.jpg)
- [Cart Page](static/media/images/urais-kitchen-cart-wireframe.jpg)
- [Account Pages](static/media/images/urais-kitchen-account-pages-wireframe.jpg)
----

## Organization:

All files are appropriately named with no capitalization or spaces and all in corresponding folders.
Each page has its own css and javascript for ease of maintenance.

---

## features:

# The landing page:

![](static/media/images/urais-kitchen-home.jpg)

I've gone for a posh restaurant look to stand out from the basic white background and black writing for a better User Experience.

The Title is to represent the sign that would be on the front of the building and the instructions how to order is on a slate place mat written in bright bold colors that compliment each other well and stand out clearly.

The restaurants phone number and opening times clearly displayed to the user.

All fonts were used from https://fonts.google.com/ and they were Red Hat Display, sans-serif, Beau Rivage, cursive.

---

![](static/media/images/urais-kitchen-navbar1.jpg)
### The NAVBAR is seen on all pages for ease of use.
![](static/media/images/urais-kitchen-navbar2.jpg)

1. The NAVBAR has a black background which highlights the links and logo well. Linking to Home page, Meal page, Dessert page, Sign up page, log in page and Cart page. I've made the sign up, log in and cart always visible for better UI/UX.
2. The logo also links to the home page.
3. When hovered over the font brightens.
4. The active property brightens the font depending on what page is selected.
5. The NAVBAR is responsive to all screen sizes and collapses down to reveal a drop down section button.
6. The cart will show items added or deleted then will reset after completed order.
7. If user is logged in (log out) will replace sign up and log in.
 
 ---

 # The footer:

![](static/media/images/urais-kitchen-footer.jpg)

1. The footer is shown in all pages for a nice flow.
2. My copyright tag is shown at the bottom with a bold pop to stand out.
3. All fully responsive.

---

# The Meals page:

![](static/media/images/urais-kitchen-meal.jpg)

1. The meals menu was created in the Admin section then formatted by Javascript and summoned to the relevant pages via HTML and styled in the CSS file with each page having it's own J.S and CSS file for ease of maintenance and bug fixing.
2. The images were stored in Cloudinary as Django dose not save media files.
3. The orders on the right is again on a slate background to tie in with the home page and the restaurant feel.
4. If user is signed in the then you can proceed to the cart with the button at the bottom otherwise the user is prompted to sign up or log in.
5. If the user clicks the cart at the top they will again be prompted to sign up or log in to complete the order.

---

# The Desserts page:

![](static/media/images/urais-kitchen-dessert.jpg)

The desserts page is much the same as the meals page in layout and responsiveness. Here you can see the authentication buttons in the orders section that take the user to the relevant account page.

---

# The Account pages:

## All pages designed to flow with each other.

# Sign up page:
![](static/media/images/urais-kitchen-signup.jpg)

- The Sign up page has Username that cant match existing Usernames.
- Email address.
- Password.
- Confirm Password.
- Bank details section but only a demo as I think that will be in the next Project.
- Delivery address.
- The user will be prompted for any errors in the form

# Log in page:
![](static/media/images/urais-kitchen-login.jpg)

- Username.
- Password.

# Log out page:
![](static/media/images/urais-kitchen-logout.jpg)

- Just asks if the user is sure they want to sign out

