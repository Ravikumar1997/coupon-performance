from cgi import test
import json
from wsgiref import headers

import couponConstants
from locust import HttpUser, between, task


class FetchCoupons(HttpUser):
    # How long a simulated user should wait between executing tasks
    wait_time = between(3, 10)

    # When a load test is started, an instance of a User class will be created for each simulated user.
    # Each user will start running within their own green thread.
    # When these users run they pick tasks that they execute, sleep for awhile, and then pick a new task and so on.

# if want to run the via discounting-engine uncomment the first two task and comment below tasks


#     @task
#     def fetchCouponListing(self):
#         self.client.get("/offers/listing", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
#     "city": couponConstants.CITY,
#     "pickup": {
#         "hex": couponConstants.PICK_HEX,
#         "cluster": couponConstants.PICK_CLUSTER
#     },
#     "drop": {
#         "hex": couponConstants.DROP_HEX,
#         "cluster": couponConstants.DROP_CLUSTER
#     },
#     "distance": couponConstants.DISTANCE,
#     "channel": {
#         "name": couponConstants.CHANNEL_NAME,
#         "host": couponConstants.CHANNEL_HOST
#     },
#     "quotes": [
#         {
#             "serviceId": couponConstants.SERVICE_ID,
#             "serviceDetailId": couponConstants.SERVICE_DETAIL_ID,
#             "baseAmount": 10.0,
#             "offersExcluded": {}
#         }
#     ]
# })

#     @task
#     def fetchCouponDetails(self):
#         self.client.get("/offers/details", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
#     "city": couponConstants.CITY,
#     "pickup": {
#         "hex": couponConstants.PICK_HEX,
#         "cluster": couponConstants.PICK_CLUSTER
#     },
#     "drop": {
#         "hex": couponConstants.DROP_HEX,
#         "cluster": couponConstants.DROP_CLUSTER
#     },
#     "distance": couponConstants.DISTANCE,
#     "channel": {
#         "name": couponConstants.CHANNEL_NAME,
#         "host": couponConstants.CHANNEL_HOST
#     },
#     "quotes": [
#         {
#             "serviceId": couponConstants.SERVICE_ID,
#             "serviceDetailId": couponConstants.SERVICE_DETAIL_ID,
#             "baseAmount": 10.0,
#             "offersExcluded": {}
#         }
#     ],
#     "offerInclude" : [],
#     "couponCode": "LOCDISP",
#     "paymentType": "rapido"
# })

    @task
    def fetchOffersFromPricing(self):
        self.client.post("/offers/coupon", headers = {"user" : json.dumps({"_id": "622c395eb519d9ca6f08bb73"}),
    "key":"nqw2amxaq9t7rGzPxFCYHM2G2CUp3cka",
    "latitude":"12.915072",
    "longitude":"77.67721",
    "channel-name":"app",
    "channel-host":"android",
    "appversion":"400"}, json = {
    
    "pickupLocation": {
        "lat": 12.914985723701825,
        "lng": 77.67726894468069
    },
    "dropLocation": {
        "lat": 12.91096317697067,
        "lng":  77.67753515392542
    },
    "fareEstimateId":"63441a051017186de0e3fca1"

})

    @task
    def validateOfferFromPricing(self):
        self.client.post("/campaign/api/coupon/check", headers = {"latitude":"22.5900159",
    "longitude":"88.4009118",
    "city":"Kolkata",
    "key":"nqw2amxaq9t7rGzPxFCYHM2G2CUp3cka",
    "x-consumer-username":"626b8487a2ea2545e8e0d476"}, json = {
    "couponCode": "PRIWEA",
    "drop": {
        "lat": 22.5900159,
        "lng": 88.4009118
    },
    "paymentType": "cash",
    "pickUp": {
        "lat": 22.5892570981467,
        "lng": 88.4087748080492
    }
})

