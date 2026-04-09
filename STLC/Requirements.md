### Requirements 

---

 ##  The Software

Webshop platform, with the following existing functionalities:

- Register and login functionality  
- Search for products, sort by price, browse categories  
- Add products to favorites  
- Add products to basket  
- Checkout process (billing, shipping info, payment method)  
- Calculation of total price  

---

##  New Features

---

 ##  1. Product Rating System

 Basic Requirement

Users should be able to rate products with a 5-star system and have the option to add written feedback.

---

  Questions

- Can users rate a product multiple times, or only once per product?  
- Are ratings allowed only after purchasing the product, or can any user rate?  
- What is the maximum character limit for written feedback?  
- Should ratings be editable or deletable after submission?  
- How is the overall product rating calculated (average, weighted, etc.)?  
- Should there be moderation or filtering for inappropriate content?  

---

###  Detailed Requirement

- Users can rate a product using a **1–5 star system** and optionally leave written feedback (max **300 characters**)  
- Only logged-in users who have purchased the product can submit a rating  
- Each user can submit only **one rating per product**, but can edit or delete it later  
- The system calculates and displays the **average rating** based on all submitted ratings  
- All written feedback is subject to **moderation and profanity filtering**  

---

##  Age Verification for Alcoholic Products

###  Basic Requirement

Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

---

###  Questions

- Should age verification happen once per session, or every time the user visits the category?  
- What input format should be used (e.g., full date of birth vs. just age input)?  
- What happens if the user enters an invalid age or closes the modal?  
- Should verified users be remembered (e.g., via cookies or account data)?  
- Are there legal requirements (e.g., country-specific age rules or disclaimers)?  
- What happens if a user bypasses the category but accesses alcohol via search or direct link?  

---

###  Detailed Requirement

- When a user navigates to the alcoholic products category, a modal appears requiring age verification  
- Users must input their **full date of birth (DD/MM/YYYY)**  
- If the user is **under 18**, access is denied and they are redirected to the homepage  
- Verification is stored for the session using **cookies**  
- Age verification is enforced across:
  - Category pages  
  - Product pages  
  - Direct links  

---

##  3. Shipping Cost Changes

###  Basic Requirement

Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

---

###  Questions

- What is the exact threshold for free shipping?  
- Is the threshold based on total price before or after discounts?  
- What is the fixed shipping fee for orders below the threshold?  
- Should shipping cost update dynamically in the cart when items are added/removed?  
- How should edge cases be handled (e.g., exactly at the threshold)?  
- Are there different shipping rules for different regions or delivery methods?  

---

###  Basic Requirement

- Orders above **€50** qualify for free shipping  
- Orders below **€50** incur a flat shipping fee of **€5**  
- The threshold is calculated based on **total price after discounts but before taxes**  
- Shipping costs are **dynamically updated** in the cart and checkout pages  
- If the order total is exactly **€50**, free shipping applies  
- Shipping rules are consistent across all regions (no variation by location)  

---
