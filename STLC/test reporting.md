# Test Execution Report — GroceryMate

**Application:** GroceryMate  
**URL:** https://grocerymate.masterschool.com/  
**Tester:** Barry Despenza  
**Date:** April 14, 2026  
**Environment:** Chrome (latest), macOS  

---

#  Scenario 1: Give Minimum Rating (1 Star)

**User Story:**  
As a logged-in user who purchased a product, I want to submit a rating so that I can share feedback

---

##  Test Steps

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter username: Kendricklamar@gmail.com | Username accepted | OK | | |
| 2b | Enter password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | Click Shop button | Navigated to store page | OK | /store | |
| 5 | Select Baresa Spaghetti → Click Add to Cart | Message displayed: Item added to cart | OK | | |
| 6 | Click cart icon | Navigated to checkout page | OK | /checkout | |
| 7a | Enter street: ABC | Field accepted | OK | | |
| 7b | Enter city: Berlin | Field accepted | OK | | |
| 7c | Enter postal code: 12345 | Field accepted | OK | | |
| 7d | Enter card number: 12345 | Field accepted | OK | | |
| 7e | Enter name on card: Abc | Field accepted | OK | | |
| 7f | Enter expiration date: 12/2032 | Field accepted | OK | | |
| 7g | Enter CVV: 123 | Field accepted | OK | | |
| 8 | Click Buy Now | Redirected to homepage | OK | | |
| 9 | Click Shop button | Redirected to store page | OK | /store | |
| 10 | Click Baresa Soaghetti | Redirected to product page | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990 | |
| 11 | Select 1 Star rating | 1 star is highlighted | OK | | |
| 12 | Click Send button | Rating visible & message displayed: "You already reviewed this product" | OK | /store | |

---
## ✅ Result
User successfully submits a 1-star rating and receives confirmation message indicating duplicate review prevention.

---

### Scenario 2: Rating Without Purchase

**User Story:**  
As a user, I should not be able to rate products I haven’t purchased.

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter username: Kendricklamar@gmail.com| Username accepted | OK | | |
| 2b | Enter password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | Click Shop button | Navigated to store page | OK | /store | |
| 5 | Select Baresa Spahgetti| You need to buy this product to tell us your opinion! | OK |https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a66 | |

## ✅ Result
User is not able to successfully able to submit a product that have not purchased.

---

### Scenario 3: Feedback Character Limit

**User Story:**  
As a user, I want feedback length to be limited to ensure proper display.

| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter username: Kendricklamar@gmail.com | Username accepted | OK | | |
| 2b | Enter password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | Click Shop button | Navigated to store page | OK | /store | |
| 5 |Click Baresa Soaghetti | Redirected to product page | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990 | |
| 6 | Select 1 Star rating | 1 star is highlighted | OK | | |
| 7 | Enter feedback comment with 500 characters. abc..... until you reach 499  |You cannot tell us more about this product.| OK | /store | |
| 8 | Click Send button | Rating visible & message displayed correctly|: "You already reviewed this product" but the display does not show all of the message abc........  | NOK |  | |

##  Result
User was not successfully able to  submit a product review past 499 characters to display proper display 

---

## Feature 2: Age Verification for Alcohol

### Scenario 6: Access Alcohol Category

**User Story:**  
As a user, I should verify my age before accessing alcohol products.

##  Test Steps

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter creates a username: Kendricklamar@gmail.com | Username accepted | OK | | |
| 2b | Enter a password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | User views the bday modal| Message displayed: Age Verification
You need to be +18 to see some products. Please enter your birth date| OK | | 
| 6 | Enter bday credentials - 19.06.1991 | Field accepted | OK | | |
| 7 | Click confirm | Rating visible & message displayed: 
You are of age. You can now view all products, even alcohol products. | OK | /store | |

---
## ✅ Result
User successfully has access to alcohol products once they set up their account with the proper age verification.


---

### Scenario 7: Valid Age Access (18+)

**User Story:**  
As a user 18+, I should access alcohol products.

##  Test Steps

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter creates a username: Kendricklamar@gmail.com | Username accepted | OK | | |
| 2b | Enter a password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | Click Shop button | Navigated to store page | OK | /store | |
| 5 | Select Corona extra beer → Click Add to Cart | Message displayed: Item added to cart | OK | | 

---
## ✅ Result
User successfully has access to alcohol products once they set up their account with the proper age verification.

### Scenario 9: Invalid DOB Input

**User Story:**  
As a user, I should receive validation errors for invalid DOB.

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter creates a username: Travisscott@gmail.com | Username accepted | OK | | |
| 2b | Enter a password: Kanyewest16!| Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | User clicks shop | Products displayed | OK | https://grocerymate.masterschool.com/store | || 
| 6 | Enter bday credentials - 19.06.2026 | Field not accepted | Message displayed you are underage to view alcohol products. OK | | 

## ✅ Result
User can not successfully access alcohol products if they are underage.

---

## Feature 3: Shipping Cost Changes

### Scenario 10: Free Shipping Threshold (€20)

**User Story:**  
As a user, I want free shipping when my cart reaches €20.

| Step# | Action                   | Expected Outcome      | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|--------------------------|-----------------------|------------------|--------|-----|---------------|
| 1     | Log in                   | User logged in        | Login successful | OK     | https://grocerymate.masterschool.com/    |               |
| 2     | Navigate to shop section | Product page loads    | work             | OK     |     |               |
| 3     | Add items totaling €20   | Free shipping applied | Applied          | OK     |     |               |

---

### Scenario 11: Below Threshold (€20)

**User Story:**  
As a user, I should pay shipping below €20.

| Step# | Action                     | Expected Outcome        | Actual Outcome | OK/NOK | URL | Link to Issue |
|-------|----------------------------|-------------------------|----------------|--------|-----|---------------|
| 1     | Log in                     | User logged in          | Login successful | OK   | https://grocerymate.masterschool.com/    |               |
| 2     | Navigate to shop section   | Product page loads      | work           | OK     |     |               |
| 3     | Add items totaling €19.99  | €5 shipping fee applied | Applied        | OK     |     |               |

---

### Scenario 14: Empty Cart Behavior

**User Story:**  
As a user, I should not see shipping cost when cart is empty.

| Step# | Action             | Expected Outcome    | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|--------------------|---------------------|------------------|--------|-----|---------------|
| 1     | Log in             | User logged in      | Login successful | OK     |  https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to cart   | Products appear     | Works            | OK     |     |               |
| 3     | Remove all items   | €5 shipping removed | Succesful        | OK     |     |               |

