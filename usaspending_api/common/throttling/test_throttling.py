# import grequests
# import requests
# import json
# from time import sleep
# from datetime import datetime
#
#
# def exception_handler(request, exception):
#     print(f"Request Failed -- Exception: {exception}")
#
#
# def generate_filter_object_spending_over_time(offset):
#     return {
#         "group": "month",
#         "filters": {
#             "time_period": [{"start_date": "2007-10-01", "end_date": "2020-09-30"}],
#             "award_amounts": [
#                 {
#                     "lower_bound": -123123123.99 + (offset * datetime.now().second) + (offset * datetime.now().minute),
#                     "upper_bound": 123123123123.99
#                     + (offset * datetime.now().second)
#                     + (offset * datetime.now().minute),
#                 }
#             ],
#             "award_type_codes": ["A", "B", "C", "D"],
#         },
#         "page": 1,
#         "limit": 60,
#         "order": "desc",
#         "subawards": False,
#         "timestamp": str(datetime.now().time()),
#     }
#
#
# def generate_filter_object_spending_by_geography(offset):
#     return {
#         "filters": {
#             "time_period": [{"start_date": "2007-10-01", "end_date": "2020-09-30"}],
#             "award_amounts": [
#                 {
#                     "lower_bound": -123123123.99 + (offset * datetime.now().second) + (offset * datetime.now().minute),
#                     "upper_bound": 123123123123.99
#                     + (offset * datetime.now().second)
#                     + (offset * datetime.now().minute),
#                 }
#             ],
#             "award_type_codes": ["A", "B", "C", "D"],
#         },
#         "scope": "place_of_performance",
#         "geo_layer": "state",
#         "subawards": False,
#     }
#
#
# IS_LOCAL = False
#
# if IS_LOCAL:
#     url_spending_over_time = "http://127.0.0.1:8000/api/v2/search/spending_over_time"
#     url_spending_by_geography = "http://127.0.0.1:8000/api/v2/search/spending_by_geography"
#     url_last_updated = "http://127.0.0.1:8000/api/v2/awards/last_updated/"
# else:
#     url_spending_over_time = "https://sandbox-api.usaspending.gov/api/v2/search/spending_over_time"
#     url_spending_by_geography = "https://sandbox-api.usaspending.gov/api/v2/search/spending_by_geography"
#     url_last_updated = "https://sandbox-api.usaspending.gov/api/v2/awards/last_updated/"
#
# headers = {"Content-type": "application/json"}
#
# reqs = []
#
# print(f"\nStart: {datetime.now()}\n--------------------------------------------")
#
# print(
#     f"Testing Generic Throttling \n--------------------------------------------\nAssume we want any unique IP to only be able to make 100 calls/second on any endpoint.\nWe set this rate in the settings.py file and do not have to explicitly add it to an endpoing APIView class.\nWe will send 1000 requests synchronously and see if some get throttled."
# )
# input("\nPress Enter to continue...")
#
#
# for i in range(20):
#     data = json.dumps(generate_filter_object_spending_over_time(i))
#     # uncomment below line for async requests
#     # reqs.append(grequests.post(url, headers=headers, data=data))
#     response = requests.post(url_spending_over_time, headers=headers, data=data)
#     print(response.json())
#
#
# # uncomment following lines for for async requests
# # print(reqs)
# # print(grequests.map(reqs, exception_handler=exception_handler))
#
#
# print(
#     f"\n--------------------------------------------\nTesting Endpoint Specific Throttling (ScopedRateThrottle)\n--------------------------------------------\nAssume calls to /search/spending_by_geography are a resource intensive requests.\nWe set a rule that any unique IP can only make 5 requests/second on the /search/spending_by_geography endpoint.\nWe also have to add the throttle_scope and throttle_classes to the APIView class corresponding to this endpoint.\nIt is important to now list the AnonRateThrottle in the throttle_classes.\nWe will send 100 requests synchronously and see if the endpoint specific rate takes precedence over the Anonymous rate."
# )
# input("Press Enter to continue...")
#
# for i in range(10):
#     # headers = {"X-requested-with": "USASpendingFronte"}
#     data = json.dumps(generate_filter_object_spending_by_geography(i))
#     response = requests.post(url_spending_by_geography, headers=headers, data=data)
#     print(response.json())
#
#
# print(
#     f"\n--------------------------------------------\nTesting Custom Throttling\n--------------------------------------------\n"
# )
# input("Press Enter to continue...")
#
# for i in range(10):
#     headers = {"X-requested-with": "USASpendingFrontend"}
#     response = requests.get(url_last_updated, headers=headers)
#     print(response.json())
#
#
# print(f"--------------------------------------------\nEnd: {datetime.now()}")
