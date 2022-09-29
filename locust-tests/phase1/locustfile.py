import json

import couponConstants
from locust import HttpUser, between, task


class FetchCoupons(HttpUser):
    # How long a simulated user should wait between executing tasks
    wait_time = between(3, 10)

    # When a load test is started, an instance of a User class will be created for each simulated user.
    # Each user will start running within their own green thread.
    # When these users run they pick tasks that they execute, sleep for awhile, and then pick a new task and so on.
    @task
    def fetchCouponListing(self):
        self.client.get("/offers/listing", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
    "city": couponConstants.CITY,
    "pickup": {
        "hex": couponConstants.PICK_HEX,
        "cluster": couponConstants.PICK_CLUSTER
    },
    "drop": {
        "hex": couponConstants.DROP_HEX,
        "cluster": couponConstants.DROP_CLUSTER
    },
    "distance": couponConstants.DISTANCE,
    "channel": {
        "name": couponConstants.CHANNEL_NAME,
        "host": couponConstants.CHANNEL_HOST
    },
    "quotes": [
        {
            "serviceId": couponConstants.SERVICE_ID,
            "serviceDetailId": couponConstants.SERVICE_DETAIL_ID,
            "baseAmount": 10.0,
            "offersExcluded": {}
        }
    ]
})

    @task
    def fetchCouponDetails(self):
        self.client.get("/offers/details", headers={"customer":couponConstants.CUSTOMER_ID, "appversion" : couponConstants.APP_VERSION}, json = {
    "city": couponConstants.CITY,
    "pickup": {
        "hex": couponConstants.PICK_HEX,
        "cluster": couponConstants.PICK_CLUSTER
    },
    "drop": {
        "hex": couponConstants.DROP_HEX,
        "cluster": couponConstants.DROP_CLUSTER
    },
    "distance": couponConstants.DISTANCE,
    "channel": {
        "name": couponConstants.CHANNEL_NAME,
        "host": couponConstants.CHANNEL_HOST
    },
    "quotes": [
        {
            "serviceId": couponConstants.SERVICE_ID,
            "serviceDetailId": couponConstants.SERVICE_DETAIL_ID,
            "baseAmount": 10.0,
            "offersExcluded": {}
        }
    ],
    "offerInclude" : [],
    "couponCode": "LOCDISP",
    "paymentType": "rapido"
})
