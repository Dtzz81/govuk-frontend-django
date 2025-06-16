
# def generate_data(count=0):
#     bucket_list = ["Iceland", "Thaiwan"]
#     return bucket_list[:count]

def generate_data(count=0, sort_by=None):
    bucket_list = [{ "country": "Tanzania", "hike": "Kili" },
                   { "country": "Switzerland", "hike": "Materhorn" },
                   {"country": "Japan", "hike": "Fujisan"},
                   {"country": "UK", "hike": "Snowdon"}]


    if count == 0:
        if sort_by:
            return sorted(bucket_list, key=lambda x: x[sort_by])
        else:
            return bucket_list  # Return unsorted
    else:
        return bucket_list[1:-1]
    


