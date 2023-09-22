## WEBSPIDERS & the n3Tz

#### All Spiders use beautiful soup, requests and selenium
#### the setup requires an android phone right now samsung is the default sms of the android phone but you can lookup your android default sms app and spawn its activity via adb inside the android/adb section of webscrapers the file that sends the adb commands are Se-Gmail.sms_code.sh

*full path is webscrapers/android/adb/Se-Gmail.sms_code.sh*
#### code is 
1. kill sms application just in case its runing
...
adb shell am force-stop com.google.android.apps.messaging
...
2. start the messaging app 
...
 adb shell am start -n com.google.android.apps.messaging/.ui.ConversationListActivity 
...



..* facebook simply logs into facebook careful messing with this facebook is sensitive about bots

 ..* gmail can create an account & bypass sms anti-bot verification 


