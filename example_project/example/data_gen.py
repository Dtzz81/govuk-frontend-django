def generate_data(count=0, sort_by=None, order=None):
   bucket_list = [
        {"location": "Tanzania", "mountain": "Kili"},
        {"location": "Switzerland", "mountain": "Materhorn"},
        {"location": "Japan", "mountain": "Fujisan"},
        {"location": "UK", "mountain": "Snowdon"},
        {"location": "Nepal", "mountain": "Annapurna"},
        {"location": "Pakistan", "mountain": "Nanga Parbat"},
    ]

   try:
      count = int(count)
      if count < 0:
         raise ValueError
   except (ValueError, TypeError):
         count = 0

   try:
      if sort_by:
         final_list = sorted(bucket_list, key=lambda x: x[sort_by], reverse=(order == "desc"))
      else:
         final_list = bucket_list
   except (KeyError, ValueError, TypeError):
 
      return bucket_list

   if count == 0 or count > len(final_list):
      return final_list
   else:
      return final_list[:count] #slice from beginning

