# crawler_for_yapi
Crawling json files saved in yapi

All files are storeed within the scripts directory.
Before executing the python files, please make sure that python cache are cleared.

dl_text
-
  This file is used for crawling json files saved as strings in the hidden ace_editor class built in the web.
  One use this file through:
  - hardcode your username and password into the file
  - type "python3 dl_text.py" into the command line

add_default and exe
-
add_default is the helper function that adds default value and descriptions on the non-commented json return values.
The swicth-case line in the file serve as a table that matches return values with its corresponding chinese translation and default value.
When new return values are added, simply adding a case into the switch-case lines is sufficient.

exe goes through all crawled files and add default/description properties on json return values.
The altered files will be output into the "updated_texts" folder.

ul_text
-
  This file is used for upload the altered json files onto the web editor. After the ul_text, you should see that value on "预览" is different from before.
  - hardcode your username and password into the file
  - type "python3 ul_text.py" into the command line
  - instead of automating the mouse-lick, you now have to manually click into the editor space within 3 seconds whenever an editor opened. So this script is not fully-automated, and thus need the user to be in front of the screen when the script is running.

