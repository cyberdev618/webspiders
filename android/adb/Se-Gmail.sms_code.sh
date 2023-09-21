#/usr/bin/bash
#maybe add argument for passing how many times to clear down

user_phone=1230982340

clear_dial() {

  echo "this clears the dial, basically... "
  for VARIABLE in {0..50..1}
  do
    echo "$VARIABLE"
    adb shell input keyevent KEYCODE_DPAD_DOWN
#  sleep 1 
  done
}

adb shell am force-stop com.google.android.apps.messaging

adb shell am start -n com.google.android.apps.messaging/.ui.ConversationListActivity
#sleep 1
adb shell input keyevent KEYCODE_DPAD_DOWN
adb shell input keyevent  KEYCODE_DPAD_CENTER
sleep 1
adb shell input keyevent  KEYCODE_DPAD_UP
#sleep 1 
adb shell input keyevent  KEYCODE_DPAD_CENTER

#OPEN TEXTNOW AND SEND CODE THAT WAY AND THEN DUMP TERMUX SMS AGAIN
adb shell am force-stop com.enflick.android.TextNow
adb shell am start -n com.enflick.android.TextNow/.activities.MainActivity
sleep 3
clear_dial
#sleep 1
adb shell input keyevent KEYCODE_DPAD_UP
#sleep 2 
adb shell input keyevent KEYCODE_DPAD_CENTER
#should be inside textnow now new sms
sleep 2
#send text to self
adb shell input text $user_phone
clear_dial
adb shell input keyevent KEYCODE_DPAD_UP

sleep 2
adb shell input keyevent 279 
adb shell input keyevent KEYCODE_DPAD_RIGHT
adb shell input keyevent KEYCODE_DPAD_CENTER
adb shell input keyevent KEYCODE_DPAD_RIGHT
adb shell input keyevent KEYCODE_DPAD_CENTER
echo Fin ..............


# scripts uses adb commands to control apps on the android phone
# apps needed [ TEXTNOW,FDROID(TERMUX & TERMUX API),SAMSUNG SMS APP]
