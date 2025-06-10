
import requests
import json
from openai import OpenAI
from functions import (
    make_purchase, order_items, complete_purchase, initiate_order, query_order_status, revoke_order,
    explore_category, activate_discount, fetch_shipping_details
)
from tools import tools

client = OpenAI(
    api_key="OLLAMA",
    base_url="http://localhost:11434/v1/"
)

system_prompt = """
You are a digital shopping assistant. Guide users to:
- Explore departments
- Purchase and order products
- Manage order status, shipping, and cancellations
- Apply special offers
Use available tools smartly. Always clarify unclear requests.
"""

conversation = [{"role": "system", "content": system_prompt}]

while True:
    user_input = input("Customer: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=conversation,
        model="granite3.2:2b",
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message
    conversation.append(message)

    if hasattr(message, "tool_calls") and message.tool_calls:
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            if name == "make_purchase":
                result = make_purchase(**args)
            elif name == "order_items":
                result = order_items(**args)
            elif name == "complete_purchase":
                result = complete_purchase(**args)
            elif name == "initiate_order":
                result = initiate_order(**args)
            elif name == "query_order_status":
                result = query_order_status(**args)
            elif name == "revoke_order":
                result = revoke_order(**args)
            elif name == "explore_category":
                result = explore_category(**args)
            elif name == "activate_discount":
                result = activate_discount(**args)
            elif name == "fetch_shipping_details":
                result = fetch_shipping_details(**args)
            else:
                result = {"error": "Unknown function"}

            print(f"Tool response: {result}")
    else:
        print("Assistant:", message.content)
