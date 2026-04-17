Example software: grocerymate

### **1. Product Rating System**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Use Case Testing

### Test Cases:

1. **Use Case Testing**:
    - **Test Case**: Verify that a logged-in user who has purchased a product can submit a rating.
        - **Input**: Select 5-star rating and enter valid feedback (e.g., 100 characters).
        - **Expected Outcome**: Rating is submitted successfully and displayed under the product.

2. **Use Case Testing**:
    - **Test Case**: Verify that a user can edit an existing rating.
        - **Input**: Change rating from 3 stars to 4 stars.
        - **Expected Outcome**: Rating updates successfully.

3. **Use Case Testing**:
    - **Test Case**: Verify that a user can delete their rating.
        - **Input**: Click delete on submitted rating.
        - **Expected Outcome**: Rating is removed from the product.

4. **Equivalence Partitioning**:
    - **Test Case**: Verify rating submission for users who have not purchased the product.
        - **Input**: Logged-in user without purchase.
        - **Expected Outcome**: Error message displayed, rating not allowed.

5. **Equivalence Partitioning**:
    - **Test Case**: Verify rating submission for users who have purchased the product.
        - **Input**: Logged-in user with purchase.
        - **Expected Outcome**: Rating submission allowed.

6. **Boundary Value Analysis**:
    - **Test Case**: Verify feedback submission with exactly 300 characters.
        - **Input**: Feedback = 300 characters.
        - **Expected Outcome**: Feedback submitted successfully.

7. **Boundary Value Analysis**:
    - **Test Case**: Verify feedback submission exceeding 500 characters.
        - **Input**: Feedback = 501 characters.
        - **Expected Outcome**: Error message "Feedback cannot exceed 500 characters."

8. **Error Guessing**:
    - **Test Case**: Verify system behavior when feedback is not entered.
        - **Input**: Submit rating without feedback.
        - **Expected Outcome**: Rating submitted successfully (feedback optional).

10. **Use Case Testing**:
    - **Test Case**: Verify average rating calculation is correct.
        - **Input**: Multiple ratings (e.g., 2, 4, 5 stars).
        - **Expected Outcome**: Correct average rating displayed.

---

### **2. Age Verification for Alcohol**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Use Case Testing

### Test Cases:

1. **Use Case Testing**:
    - **Test Case**: Verify age verification modal appears when accessing alcohol category.
        - **Input**: Navigate to alcohol category.
        - **Expected Outcome**: Modal is displayed requesting date of birth.

2. **Boundary Value Analysis**:
    - **Test Case**: Verify access for a user exactly 18 years old.
        - **Input**: Date of Birth = (Today - 18 years).
        - **Expected Outcome**: Access granted to alcohol products.

3. **Boundary Value Analysis**:
    - **Test Case**: Verify access for a user just below 18 years old.
        - **Input**: Date of Birth = (Today - 18 years + 1 day).
        - **Expected Outcome**: Access denied and redirected to homepage.

4. **Equivalence Partitioning**:
    - **Test Case**: Verify access for users below 18 years.
        - **Input**: Date of Birth = (Today - 17 years).
        - **Expected Outcome**: Access denied.

5. **Equivalence Partitioning**:
    - **Test Case**: Verify access for users above 18 years.
        - **Input**: Date of Birth = (Today - 25 years).
        - **Expected Outcome**: Access granted.

6. **Error Guessing**:
    - **Test Case**: Verify system behavior when date of birth is not entered.
        - **Input**: Empty input field.
        - **Expected Outcome**: Error message "Date of Birth is required."

7. **Error Guessing**:
    - **Test Case**: Verify system behavior when invalid date format is entered.
        - **Input**: Date of Birth = "99/99/9999".
        - **Expected Outcome**: Error message for invalid format.

8. **Use Case Testing**:
    - **Test Case**: Verify that age verification persists within session.
        - **Input**: Verify age → navigate away → return to alcohol category.
        - **Expected Outcome**: Modal does not reappear during same session.

9. **Use Case Testing**:
    - **Test Case**: Verify age verification when accessing alcohol via search.
        - **Input**: Search alcohol product and click.
        - **Expected Outcome**: Modal appears before access.

10. **Use Case Testing**:
    - **Test Case**: Verify age verification when accessing alcohol via direct link.
        - **Input**: Open alcohol product URL directly.
        - **Expected Outcome**: Modal appears and blocks access until verified.

---

### **3. Shipping Cost Changes**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Use Case Testing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify free shipping when cart total is exactly €20.
        - **Input**: Cart total = €20.
        - **Expected Outcome**: Free shipping applied.

2. **Boundary Value Analysis**:
    - **Test Case**: Verify shipping fee when cart total is just below €20.
        - **Input**: Cart total = €19.99.
        - **Expected Outcome**: €5 shipping fee applied.

3. **Boundary Value Analysis**:
    - **Test Case**: Verify free shipping when cart total is above €20.
        - **Input**: Cart total = €21.
        - **Expected Outcome**: Free shipping applied.

4. **Equivalence Partitioning**:
    - **Test Case**: Verify shipping fee for totals below threshold.
        - **Input**: Cart total = €30.
        - **Expected Outcome**: €5 shipping fee applied.

5. **Equivalence Partitioning**:
    - **Test Case**: Verify free shipping for totals above threshold.
        - **Input**: Cart total = €70.
        - **Expected Outcome**: Free shipping applied.

6. **Use Case Testing**:
    - **Test Case**: Verify dynamic update of shipping cost in cart.
        - **Input**: Add/remove items from cart.
        - **Expected Outcome**: Shipping cost updates instantly.

7. **Use Case Testing**:
    - **Test Case**: Verify shipping cost consistency between cart and checkout.
        - **Input**: Proceed to checkout.
        - **Expected Outcome**: Shipping cost matches cart value.

9. **Error Guessing**:
    - **Test Case**: Verify behavior when cart is empty.
        - **Input**: No items in cart.
        - **Expected Outcome**: No shipping cost displayed or checkout disabled.
