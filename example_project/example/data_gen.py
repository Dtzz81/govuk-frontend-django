
def generate_data(count=0, sort_by=None, order="asc"):
    bucket_list = [{ "location": "Tanzania", "mountain": "Kili" },
                   { "location": "Switzerland", "mountain": "Materhorn" },
                   {"location": "Japan", "mountain": "Fujisan"},
                   {"location": "UK", "mountain": "Snowdon"}]


    if count == 0:
        if sort_by:
            return sorted(bucket_list, key=lambda x: x[sort_by], reverse=(order == "desc"))
        else:
            return bucket_list  # Return unsorted
    else:
        return bucket_list[1:-1]






#and rng generator
