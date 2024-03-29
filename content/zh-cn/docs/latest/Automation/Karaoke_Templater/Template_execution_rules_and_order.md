---
title: 卡拉OK模板执行环境和顺序
menu:
  docs:
    parent: karaoke-templater
weight: 6120
---

本页描述了许多有关 卡拉OK模板执行器(*kara-templater*)
的工作方式，并且会解释为什么许多东西起作用，而另一些不起作用。

大多数的细节你在卡拉OK模板执行器中是不需要用到的，但是如果你在某些脚本中看到了你不理解的行为，那么本页面可能会解释它。

## 概念

有些术语和概念在本页全篇中都有使用。这些名称和脚本中使用的相似或者完全相同。（译者注：在使用时需要保留英文，故翻译内容保留重要英文）

`tenv`
: **t**emplate **env**ironment(模板环境)的缩写, 或者
  [代码执行环境]({{< relref "./Code_execution_environment" >}})。

`varctx`
: **var**iable **c**on**t**e**x**t(内联变量环境),
  [内联变量]({{< relref "./Inline_variables" >}})存储在的实际区域。

`template`
: 卡拉OK模板执行器(kara-templater)中最基本的 "执行单元(execution
  unit)" , 事实上一个模板就是一个迷你程序，这个程序由
  卡拉OK模板执行器 编译并执行。

`code template`
: 以Lua代码块方式行使功能的模板，但是一般情况下不会直接输出字幕对象。(用
  *code* 关键字声明)

`output template`
: 会产生字幕行(字幕对象)的一类模板，一般以打好K值的行作为输入。(用
  *template* 关键字声明)

`code line`
: 字幕文件中的一行，该行定义了一个code模板(code 模板)。

`template line`
: 字幕文件中的一行，该行定义了一个输出模板(output template),
  或者整个输出模板中的一部分。 (一个 *line*
  类输出模板可以对应多个模板行)

`class(类)`
: 一个类指的是一种类型的模板。有四种基本的模板类, *once*, *line*,
  *syl* and *furi*, 第一个类只对code模板有用。

`modifier(修饰语)`
: 修饰语会影响模板作用的方式和作用的顺序。

`template text` 或 `text`
: 模板的"文本" 部分，可以是code模板中的 Lua
  代码，或者是输出模板中的模板代码。 *line* 类输出模板还有一个
  *pre-line text* 。

## 启动(Start-up)

卡拉OK模板执行器(后文均简称模板应用器)做的第一件事是使用
[卡拉OK框架(karaskel)]({{< relref "../Lua/Modules/karaskel.lua.md" >}})
来收集一些基础的字幕文件信息。这个过程中总是会伴随着传递 `真(true)`值给
*generate_furigana* (生成假名标注)，它属于`karaskel.collect_head`
函数，这意味着
[假名标注(furigana)]({{< relref "Furigana_karaoke" >}}
的样式会被生成，除非它们早就存在。

然后模板应用器会收集文件中的所有模板行(template line)信息。

### 收集，解析并编译模板

文件中的每一行都会被检查是否是一行模板，例如，被打上注释并且特效栏(Effect
field)填写着 *code* 或者 *template* 的行会被作为模板行。

细节在这里并不重要。你要知道的是
特效栏关键字后的修饰语会作为一个参数起作用。

当遇到一个 *line*
类的模板行时，模板应用器首先会检查是否有其他和这行具有一样模板名称的行。如果没有，则会以该名称新建一行，并按照给定的修饰语进行初始化。如果已经存在这样的行,
*该模板行中的文本会被加入到当前模板行中统一成一个新模板行*
。最终应用的修饰语决定于后一个模板行的修饰语，而非当前行。应用模板的过程中，修饰语没有办法从模板中移除。特殊的是
*pre-line* 模板行的文本会被添加到 *pre-line text*
(被置于所有代码的最前面)。

不同类的模板会被分别放置到各自的 "bucket" 中，所以 *line* 和 *syl*
模板不会被一起保存。(应用模板后不会产生同类合并效果)

### 清除(Clean-up)

在所有模板信息都被收集后。所有不需要的行会被从字幕文件中删除，最常见的情况是，第二次应用同一个模板时第一次生成的
*fx(在Effect栏)* 行会先被清除。

### 初始化 *tenv*

在开始实际应用模板之前的最后一项工作就是初始化运行环境。基本上，在所有的模板运行之前，都会被放置到
*tenv*。详见 [代码执行环境]({{< relref "./Code_execution_environment" >}})
("基本上"是指除了 `line`, `orgline`, `syl` 和 `basesyl`.)

## 运行 *once* 模板

所有的 *once*
类模板会被首先执行。这个过程中没有什么激动人心的事情发生，发生的仅仅是一些额外的文件被添加到了
*tenv*。

## 循环访问(Iterate through)卡拉OK行

字幕文件中的每个非模板行都会被浏览并且按顺序应用上模板。

- 如果一行的注释已经打勾，但是特效栏没有写着`Karaoke`，那么应用模板时这行会被跳过。
- 如果一行没被打上注释，并且特效栏写着除了`Karaoke`或者空白以外的文本，它也会被跳过。
- 模板应用器会试图匹配所有非模板行。

如果通过了以上几点，剩下的每一行都会以三个步骤被应用上模板。

首先，所有的 *line*
类模板会试图匹配非模板行然后再逐一在karaoke行上运行。下面会给出"模板匹配行的顺序"的概念。

接下来，所有行内的音节会按顺序被浏览，所有的 *syl*
类模板最终会被应用在每个音节上。

最后，会过一遍所有注音假名的音节，来尝试将所有 *furi*
类模板匹配相应行，然后在注音假名上应用模板。

值得注意的是，音节和注音假名音节是会被解析并储存的音节，而不是用multi时的虚拟音节，或是用char时的虚拟音节，并且不是一个组合。

{{<example-box>}}
假设有三个 `syl` 类模板: A, B 和 C.

- A 是一个规则的模板，不带有 *multi* 或者 *char* 修饰语。
- B 模板含有 *multi* 修饰语，但是不含有 *char* 修饰语。
- C 含有 *char* 和 *multi* 修饰语。

现在这三个模板会被应用到一行中，这行含有两个音节(syllable)。以下是过程:

- 音节1 被选出
  - 模板A匹配到这行，音节1被匹配。
    - 模板A被应用到音节1。
  - 模板B匹配到这行，音节1被匹配。
    - 音节1被分解为多音节标注的虚拟音节1.1 和 1.2
    - 模板B被应用到虚拟音节1.1。
    - 模板B被应用到虚拟音节1.2。
  - 模板C匹配到这行。
    - 音节1被分解为以字符为单位的虚拟音节1.a 和 1.b
    - 音节 1.a 和 1.b 被进一步分解为 1.a1, 1.a2, 1.b1 和 1.b2。
    - 模板C被应用到虚拟音节 1.a1。
    - 模板C被应用到虚拟音节 1.a2。
    - 模板C被应用到虚拟音节 1.b1。
    - 模板C被应用到虚拟音节 1.b2。
  - 音节2 被选出
    - 进行和上面相似的过程。

想知道更多有关 多音节标注 和 以字符为单位的虚拟音节的内容，请看下面。
{{</example-box>}}

如果任何一个模板在以上三个步骤中匹配到了"打好K值的行"，执行过模板后这样的行就会被打上注释，并且特效栏会显示
`karaoke` 。

### 模板匹配行

模板的匹配总是以行为单位，而不是音节或其他单位。

- 如果模板含有 *fxgroup* 修饰语，那么名字和 fxgroup
  名相同的行会被无视。
- 如果模板含有 *all* 修饰语，它会匹配任何行。
- 如果模板和某行有一样的样式，它会匹配到这行。（这是最常见的情况）
- 其他情况下模板不会匹配到行。

## 应用 *line* 类模板

{{<todo>}}待编写(原文如此){{</todo>}}

## 应用 *syl* 和 *furi* 类模板

{{<todo>}}待编写(原文如此){{</todo>}}

## 过程描述

(这部分内容的具体代码可以在Aegisub安装目录下的automation/autoload/kara-templater.lua中读到)

<pre>
卡拉OK模板执行器执行的主要过程:
1. 收集头部信息
   1. 找到所有的头部信息，基本有播放分辨率（X/Y）。
   2. 找到所有的样式。
   3. 生成对应样式的假名标注样式。
2. 收集模板并删除已存在的 "fx" 行lines。
3. 初始化 tenv
   1. 添加 "string", "math" 和 "_G" 标记
   2. 添加 "tenv"自引用
   3. 添加 "retime" 函数
   4. 添加空的 "fxgroup" 表
4. 运行每一个"code once" 模板
5. 对于字幕文件中每个待处理的对话行:
   a. 如果特效栏以 "code" 或 "template"开始:
      1. 跳过行
   b. 否则:
      1. 如果特效栏不是空的，也不是 "karaoke":
         a. 跳过行
      2. 如果特效栏是空的，并且该行被打上注释:
         a. 跳过行
      3. 用karaskel(卡拉OK框架)预处理行
      4. 初始化 varctx(内联变量环境)
      5. 重置 tenv
         1. 把 "orgline" 作为输入
         2. 把 "line", "syl" 和 "basesyl" 置空
      6. 对于每个 "line" 模板:
         如果样式匹配或者作用范围是"all":
         循环过程("template.loops")多次:
         1. 置 "tenv.j" 为循环计数器
         2. a. 如果模板是 code 行:
               1. 置 "tenv.line" 为输入行
               2. 运行 code 代码
            b. 否则:
               1. 产生输出行作为输入行的副本
               2. 置 "tenv.line" t为输出行
               3. 初始化 输出行层(output line Layer)为模板层(template Layer)
               4. 初始化 输出行文本为空
               5. 如果模板含有 pre-line:
                  1. 运行 pre-line 模板
                  2. 在输出结果上附加文本
               6. a. 如果模板匹配到规则的行:
                     对于输入行中的每个音节:
                     1. 置 "tenv.syl" 为音节
                     2. 为音节更新 varctx 
                     3. 运行 line 模板
                     4. 在输出结果上附加文本
                     5. 如果未设置 "notext" :
                        a. 如果设置 "keeptags" :
                           1. 在输出文本上附上 "syl.text" 
                        b. 否则:
                           1. 在输出文本上附上 "syl.text_stripped"(剥离原标签的文本)
                  b. 否则:
                     a. 如果设置了 "keeptags" :
                        1. 在输出文本上附上 "syl.text" 
                     b. 否则
                        1. 在输出文本上附上 "syl.text_stripped"
               7. 把输出行的特效栏填上 "fx"
               8. 把输出行整合到字幕文件中
      7. 对于行中每个主要的音节:
         对于每个 "syl" 模板:
         如果样式匹配或者作用范围是"all":
         如果模板不是在一个无效的fxgroup中:
         1. 置 "tenv.syl" 为音节
         2. 为音节更新 varctx 
         3. 如果音节的inlinefx(内联特效)没有匹配到对应的模板:
            1. 跳过音节
         4. 如果模板设置了 "noblank" 并且这个音节是个空格:
            1. 跳过音节
         5. 如果模板有"char"修饰:
            1. 建立 "charsyl" 作为音节的副本
            2. 置 "tenv.basesyl"(基础音节)为当前的"tenv.syl"
            3. 置 "tenv.syl" 为"charsyl"(字符音节)
            4. 对于音节中每个 Unicode 编码的字符:
               1. 对"charsyl"计算虚拟音节数 
               2. 为"字符音节"更新 varctx  
               3. 对虚拟音节继续进行音节的处理过程 (从 5.b.7.6.)
         6. 如果模板有"multi"修饰:
            1. 建立 "hlsyl"(音节) 作为音节的副本
            2. 除非 "tenv.basesyl" 早就存在,否则置为 "hlsyl"
            3. 置 "tenv.syl" 为 "hlsyl"
            4. 对于音节上每个标记:
               1. 对"hlsyl"计算虚拟音节数
               2. 为"标记音节"更新 varctx  
               3. 对虚拟音节继续进行音节的处理过程 (从 5.b.7.7.)
         7. a. 如果模板是 code 行:
               1. 置 "tenv.line" 为输入行
               2. 运行 code 代码
            b. 否则:
               1. 置 "tenv.line" 为输入行
               2. 运行 code 代码
               循环过程("template.loops")多次:
               1. 置 "tenv.j" 为循环计数器
               2. 创建输出行
               3. 置输出行的样式为虚拟音节样式
               4. 置输出行层为模板层
               5. 置 "tenv.line" 为输出行
               6. 运行模板
               7. 置输出行文本为结果
               8. a. 如果设置了 "keeptags" :
                     1. 在输出文本上附上 "syl.text"
                  b. 如果未设置 "keeptags" :
                     1. 在输出行文本上附上 "syl.text_stripped"
                  c. 其他情况下什么都不会发生
               9. 置输出行的特效栏内容为"fx"
            10. 把输出行整合到字幕文件中
      8. 对于行中的每个假名部分:
         和音节处理方式相同 (5.b.7.)
      9. 如果有非 code 模板应用到行:
         1. 把输入行置为注释
         2. 置输入行的特效栏文本为 "karaoke"
         3. 存储修饰过的输入行到字幕文件

运行 code 行:
1. 编译行文本为 Lua 函数
2. 如果编译失败, 报告错误
3. 置已编译的函数的环境到 tenv
4. 循环过程("template.loops")多次::
   1. 置 "tenv.j" 为循环计数器
   2. 运行已编译的函数
   3. 如果发生错误，报告它

运行一行单独的模板:
1. 置结果文本为模板
2. 如果存在 varctx:
   对于结果文本中的每个属于 "$([a-zA-Z_]+)" 的字符:
   1. 将捕获到的文本转化为小写
   2. a. 如果捕获到的名称在 varctx中:
         1. 替换结果文本中的这部分为 varctx中的值
      b. 否则:
         1. 警告
         2. 保持原文本不变
3. 对于结果文本中匹配到 "!(.-)!" 的情况:
   1. 附加 "结果 " 到捕获的代码中
   2. 按照Lua函数的方式编译 捕获到的代码
   3. 如果编译失败，报告错误
   4. 置已编译的函数的环境到 tenv 中
   5. 运行已编译的函数
      a. 如果已编译的函数产生了错误:
         1. 报告错误
         2. 在结果文本中保留了匹配到的内容
      b. 否则:
         1. 用函数运行的结果替换掉匹配到的内容
</pre>

{{<todo>}}把这变得更合理一些？(Turn this into something more reasonable?){{</todo>}}
