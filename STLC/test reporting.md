# Test Execution Report — GroceryMate

**Application:** GroceryMate  
**URL:** https://grocerymate.masterschool.com/  
**Tester:** Barry Despenza  
**Date:** April 14, 2026  
**Environment:** Chrome (latest), macOS  

---

# 📌 Scenario 1: Give Minimum Rating (1 Star)

**User Story:**  
As a logged-in user who purchased a product, I want to submit a rating so that I can share feedback

---

## 🧪 Test Steps

| Step # | Action | Expected Outcome | Status | URL | Issue |
|-------|--------|------------------|--------|-----|-------|
| 1 | Go to the login page of GroceryMate | Login page appears | OK | https://grocerymate.masterschool.com/ | |
| 2a | Enter username: asdf@example.com | Username accepted | OK | | |
| 2b | Enter password: AsDfGh | Password accepted | OK | | |
| 3 | Click Sign In | User is successfully logged in and redirected to homepage | OK | | |
| 4 | Click Shop button | Navigated to store page | OK | /store | |
| 5 | Select Pears → Click Add to Cart | Message displayed: Item added to cart | OK | | |
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
| 10 | Click Pears | Redirected to product page | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990 | |
| 11 | Select 1 Star rating | 1 star is highlighted | OK | | |
| 12 | Click Send button | Rating visible & message displayed: "You already reviewed this product" | OK | /store | |

---
## ✅ Result
User successfully submits a 1-star rating and receives confirmation message indicating duplicate review prevention.

---

### Scenario 2: Rating Without Purchase

**User Story:**  
As a user, I should not be able to rate products I haven’t purchased.

| Step# | Action               | Expected Outcome       | Actual Outcome | OK/NOK | URL | Link to Issue |
|-------|----------------------|------------------------|----------------|--------|-----|---------------|
| 1     | Log in (no purchase) | User logged in         | Login successful            | OK     |  https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to pink lady apples  product  | Product loads          | OK             | OK     | https://grocerymate.masterschool.com/store    |               |
| 3     | User click 1 star rating    | Inline message appears below the product | OK             | OK     | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a6    |               |

---

### Scenario 3: Feedback Character Limit

**User Story:**  
As a user, I want feedback length to be limited to ensure proper display.

| Step# | Action                        | Expected Outcome               | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-------------------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in                | Login successful | OK     |  https://grocerymate.masterschool.com/https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to purchased product | Product page loads            | success           | OK     |  https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a6   |               |
| 3     | Select star rating            | Rating selected               | success            | OK     |     |               |
| 4     | Enter feedback (500 chars)    | Feedback accepted             | success            | OK     |     |               |
| 5     | Enter feedback (2 chars)      | Feedback not accepted         | success            | NOK    |     |   [Feedback Length Validation Bug](https://github.com/bdespenza91/example-portfolio/issues/13)            |

---

### Scenario 4: Empty Feedback Submission

**User Story:**  
As a user, I should be able to submit a rating without feedback if optional.

| Step# | Action                        | Expected Outcome   | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|--------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in     | Login successful  | OK     |  https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to purchased product | Product page loads | Page success      | OK     |  https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a6   |               |
| 3     | Select desired rating         | Rating selected    | Success           | OK     |     |               |
| 4     | Enter no feedback comment     | Review accepted    | Success           | OK     |     |               |

---

## Feature 2: Age Verification for Alcohol

### Scenario 6: Access Alcohol Category

**User Story:**  
As a user, I should verify my age before accessing alcohol products.

| Step# | Action                        | Expected Outcome                  | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-----------------------------------|------------------|--------|-----|---------------|
| 1     | User Create account           | User logged in                   | Login successful | OK     |  https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to shop section      | Product pages loads              | Success          | OK     |  https://grocerymate.masterschool.com/store   |               |
| 3     | Select alcohol tab            | Alcohol products are loaded      | Success          | OK     |     |               |
| 4     | Age Verification modal appears| Error message appears to verify  | Success          | OK     |     |               |

---

### Scenario 7: Valid Age Access (18+)

**User Story:**  
As a user 18+, I should access alcohol products.

| Step# | Action                        | Expected Outcome      | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-----------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in        | Login successful | OK     | https://grocerymate.masterschool.com/    |               |
| 2     | Navigate to shop section      | Product page loads    | work             | OK     |     |               |
| 3     | Select alcohol tab            | Rating selected       | work             | OK     |     |               |
| 4     | Age Verification modal appears| Feedback accepted     | work             | OK     |     |               |
| 5     | Enter DOB = 19.06.1991        | Access granted        | alcohol displayed| OK     |   https://grocerymate.masterschool.com/store#  |               |

---

### Scenario 9: Invalid DOB Input

**User Story:**  
As a user, I should receive validation errors for invalid DOB.

| Step# | Action                         | Expected Outcome   | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|--------------------------------|--------------------|------------------|--------|-----|---------------|
| 1     | Log in                         | User logged in     | Login successful | OK     |  https://grocerymate.masterschool.com/   |               |
| 2     | Navigate to shop section       | Product page loads | work             | OK     |     |               |
| 3     | Select alcohol tab             | Rating selected    | work             | OK     |     |               |
| 4     | Age Verification modal appears | Feedback accepted  | work             | OK     |     |               |
| 5     | Enter DOB = "99/99/9999"       | Access not granted | work             | OK     |     |               |

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
