---
title: 剪贴板
menu:
  docs:
    parent: lua-modules
weight: 6265
---

`clipboard`模块提供读取和写入剪贴板的函数。

## 使用 {#section}

使用`clipboard = require 'aegisub.clipboard'`导入此模块。

### clipboard.get() {#clipboardget}

示例：`text = clipboard.get()`

以字符串形式获取剪贴板的当前内容。
如果剪贴板当前不包含文本或发生错误，则返回`nil`。

### clipboard.set() {#clipboardset}

示例：`clipboard.set(new_text)`

将剪贴板内容设为指定字符串。 设定成功将返回true，出错则返回false。
