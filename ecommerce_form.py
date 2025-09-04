
class OnlinePurchase:
    def __init__(self):
        # List of valid coupons
        self.valid_coupons = {"DISCOUNT10": 0.10, "FREESHIP": 0.00}

    def validate_quantity(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            return True
        return False

    def validate_coupon(self, code):
        if code in self.valid_coupons or code == "":
            return True
        return False

    def validate_address(self, address):
        if isinstance(address, str) and len(address.strip()) > 5:
            return True
        return False

    def process_purchase(self, quantity, coupon, address):
        print("Processing purchase...")

        # Validations
        if not self.validate_quantity(quantity):
            return "❌ Error: Quantity must be an integer greater than 0."

        if not self.validate_coupon(coupon):
            return "❌ Error: The entered coupon code is not valid."

        if not self.validate_address(address):
            return "❌ Error: The shipping address is not valid."

        discount = self.valid_coupons.get(coupon, 0)
        total = quantity * 100   
        total_with_discount = total * (1 - discount)

        return (f"✅ Purchase completed.\n"
                f"Quantity: {quantity}\n"
                f"Coupon: {coupon or 'None'}\n"
                f"Shipping Address: {address}\n"
                f"Total to pay: ${total_with_discount:.2f}")


# Example of usage
if __name__ == "__main__":
    system = OnlinePurchase()

    # Test data
    quantity = 2
    coupon = "DISCOUNT10"
    address = "742 Evergreen Terrace, Springfield"

    result = system.process_purchase(quantity, coupon, address)
    print(result)
