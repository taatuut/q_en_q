import xml.etree.ElementTree as ET
import random

# Define the number of products to generate
num_products = 50000

# Define the number of properties per product
num_properties = 30

# Define the maximum depth of nesting
max_depth = 4

# Define the attribute names
attribute_names = ["color_scheme", "material_type", "size_unit", "weight_unit", "price_currency", "language"]

# Define the property names
property_names = ["color", "material", "size", "weight", "price",
                  "brand", "manufacturer", "model", "sku", "upc",
                  "description", "image_url", "category", "rating", "reviews",
                  "length", "width", "height", "diameter", "thickness",
                  "country_of_origin", "warranty", "power_source", "capacity", "connectivity",
                  "display_type", "resolution", "battery_life", "compatibility", "new_property"]

# Loop over language codes
languages = ["en", "de", "nl", "it", "fr", "es", "pt", "po", "ic", "no", "se", "fi"]
for lang_code in languages:
    # Create the root element
    root = ET.Element("products")

    # Generate the products
    for i in range(num_products):
        # Create the product element
        product = ET.SubElement(root, "product", {"id": str(i + 1), "language": lang_code})

        # Add the properties to the product
        for j in range(num_properties):
            # Create the property element
            property_element = ET.SubElement(product, "property")

            # Set the name of the property
            property_element.set("name", property_names[j])

            # Determine the depth of nesting
            depth = 0
            parent = property_element
            while depth < max_depth:
                if random.random() < 0.5:
                    break
                child = ET.SubElement(parent, "property")
                child.set("name", property_names[j])
                parent = child
                depth += 1

            # Add attributes to the property if required
            if property_names[j] in ["color", "material", "size", "weight", "price",
                                     "length", "width", "height", "diameter", "thickness",
                                     "capacity", "display_type", "resolution", "battery_life", "compatibility"]:
                for attr_name in attribute_names:
                    if attr_name == "language":
                        property_element.set(attr_name, lang_code)
                    else:
                        property_element.set(attr_name, "NA")

            # Add a text value to the property
            property_element.text = "NA"

    # Create the XML file
    tree = ET.ElementTree(root)
    filename = "data/product_descriptions_{}.xml".format(lang_code)
    tree.write(filename)
