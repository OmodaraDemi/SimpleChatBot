tools = [{
        "type": "function",
        "function": {
            "name": "make_purchase",
            "description": "This function is meant to make purchase of items ",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {"type": "string"}
                },
                "required": ["item_name"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "order_items",
            "description": "This function is meant to make order of items ",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {"type": "string"},
                    "quantity": {"type": "integer"},

                },
                "required": ["item_name", "quantity"]
            }
        }
    }

]

tools = [
    {
        "type": "function",
        "function": {
            "name": "complete_purchase",
            "description": "Finalize the purchase of a product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "quantity": {"type": "integer"}
                },
                "required": ["product_name", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "initiate_order",
            "description": "Begin order process for a given product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "quantity": {"type": "integer"}
                },
                "required": ["product_name", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "query_order_status",
            "description": "Get the status of a specific order",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_ref": {"type": "string"}
                },
                "required": ["order_ref"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "revoke_order",
            "description": "Cancel a previously placed order",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_ref": {"type": "string"}
                },
                "required": ["order_ref"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "explore_category",
            "description": "Browse items in a specific department",
            "parameters": {
                "type": "object",
                "properties": {
                    "department": {"type": "string"}
                },
                "required": ["department"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "activate_discount",
            "description": "Apply a promotional discount code",
            "parameters": {
                "type": "object",
                "properties": {
                    "coupon_code": {"type": "string"}
                },
                "required": ["coupon_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_shipping_details",
            "description": "Provide shipping info for a specific order",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_ref": {"type": "string"}
                },
                "required": ["order_ref"]
            }
        }
    }
]
