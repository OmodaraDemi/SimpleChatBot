# SimpleChatBot
A simple ecommerece chatbot hat simulate a digital shopping assistant's capabilities. Each function corresponds to a specific task, such as making purchases, ordering items, completing purchases, initiating orders, querying order status, revoking orders, exploring categories, activating discounts, and fetching shipping details.

##Test User Prompts
1. make_purchase

"I'd like to buy a MacBook Air, please."

"Can you help me purchase 3 t-shirts?"

2. order_items

"Order 2 pairs of white sneakers."

"I need 5 units of Bluetooth speakers."

3. complete_purchase(product_name, quantity)
Finalize a purchase.

"I'd like to complete my purchase for 2 Galaxy Watches."

"Can you help me buy 5 yoga mats?"

4. initiate_order(product_name, quantity)
Start the order process for a product.

"I want to order 3 packs of protein bars."

"Place an order for one standing desk."

5. query_order_status(order_ref)
Check the status of a specific order.

"Can you check the status of order ID ORD1005?"

"Is order XTR459 already shipped?"

6. revoke_order(order_ref)
Cancel a placed order.

"Please cancel my order ORD6789."

"I’d like to revoke the recent order CANCEL55."

7. explore_category(department)
Browse items in a given department/category.

"Show me items in the fitness department."

"What do you have in the electronics section?"

8. activate_discount(coupon_code)
Apply a discount or coupon code.

"Apply the promo code FALL2025 to my order."

"Use SAVE25NOW on this purchase."

9. fetch_shipping_details(order_ref)
Get estimated delivery or shipping info.

"When will my order SHIP8877 arrive?"

"Tell me the shipping details for order ZX999."
