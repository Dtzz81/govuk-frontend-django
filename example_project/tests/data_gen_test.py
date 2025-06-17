
import pytest
from example.data_gen import generate_data


def test_function_returns_a_list():
    # Arrange

    #act
    result = generate_data()

    # Assert
    assert type(result) == list

# @pytest.mark.skip(reason="lost with this as i move forward")
def test_function_returns_a_list_with_2_items():
    result = generate_data(2)
    assert len(result) == 2

def test_each_item_has_value_and_keys():
    # Arrange

    # Act
    result = generate_data()

    # Assert
    for item in result:
        assert "location" in item and "mountain" in item

def test_data_set_sorted_in_ascending_order_by_location():

    # Act
    result = generate_data(sort_by="location")
    location_names = [item["location"] for item in result]

    # Assert
    assert all(location_names[i] <= location_names[i+1] for i in range(len(location_names) - 1))

def test_data_set_sorted_in_ascending_order_by_mountain():

    # Act
    result = generate_data(sort_by="mountain")
    mountain_names = [item["mountain"] for item in result]

    # Assert
    assert all(mountain_names[i] <= mountain_names[i+1] for i in range(len(mountain_names) - 1))

def test_data_set_sorted_in_descending_order_by_location():

    # Act
    result = generate_data(sort_by="location", order="desc")
    location_names = [item["location"] for item in result]

    assert all(location_names[i] >= location_names[i+1] for i in range(len(location_names) - 1))


def test_data_set_sorted_in_ascending_order_by_location():
    # arrange
    bucket_list = [{ "location": "Tanzania",     "mountain": "Kili" },
                   { "location": "Switzerland",  "mountain": "Materhorn" },
                   { "location": "Japan",        "mountain": "Fujisan"},
                   { "location": "UK",           "mountain": "Snowdon"}]

     # Act
    expected_data = [
    {"location": "Japan", "mountain": "Fujisan"},
    {"location": "Switzerland", "mountain": "Materhorn"},
    {"location": "Tanzania", "mountain": "Kili"},
    {"location": "UK", "mountain": "Snowdon"}]


    result = generate_data(sort_by="location", order="asc")

    # Assert
    assert result == expected_data
