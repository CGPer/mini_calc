# 计算器

#### 项目介绍
非常小巧的计算器，用键盘输入。

#### 软件架构
使用Qt Designer制作的UI

![](https://images.gitee.com/uploads/images/2018/0705/155742_afe47cea_2020534.png "深度截图_选择区域_20180705155718.png")


#### 使用说明

1. 可以直接在Python的IDE内运行。也可以安装pyinstaller，执行命令 pip install PyIntaller
2. 进入下载的文件夹，执行命令 pyinstaller mini_calc_logic.py（执行前确保Python有PyQt5模块）
3. 在当前文件夹会生成一系列文件，在dist文件夹中有可执行文件，双击运行。(建议dist文件不要放在含中文名的文件内运行，否则可能无法运行)
![](https://gitee.com/uploads/images/2018/0630/211520_19dcd05b_2020534.png "深度截图_选择区域_20180630211456.png")
4.示例：sqrt(2)+sin(pi/2)+2**3+8*2-5/3，按下Enter键得到结果。


![示例](https://gitee.com/uploads/images/2018/0630/163312_22830b66_2020534.png "深度截图_选择区域_20180630163254.png")

5.输入框的内容可像文本一样编辑。
6.若想修改UI，可以直接修改ui文件，再执行pyuic5 -o mini_calc_ui.py mini_calc_ui.ui ,会生成新的UI的Python脚本。

#### 问题
显示结果不能大于12位。

#### 参与贡献
凤舞九天

