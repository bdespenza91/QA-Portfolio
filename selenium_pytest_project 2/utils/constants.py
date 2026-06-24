BASE_URL = "https://grocerymate.masterschool.com"
LOGIN_URL = f"{BASE_URL}/auth"
STORE_URL = f"{BASE_URL}/store"
ALCOHOL_URL = f"{BASE_URL}/store?category=Alcohol"
CART_URL = f"{BASE_URL}/cart"

VALID_EMAIL = "barry.despenza@test.com"
VALID_PASSWORD = "Test1234!"

SHIPPING_THRESHOLD = 20.00
SHIPPING_FEE = 5.00

ALCOHOL_PRODUCT_NAME = "Heineken"

PRODUCTS_BY_PRICE = {
    "low": "Banana",
    "high": "Organic Whole Milk",
}

RATING_FEEDBACK_LONG = "A" * 501
RATING_FEEDBACK_VALID = "Great product, highly recommend it to anyone looking for quality!"

DATE_OF_BIRTH_18 = None  # calculated dynamically in tests
