# XPath Task 2

## 1. Highlighted icon/button

```xpath
//button[contains(@class,'MuiIconButton-root')]
```

---

# Authentication Page

## 2. Email Address input

```xpath
//input[@type='email']
```

---

## 3. Password input

```xpath
//input[@type='password']
```

---

## 4. Sign In button

```xpath
//button[contains(text(),'Sign In')]
```

---

## 5. Create a new account link

```xpath
//a[contains(text(),'Create a new account')]
```

---

## 6. Go to Home link

```xpath
//a[contains(text(),'Go to Home')]
```

---

# Create New Account Page

## 7. Full Name input

```xpath
//input[contains(@placeholder,'Full')]
```

---

## 8. Email Address input

```xpath
//input[@type='email']
```

---

## 9. Password input

```xpath
//input[@type='password']
```

---

## 10. Sign Up button

```xpath
//button[contains(text(),'Sign Up')]
```

---

# Store Modal

## 11. Confirm button

```xpath
//button[contains(text(),'Confirm')]
```

---

# Shop Page

## 12. Quantity input for Oranges

```xpath
//h6[contains(text(),'Oranges')]/ancestor::div[contains(@class,'card')]//input
```

---

## 13. Add to cart button for Oranges

```xpath
//h6[contains(text(),'Oranges')]/ancestor::div[contains(@class,'card')]//button[contains(.,'Add to Cart')]
```

---

## 14. Add to wish list for Oranges

```xpath
//h6[contains(text(),'Oranges')]/ancestor::div[contains(@class,'card')]//*[contains(@data-testid,'FavoriteBorderIcon')]
```
