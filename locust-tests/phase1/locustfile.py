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


    @task
    def fetchCouponListing(self):
        self.client.get("/offers/listing", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
    "city": "Bangalore",
    "pickup": {
        "hex": "8861892735fffff",
        "cluster": "Sarjapur Road"
    },
    "drop": {
        "hex": "8861892735fffff",
        "cluster": "Sarjapur Road"
    },
    "distanceInKms": 0.4588557078828423,
    "channel": {
        "name": "app",
        "host": "android"
    },
    "quotes": [
        {
            "serviceId": "5bd6c6e2e79cc313a94728d0",
            "serviceDetailId": "5bd6c6e2e79cc313a94728d0",
            "baseAmount": 70.0,
            "offersExcluded": {}
        },
        {
            "serviceId": "572e29b0116b5db3057bd821",
            "serviceDetailId": "57370b61a6855d70057417d1",
            "baseAmount": 70,
            "offersExcluded": {}
        }
    ]
})

    @task
    def fetchCouponDetails(self):
        self.client.get("/offers/details", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
    "city": "Bangalore",
    "pickup": {
        "hex": "8861892735fffff",
        "cluster": "Sarjapur Road"
    },
    "drop": {
        "hex": "8861892735fffff",
        "cluster": "Sarjapur Road"
    },
    "distance": 0.883,
    "channel": {
        "name": "app",
        "host": "android"
    },
    "quotes": [
        {
            "serviceId": "5e79d11d4abaed2515895b62",
            "serviceDetailId": "5e79e1474abaede043895b66",
            "baseAmount": 7.0,
            "offersExcluded": {}
        },
        {
            "serviceId": "5f47ae0cd22ce420065e7a7e",
            "serviceDetailId": "5f4cd594f1283d4f1ba11436",
            "baseAmount": 3.0,
            "offersExcluded": {}
        },
        {
            "serviceId": "5c53562fceb6fc9241980547",
            "serviceDetailId": "5e79e1474abaede043895b66",
            "baseAmount": 13.0,
            "offersExcluded": {}
        },
        {
            "serviceId": "572e29b0116b5db3057bd821",
            "serviceDetailId": "57370b61a6855d70057417d1",
            "baseAmount": 5.0,
            "offersExcluded": {}
        }
    ],
    "couponCode" : "TESTDEMOLOCATION",
    "paymentType" : "rapido"
})

#     @task
#     def fetchOffersFromPricing(self):
#         self.client.post("/offers/coupon", headers = {"user" : json.dumps({"_id": "622c395eb519d9ca6f08bb73"}),
#     "key":"nqw2amxaq9t7rGzPxFCYHM2G2CUp3cka",
#     "latitude":"12.915072",
#     "longitude":"77.67721",
#     "channel-name":"app",
#     "channel-host":"android",
#     "appversion":"400"}, json = {
    
#     "pickupLocation": {
#         "lat": 12.914985723701825,
#         "lng": 77.67726894468069
#     },
#     "dropLocation": {
#         "lat": 12.91096317697067,
#         "lng":  77.67753515392542
#     }

# })

#     @task
#     def validateOfferFromPricing(self):
#         self.client.post("/campaign/api/coupon/check", headers = {"latitude":"12.915072",
#     "longitude":"77.67721",
#     "city":"Bangalore",
#     "key":"nqw2amxaq9t7rGzPxFCYHM2G2CUp3cka",
#     "x-consumer-username":"622c395eb519d9ca6f08bb73", "channel-name" : "app", 
#     "channel-host" : "android", 
#     "appversion" : "400"}, json = {
#     "couponCode": "TESTDEMOLOCATION",
#     "drop": {
#         "lat": 12.91096317697067,
#         "lng": 77.67753515392542
#     },
#     "paymentType": "rapido",
#     "pickUp": {
#         "lat":12.914985723701825,
#         "lng": 77.67726894468069
#     }
   
# })

#     @task
#     def postOrderProcessorAPITest(self):
#         self.client.post("/bulk/userOfferLimit/624686497ddbcb80da2543f1", headers = {"authorization", "abhi"},
#          json = {"offers":[
#     "5f6b3c5251e2871e2eb9636d"
# ],"offerType":"coupon"})

