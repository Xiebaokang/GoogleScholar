# GoogleScholar
生成被引用文章信息word模板，保存pdf下载链接
### 说明
1. 脚本可以保存我们需要的文章的word模板，以及保存pdf的下载链接，在文件夹 “files” 下
2. 先打开项目下的 src_paper.txt 文件，按一行一论文的格式填入需要搜索的文章
3. 再打开梯子，然后打开项目下的 script.py 脚本，确保脚本中 proxies 设置的端口 “7890” 和梯子的端口对应；
4. 然后打开谷歌学术，按F12打开控制台，点击 “网络” -> “文档”，再刷新页面，最后找到 cookie 中的 “__Secure-1PSID” 对应的 value
![如图](images/one.png)
5. 将 script.py 中 cookies 的 __Secure-1PSID 的 value 修改成新的 value
6. 运行 python script.py 脚本
### 注意！
google有反爬机制（人机验证），如果打印出 “请重新获取cookies” 字样，则需要重复步骤 “3” -> “4”
如果仍然不能运行，那就自己下载吧。
