import re


class CheckoutReviewPage:
    # Replace this with your real checkout review URL.
    URL = "https://example.com/checkout/review"

    def __init__(self, page):
        self.page = page

        # Item-level locators
        self.item_cards = page.locator("[data-testid='review-item']")
        self.item_thumbnail = page.locator("[data-testid='item-thumbnail']")
        self.item_name = page.locator("[data-testid='item-name']")
        self.item_attributes = page.locator("[data-testid='item-attributes']")
        self.item_unit_price = page.locator("[data-testid='item-unit-price']")

        # Pricing locators
        self.subtotal = page.locator("[data-testid='subtotal']")
        self.estimated_tax = page.locator("[data-testid='estimated-tax']")
        self.shipping = page.locator("[data-testid='shipping']")
        self.grand_total = page.locator("[data-testid='grand-total']")

        # Navigation/action locators
        self.product_name_link = page.locator("[data-testid='item-name-link']")
        self.place_order_button = page.locator("[data-testid='place-order']")

    def open(self):
        self.page.goto(self.URL)

    def item_count(self) -> int:
        return self.item_cards.count()

    def has_visible_item_details(self) -> bool:
        return (
            self.item_thumbnail.first.is_visible()
            and self.item_name.first.is_visible()
            and self.item_attributes.first.is_visible()
            and self.item_unit_price.first.is_visible()
        )

    def pricing_fields_visible(self) -> bool:
        return (
            self.subtotal.is_visible()
            and self.estimated_tax.is_visible()
            and self.shipping.is_visible()
            and self.grand_total.is_visible()
        )

    @staticmethod
    def parse_amount(text: str) -> float:
        cleaned = re.sub(r"[^\d.\-]", "", text)
        if not cleaned:
            raise ValueError(f"Could not parse amount from: {text}")
        return float(cleaned)

    def subtotal_value(self) -> float:
        return self.parse_amount(self.subtotal.inner_text())

    def estimated_tax_value(self) -> float:
        return self.parse_amount(self.estimated_tax.inner_text())

    def shipping_value(self) -> float:
        return self.parse_amount(self.shipping.inner_text())

    def grand_total_value(self) -> float:
        return self.parse_amount(self.grand_total.inner_text())

    def total_math_is_correct(self) -> bool:
        computed = (
            self.subtotal_value() + self.estimated_tax_value() + self.shipping_value()
        )
        displayed = self.grand_total_value()
        return abs(computed - displayed) < 0.01

    def click_first_product_name(self):
        self.product_name_link.first.click()
