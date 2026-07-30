import random
import pandas as pd

# (cost -> normal sell)
PRICE_POINTS = {
    (
        "calça",
        "calça wide leg",
        "calça skinny",
        "calça mom",
        "calça aladin",
        "leggings",
    ): [(15,30),(20,30),(25,35),(30,35),(35,38),(40,42)],

    (
        "calça jeans",
        "calça jeans wide leg",
        "calça jeans skinny",
        "calça jeans mom",
        "calça jeans aladin",
    ): [(15,45),(20,45),(25,45),(30,50),(35,50),(40,50),(45,50)],

    (
        "blusa",
        "t-shirt",
        "cropped",
    ): [(10,20),(15,20),(20,25),(25,27),(30,31),(35,36)],

    (
        "short jeans",
        "saia jeans",     
    ): [(15,30),(20,30),(25,35),(30,40),(35,40),(40,45)],

    (
        "short",
        "saia",
    ): [(15,30),(20,30),(25,32),(30,32),(35,37),(40,42)],
   
    (
        "vestido colado curto",
        "vestido colado medio",
        "vestido solto curto",      
        "vestido solto medio",
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio"
    ): [(15,20),(20,25),(25,30),(30,35),(35,37),(40,41)],

    (
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio"
    ): [(15,20),(20,25),(25,30),(30,35),(35,37),(40,41)],

    (
        "vestido colado longo",
        "vestido solto longo",
        "vestido jeans solto longo",
    ): [(15,30),(20,35),(25,40),(30,45),(35,47),(40,50)],

    (
        "cardigan",
        "sueter",
        "macaquinho"
    ): [(15,30),(20,35),(25,35),(30,40),(35,40),(40,42)],

    (
        "blazer",
        "jaqueta",
        "macacao longo"
    ): [(15,35),(20,35),(25,40),(30,40),(35,45),(40,50)],
}


SLEEVES = {
    (
        "blazer",
        "sueter",
        "jaqueta",
        "cardigan",
    ):["Manga longa"],  

    (
        "calça",
        "calça wide leg",
        "calça skinny",
        "calça mom",
        "calça aladin",
        "leggings",
        "calça jeans",
        "calça jeans wide leg",
        "calça jeans skinny",
        "calça jeans mom",
        "calça jeans aladin",
        "short jeans",
        "saia jeans",  
        "short",
        "saia",
        "t-shirt",
    ): ["unknown"],

    (
        "blusa",
        "macaquinho",
        "macacao longo",
        "vestido colado curto",
        "vestido solto curto",
        "vestido colado curto",
        "vestido colado medio",
        "vestido solto curto",      
        "vestido solto medio",
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio"
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio",
        "vestido colado longo",
        "vestido solto longo",
        "vestido jeans solto longo",
        "cropped"
    ) :["Manga curta","Manga longa","Manga 3/4","Uma manga só","regata"],
}

WEIGHTS = {
    (
        "calça",
        "calça wide leg",
        "calça skinny",
        "calça mom",
        "calça aladin",
        "leggings",
    ): 10,

    (
        "calça jeans",
        "calça jeans wide leg",
        "calça jeans skinny",
        "calça jeans mom",
        "calça jeans aladin",
    ): 10,

    (
        "blusa",
        "t-shirt",
        "cropped",
    ): 10,

    (
        "short jeans",
        "saia jeans",     
    ): 10,

    (
        "short",
        "saia",
    ): 10,
         
    (
        "vestido colado curto",
        "vestido colado medio",
        "vestido solto curto",      
        "vestido solto medio",
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio"
    ): 10,

    (
        "vestido jeans colado curto",
        "vestido jeans colado medio",
        "vestido jeans solto curto",      
        "vestido jeans solto medio"
    ): 10,

    (
        "vestido colado longo",
        "vestido solto longo",
        "vestido jeans solto longo",
    ): 10,

    (
        "cardigan",
        "sueter",
        "macaquinho"
    ): 10,

    (
        "blazer",
        "jaqueta",
        "macacao longo"
    ): 10,
}

# Estimate a selling price by linearly interpolating
# between the nearest known cost-price reference points.
def interpolate(points, cost):
    # Sort the reference points by cost to ensure interpolation works correctly
    pts = sorted(points)

    # If the cost is below the minimum known value,
    # return the lowest available price
    if cost <= pts[0][0]:
        return pts[0][1]

    # If the cost is above the maximum known value,
    # return the highest available price
    if cost >= pts[-1][0]:
        return pts[-1][1]

    # Find the two reference points that surround the current cost
    for (c1, p1), (c2, p2) in zip(pts, pts[1:]):

        # Check if the cost falls between these two points
        if c1 <= cost <= c2:

            # Calculate how far the cost is between the two reference costs
            ratio = (cost - c1) / (c2 - c1)

            # Estimate the price using linear interpolation
            return p1 + ratio * (p2 - p1)


# Generate a realistic selling price for a category
# based on its cost and pricing rules.
def normal_price(category, cost):
    # Get the pricing rules associated with the category
    points = get_group_value(PRICE_POINTS, category)

    # Estimate the base price using linear interpolation
    base = interpolate(points, cost)

    # Add a small random variation to simulate real-world pricing
    return round(base + random.uniform(-0.6, 0.6))


# Retrieve the value associated with the group
# that contains the given category.
def get_group_value(mapping, category):
    # Search through all category groups
    for categories, value in mapping.items():

        # Return the corresponding value when the category is found
        if category in categories:
            return value

    # Raise an error if the category does not belong to any group
    raise ValueError(f"Category '{category}' not found.")

def exception_price(cost):
    if cost >= 50:
        return 50
    return min(
        50,
        cost + random.choices([0, 1, 2], weights=[20, 60, 20])[0]
    )

# Generate a synthetic clothing pricing dataset
# based on predefined business rules.
def generate(rows=120000):

    # Get all category groups and their selection weights
    groups = list(PRICE_POINTS.keys())
    weights = [WEIGHTS[group] for group in groups]

    data = []

    for _ in range(rows):

        # Randomly select a category group
        group = random.choices(groups, weights=weights, k=1)[0]

        # Randomly select a category from the chosen group
        category = random.choice(group)

        # Assign whether the item is premium
        premium = random.choices(
            ["no", "yes"],
            weights=[70, 30]
        )[0]

        # Retrieve pricing rules and valid sleeve types
        points = get_group_value(PRICE_POINTS, category)
        sleeves = get_group_value(SLEEVES, category)

        # Get the highest cost that follows the normal pricing curve
        normal_max_cost = points[-1][0]

        # Generate mostly normal cases and a few expensive edge cases
        if random.random() < 0.97:
            cost = random.randint(points[0][0], normal_max_cost)
            price = normal_price(category, cost)
        else:
            cost = random.randint(normal_max_cost + 1, 50)
            price = exception_price(cost)

        # Increase the price for premium items when applicable
        if premium == "yes" and price < 50 and cost <= normal_max_cost:
            price = min(50, price + random.randint(3, 5))

        # Ensure the selling price is never below the cost price
        if price < cost:
            price = cost

        # Store the generated record
        data.append({
            "category": category,
            "sleeveType": random.choice(sleeves),
            "premium": premium,
            "costPrice": cost,
            "price": price
        })

    # Return the generated dataset as a pandas DataFrame
    return pd.DataFrame(data)

# Generate the synthetic dataset and save it as a CSV file.
if __name__ == "__main__":
    df = generate(120000)
    df.to_csv("clothing_pricing_dataset.csv", index=False)
