def calculteFoodItemMacros(val, serving_size, qty_used):
    return round(((val / serving_size) * qty_used), 2)


def calculateRecipeMacros(recipeItems):
    macros = {
        "total_calories": 0,
        "total_protein_in_g": 0,
        "total_carbs_in_g": 0,
        "total_fats_in_g": 0,
        "total_sugar_in_g": 0,
    }

    for item in recipeItems:
        servingSize = item["serving_size_in_g"]
        qtyUsed = item["qty_used_in_g"]
        macros["total_calories"] += calculteFoodItemMacros(
            item["calories"], servingSize, qtyUsed
        )
        macros["total_protein_in_g"] += calculteFoodItemMacros(
            item["protein_in_g"], servingSize, qtyUsed
        )
        macros["total_carbs_in_g"] += calculteFoodItemMacros(
            item["carbs_in_g"], servingSize, qtyUsed
        )
        macros["total_fats_in_g"] += calculteFoodItemMacros(
            item["fats_in_g"], servingSize, qtyUsed
        )
        macros["total_sugar_in_g"] += calculteFoodItemMacros(
            item["sugar_in_g"], servingSize, qtyUsed
        )

    return macros
