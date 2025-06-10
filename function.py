def make_purchase(item_name:str):
    return {"message": f"Purchased item: {item_name}"}

def order_items(item_name:str, quantity:int):
    return  {"message": f"{quantity} Ordered items are on the way: {item_name}"}

def complete_purchase(product_name: str, quantity: int = 1):
    return {"message": f" {quantity} x {product_name} successfully purchased!"}

def initiate_order(product_name: str, quantity: int):
    return {"message": f"🛒 Order initiated: {quantity} x {product_name} on the way."}

def query_order_status(order_ref: str):
    return {"status": f"Order {order_ref} is in transit."}

def revoke_order(order_ref: str):
    return {"message": f"Order {order_ref} has been canceled."}

def explore_category(department: str):
    return {"results": [f"{department} Product A", f"{department} Product B"]}

def activate_discount(coupon_code: str):
    return {"message": f"🎉 Coupon '{coupon_code}' applied. Enjoy your savings!"}

def fetch_shipping_details(order_ref: str):
    return {"shipping_info": f"Order {order_ref} ships within 2–4 business days."}
# This code defines functions that simulate a digital shopping assistant's capabilities.
# Each function corresponds to a specific task, such as making purchases, ordering items,
# completing purchases, initiating orders, querying order status, revoking orders,
# exploring categories, activating discounts, and fetching shipping details.
# These functions return structured responses that can be used in a conversational AI context.