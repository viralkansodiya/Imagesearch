# Copyright (c) 2025, test and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
from tensorflow.keras.preprocessing import image

class ProductSearch(Document):
    pass

@frappe.whitelist()
def find_your_product(product_name):
    base_model = tf.keras.applications.MobileNetV2(input_shape=(224,224,3),
                                                include_top=False,
                                                weights='imagenet')
    base_model.trainable = False	

    # One-time preprocessing
    item_embeddings = []
    item_names = []

    for item in get_image_paths():
        img = image.load_img(item.get("image_path"), target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        embedding = base_model.predict(img_array)
        item_embeddings.append(embedding.flatten())
        item_names.append(item.get("name"))

    # Save item_embeddings and item_names

    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

    # Load the image and preprocess
    img = image.load_img(product_name, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = preprocess_input(img_array)

    # Get the embedding using base model
    query_embedding = base_model.predict(img_array)
    query_embedding = query_embedding.flatten()  # Convert to 1D



    from sklearn.metrics.pairwise import cosine_similarity
    similarities = cosine_similarity(query_embedding.reshape(1, -1), item_embeddings)
    top_index = np.argmax(similarities)
    top_match_item = item_names[top_index]

    print(top_match_item)	


def get_image_paths():
    items = []
    item_list - frappe.db.get_list("Item", pluck="image")
    for row in item_list:
        doc = frappe.get_doc("Item", row)
        file_path = doc.image
        d = doc.image.split("/")[-1]
        items.append({"image_path": file_path, "name": d})
    return items