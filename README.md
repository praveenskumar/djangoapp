djangoapp
=========

my train application. 

It was my first python project. I did it in my college as a mini project.

Basically this is a django application, which uses other website as a middleware to get information of trains in India by using train number or station code for information.

This app is actually a SMS service based application, which sends information using SMS, First you need to send an SMS to the specified number(EX: SMET , 16227) to 9222222222, the platform then sends these parameters to our main django application, which in term scraps the railway website ( traininfo.com, etc) for the information and sends that train inofrmation to the number from which it recieved the query through SMS.

Currently It won't work as the SMS gateway, what we have used is no more supports these kind of applications( As we used third party gateways).

Praveen
