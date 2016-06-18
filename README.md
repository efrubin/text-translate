# text-translate
Text translate is a wrapper for the Google Translate API.  It allows you to
access Google Translate over SMS.  This is useful if you are travelling and have
SMS but no data.  The usage is simple:

    [source language] [target language] [query string]

for the language tags, any ISO-639 language code tag is supported. 

Here's an example 


![half-example](https://cloud.githubusercontent.com/assets/12804487/16174333/8d25e8fe-3593-11e6-838c-f735b994f4db.png)

The SMS integration is done via Twilio.  You just need to set up a Twilio number and point the endpoint to the location of your app.

