import allure


@allure.feature("Products")
def test_product_creation_and_automatic_deletion(logged_in_supplier, autogenerate_product):
    product_id = autogenerate_product
    response = logged_in_supplier.get_product_variations(product_id=product_id)
    assert response.ok is True, f"Product {product_id} was created, but not found! Response: {response}"
    assert response.result is not None, f"Product {product_id} has no variations. Response: {response}"
    print(f"Product {product_id} is active and verified!")

