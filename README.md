# Tabs Tamer
#### Video Demo:  <URL https://www.youtube.com/watch?v=VVAv2Bzrxzg>
#### Description:
TODO
Chrome extension helping to not horder tabs.

This extension will help and secure so that users don't have open tabs not in use that can be hacked.
You will still be able to use ordinary new tab feature in Chrome and therefor you can still have many tabs open, but open with this button will just close all open tabs, bookmark the in a folder with todays date.

I learned how Chrome extension works.
I also learned that there are a lot of extension doing similar things and a lot of features in Chrome that can be used to do this manually.


This is a Chrome Extension called Tabs Tamer to prevent tab hoarding. It's a straightforward tool with no additional settings.

The extension's icon is a plus sign, and clicking on it will save all open tabs as bookmarks before closing them.

I've tailored the extension's behavior to suit my preferences:

1  The active tab remains open after all others are closed. While I could have opted for the first or last tab, this choice ensures that the selected tab stays open.

2 All the tab's URL are saved in a bookmark folder and upon initial use, a folder named "Tabs Tamer" is created.

Within that folder, a subfolder is generated with the current date. Initially, I included the time, but to avoid excessive folder creation, I decided to omit it.

Only one subfolder per day is created.

If a URL has already been bookmarked on the same day, it won't be bookmarked again. However, if it was bookmarked on a different day, it will still be included in the bookmarks.

Note I've identified a bug: if two tabs with the same URL are among those being closed, both will be bookmarked, but that is Ok for me and I will probably not change it in the future.


There are five files in the extension
     manifest.json
     background.js
     In a folder alled "Images" there are three icons.
            icon16.png
            icon48.png
            icon128.png

All javascript is in the background.js and the manifest is version 3

INSTALLATION
Install the chrome extension by:
1) Go to chrome://extensions/
2) Click on developer mode
3) Click on load unpacked and choose the folder where the source code is.
4) When you are back in the page for managing the extensionm click on the details for Tabs Tamer and click on pin to toolbar.
 Now you are ready to use the extension.

 USER INSTRUTCION

When clicking on the plus sign, all tabs that are open will close. The only tab that will still be open is the one that is in focus.
All the url in the tabs are first added to the bookmark lists in a folder named todays date and that is  a subfolder to that folder called Tabs Tamer. If you click the + sign another time same day the tabs will be inlcuded in the same folder, but will only be bookmarekd if the are not already in the lists of bookmarks.

In the file manifest.json tells us that we are using manifest version 3 and the permission for the api is tabs and bookmarks.

In the javascript file background.js:
The activation of the extesnion will happen with help of a listener that listens to if the + sign is clicked.

When it is clicked we first get all the tabs by using:
     chrome.tabs.query
     chrome.bookmarks.getTree

     We then find the active tab.
     Bookmarks all tabs with help of the funciton bookmarkAlltabs.
          First if the folder Tabs Tamer doesn't exist we create it.
          We close all other tabs, with help of chrome.tabs,remove

Enjoy!
