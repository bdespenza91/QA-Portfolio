# Test Execution Report — GroceryMate

**Application:** GroceryMate  
**URL:** https://grocerymate.masterschool.com/  
**Tester:** Barry Despenza  
**Date:** April 14, 2026  
**Environment:** Chrome (latest), macOS  

---

## Feature 1: Product Rating System

### Scenario 1: Valid Rating Submission

**User Story:**  
As a logged-in user who purchased a product, I want to submit a rating so that I can share feedback.

| Step# | Action                        | Expected Outcome               | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-------------------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in                | Login successful | OK     |     |               |
| 2     | Navigate to purchased product | Product page loads            | work             | OK     |     |               |
| 3     | Select star rating            | Rating selected               | work             | OK     |     |               |
| 4     | Enter feedback (500 chars)    | Feedback accepted             | work             | OK     |     |               |
| 5     | Submit rating                 | Rating displayed under product| displayed        | OK     |     |               |

---

### Scenario 2: Rating Without Purchase

**User Story:**  
As a user, I should not be able to rate products I haven’t purchased.

| Step# | Action               | Expected Outcome       | Actual Outcome | OK/NOK | URL | Link to Issue |
|-------|----------------------|------------------------|----------------|--------|-----|---------------|
| 1     | Log in (no purchase) | User logged in         | OK             | OK     |     |               |
| 2     | Navigate to product  | Product loads          | OK             | OK     |     |               |
| 3     | User click rating    | Inline message appears | OK             | OK     |     |               |

---

### Scenario 3: Feedback Character Limit

**User Story:**  
As a user, I want feedback length to be limited to ensure proper display.

| Step# | Action                        | Expected Outcome               | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-------------------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in                | Login successful | OK     |     |               |
| 2     | Navigate to purchased product | Product page loads            | work             | OK     |     |               |
| 3     | Select star rating          | Rating selected               | work             | OK     |     |               |
| 4     | Enter feedback (500 chars)    | Feedback accepted             | work             | OK     |     |               |
| 5     | Enter feedback (501 chars)    | Feedback not accepted         | work             | OK     |     |               |

---

### Scenario 4: Empty Feedback Submission

**User Story:**  
As a user, I should be able to submit a rating without feedback if optional.

| Step# | Action                        | Expected Outcome   | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|--------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in     | Login successful | OK     |     |               |
| 2     | Navigate to purchased product | Product page loads | work             | OK     |     |               |
| 3     | Select rating                 | Rating selected    | work             | OK     |     |               |
| 4     | Enter no feedback             | Review accepted    | work             | OK     |     |               |

---

## Feature 2: Age Verification for Alcohol

### Scenario 6: Access Alcohol Category

**User Story:**  
As a user, I should verify my age before accessing alcohol products.

| Step# | Action                        | Expected Outcome                  | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-----------------------------------|------------------|--------|-----|---------------|
| 1     | User Create account           | User logged in                   | Login successful | OK     |     |               |
| 2     | Navigate to shop section      | Product pages loads              | work             | OK     |     |               |
| 3     | Select alcohol tab            | Alcohol products are loaded      | work             | OK     |     |               |
| 4     | Age Verification modal appears| Error message appears to verify  | work             | OK     |     |               |

---

### Scenario 7: Valid Age Access (18+)

**User Story:**  
As a user 18+, I should access alcohol products.

| Step# | Action                        | Expected Outcome      | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|-------------------------------|-----------------------|------------------|--------|-----|---------------|
| 1     | Log in                        | User logged in        | Login successful | OK     |     |               |
| 2     | Navigate to shop section      | Product page loads    | work             | OK     |     |               |
| 3     | Select alcohol tab            | Rating selected       | work             | OK     |     |               |
| 4     | Age Verification modal appears| Feedback accepted     | work             | OK     |     |               |
| 5     | Enter DOB = 19.06.1991        | Access granted        | alcohol displayed| OK     |     |               |

---

### Scenario 9: Invalid DOB Input

**User Story:**  
As a user, I should receive validation errors for invalid DOB.

| Step# | Action                         | Expected Outcome   | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|--------------------------------|--------------------|------------------|--------|-----|---------------|
| 1     | Log in                         | User logged in     | Login successful | OK     |     |               |
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
| 1     | Log in                   | User logged in        | Login successful | OK     |     |               |
| 2     | Navigate to shop section | Product page loads    | work             | OK     |     |               |
| 3     | Add items totaling €20   | Free shipping applied | Applied          | OK     |     |               |

---

### Scenario 11: Below Threshold (€20)

**User Story:**  
As a user, I should pay shipping below €20.

| Step# | Action                     | Expected Outcome        | Actual Outcome | OK/NOK | URL | Link to Issue |
|-------|----------------------------|-------------------------|----------------|--------|-----|---------------|
| 1     | Log in                     | User logged in          | Login successful | OK   |     |               |
| 2     | Navigate to shop section   | Product page loads      | work           | OK     |     |               |
| 3     | Add items totaling €19.99  | €5 shipping fee applied | Applied        | OK     |     |               |

---

### Scenario 14: Empty Cart Behavior

**User Story:**  
As a user, I should not see shipping cost when cart is empty.

| Step# | Action             | Expected Outcome    | Actual Outcome   | OK/NOK | URL | Link to Issue |
|-------|--------------------|---------------------|------------------|--------|-----|---------------|
| 1     | Log in             | User logged in      | Login successful | OK     |     |               |
| 2     | Navigate to cart   | Products appear     | Works            | OK     |     |               |
| 3     | Remove all items   | €5 shipping removed | Succesful        | OK     |     |               |
