# crawler_for_yapi
Crawling json files saved in yapi

All files are storeed within the scripts directory.
Before executing the python files, please make sure that python cache are cleared.
#crawler_for_yapi

爬取yapi中保存的json文件

所有文件都存储在脚本目录中。
在执行python文件之前，请确保清除python缓存。

dl_text
-
  This file is used for crawling json files saved as strings in the hidden ace_editor class built in the web.
  One use this file through:
  - hardcode your username and password into the file
  - type "python3 dl_text.py" into the command line

  该文件用于爬取网络内置的隐藏ace_editor类中保存为字符串的json文件。
  通过以下方式使用该文件：
  - 将您的用户名和密码硬编码到文件中
  - 在命令行中输入“python3 dl_text.py”

add_default and exe
-
add_default is the helper function that adds default value and descriptions on the non-commented json return values.
The swicth-case line in the file serve as a table that matches return values with its corresponding chinese translation and default value.
When new return values are added, simply adding a case into the switch-case lines is sufficient.

exe goes through all crawled files and add default/description properties on json return values.
The altered files will be output into the "updated_texts" folder.

add_default 是在未注释的 json 返回值上添加默认值和说明的辅助函数。
文件中的 swicth-case 行充当一个表，将返回值与其相应的中文翻译和默认值进行匹配。
当添加新的返回值时，只需在 switch-case 行中添加一个 case 就足够了。

exe 会遍历所有爬网文件并在 json 返回值上添加默认/描述属性。
更改后的文件将输出到“updated_texts”文件夹中。

ul_text
-
  This file is used for upload the altered json files onto the web editor. After the ul_text, you should see that value on "预览" is different from before.
  - hardcode your username and password into the file
  - type "python3 ul_text.py" into the command line
  - instead of automating the mouse-lick, you now have to manually click into the editor space within 3 seconds whenever an editor opened. So this script is not fully-automated, and thus need the user to be in front of the screen when the script is running.

  该文件用于将更改后的 json 文件上传到 Web 编辑器。在 ul_text 之后，您应该会看到“Preview”上的值与之前不同。
  - 将您的用户名和密码硬编码到文件中
  - 在命令行中输入“python3 ul_text.py”
  - 现在，每当编辑器打开时，您都必须在 3 秒内手动单击编辑器空间，因为脚本无法自动单击鼠标。所以这个脚本不是完全自动化的，因此需要用户在脚本运行时位于屏幕前面。

