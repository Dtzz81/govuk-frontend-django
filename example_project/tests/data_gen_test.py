# from http import client
import pytest
from example.data_gen import generate_data
from example import views

def test_function_returns_a_list():
    result = generate_data()
    assert type(result) == list

def test_function_returns_a_list_with_2_items():
    result = generate_data(2)
    assert len(result) == 2

def test_each_item_has_value_and_keys():
    result = generate_data()

    for item in result:
        assert "location" in item and "mountain" in item

def test_data_set_sorted_in_ascending_order_by_location():
    result = generate_data(sort_by="location")
    location_names = [item["location"] for item in result]

    assert all(location_names[i] <= location_names[i+1] for i in range(len(location_names) - 1))

def test_data_set_sorted_in_ascending_order_by_mountain():

    result = generate_data(sort_by="mountain")
    mountain_names = [item["mountain"] for item in result]
    assert all(mountain_names[i] <= mountain_names[i+1] for i in range(len(mountain_names) - 1))

def test_data_set_sorted_in_descending_order_by_location():

    result = generate_data(sort_by="location", order="desc")
    location_names = [item["location"] for item in result]

    assert all(location_names[i] >= location_names[i+1] for i in range(len(location_names) - 1))


def test_data_set_sorted_in_ascending_order_by_location():
    bucket_list = [{ "location": "Tanzania",     "mountain": "Kili" },
                   { "location": "Switzerland",  "mountain": "Materhorn" },
                   { "location": "Japan",        "mountain": "Fujisan"},
                   { "location": "UK",           "mountain": "Snowdon"},
                   {'location': 'Nepal',         "mountain": "Annapurna"},
                   {'location': 'Pakistan',      "mountain": "Nanga Parbat"},]

    expected_data = [
    {"location": "Japan", "mountain": "Fujisan"},
    {'location': 'Nepal', 'mountain': 'Annapurna'},
    {'location': 'Pakistan', 'mountain': 'Nanga Parbat'},
    {"location": "Switzerland", "mountain": "Materhorn"},
    {"location": "Tanzania", "mountain": "Kili"},
    {"location": "UK", "mountain": "Snowdon"}]


    result = generate_data(sort_by="location", order="asc")

    assert result == expected_data


def test_gen_data_returns_entire_list_when_count_is_not_valid():
    count = "abc"
    expected = [
        {"location": "Tanzania", "mountain": "Kili"},
        {"location": "Switzerland", "mountain": "Materhorn"},
        {"location": "Japan", "mountain": "Fujisan"},
        {"location": "UK", "mountain": "Snowdon"},
        {"location": "Nepal", "mountain": "Annapurna"},
        {"location": "Pakistan", "mountain": "Nanga Parbat"},
    ]

    result = generate_data(count=count)

    assert result == expected



def test_gen_data_returns_entire_bucket_list_when_sort_by_is_not_valid():

    invalid_key = "name"

    expected = [
        {"location": "Tanzania", "mountain": "Kili"},
        {"location": "Switzerland", "mountain": "Materhorn"},
        {"location": "Japan", "mountain": "Fujisan"},
        {"location": "UK", "mountain": "Snowdon"},
        {"location": "Nepal", "mountain": "Annapurna"},
        {"location": "Pakistan", "mountain": "Nanga Parbat"},
    ]

    result = generate_data(sort_by=invalid_key)

    assert result == expected
