
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
        assert "country" in item and "hike" in item

def test_data_set_sorted_in_ascending_order_by_country():

    # Act
    result = generate_data(sort_by="country")
    country_names = [item["country"] for item in result]

    # Assert
    assert all(country_names[i] <= country_names[i+1] for i in range(len(country_names) - 1))

def test_data_set_sorted_in_ascending_order_by_hike():

    # Act
    result = generate_data(sort_by="hike")
    hike_names = [item["hike"] for item in result]

    # Assert
    assert all(hike_names[i] <= hike_names[i+1] for i in range(len(hike_names) - 1))

def test_data_set_sorted_in_descending_order_by_country():

    # Act
    result = generate_data(sort_by="country", order="desc")
    country_names = [item["country"] for item in result]

    assert all(country_names[i] >= country_names[i+1] for i in range(len(country_names) - 1))


def test_data_set_sorted_in_ascending_order_by_country():
    # arrange
    bucket_list = [{ "country": "Tanzania",     "hike": "Kili" },
                   { "country": "Switzerland",  "hike": "Materhorn" },
                   { "country": "Japan",        "hike": "Fujisan"},
                   { "country": "UK",           "hike": "Snowdon"}]

     # Act
    expected_data = [
    {"country": "Japan", "hike": "Fujisan"},
    {"country": "Switzerland", "hike": "Materhorn"},
    {"country": "Tanzania", "hike": "Kili"},
    {"country": "UK", "hike": "Snowdon"}]


    result = generate_data(sort_by="country", order="asc")

    # Assert
    assert result == expected_data
