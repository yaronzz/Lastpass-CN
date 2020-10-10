# Lastpass-CN (插件汉化)

### 已测平台

- Google Chrome谷歌浏览器
- Edge Windows自带浏览器

### 使用方法

1. 安装Lastpass插件

- [Chrome插件](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?utm_source=chrome-ntp-icon) 
- [Edge插件](https://microsoftedge.microsoft.com/addons/detail/bbcinlkgjjkejfdpemiealijmmooekmp?hl=zh-CN)

2. 下载仓库中[messages.json](https://github.com/yaronzz/Lastpass-CN/blob/master/messages.json)文件
3. 在插件安装目录下的_locales目录下新建zh_CN的目录，把messages.json文件放置在这个目录下

| 平台   | 插件路径                                                     |
| ------ | ------------------------------------------------------------ |
| Chrome | **C:\Users\你的用户名\AppData\Local\Google\Chrome\User Data\Default\Extensions\hdokiejnpimakedhajhdlcegeplioahd\插件版本号\\_locales\zh_CN\\** |
| Edge   | **C:\Users\你的用户名\AppData\Local\Microsoft\Edge\User Data\Default\Extensions\bbcinlkgjjkejfdpemiealijmmooekmp\插件版本号\\_locales\zh_CN\\** |

4. 修改插件根目录下的lpfulllib.js和onloadwff.js文件

   查找替换`es:"Spanish"}`替换为`es:"Spanish",zh_CN:"简体中文"}`

5. 在插件 **选项** - **Advanced** - **Lanuage** 的下拉选项中选择简体中文，重启浏览器生效

### 备注

因为平时比较忙没翻译完，后面有时间再更新。另外翻译大多是从谷歌翻译直译过来的，如果有能力优化，欢迎pull request。
