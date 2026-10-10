# UFI-TOOLS 官方仓库备份与自定义源

此仓库 Fork 自 [kanoqwq/UFI-TOOLS-PLUGINS](https://github.com/kanoqwq/UFI-TOOLS-PLUGINS)。原始插件和配套资源保持不变；新增 `store.json` 适配 UFI-TOOLS 的自定义插件源格式。

## 导入插件源

打开 UFI 后台 → 插件功能 → 插件商店，在“自定义插件源地址”粘贴：

```text
https://raw.githubusercontent.com/BearHero520/UFI-TOOLS-PLUGINS/main/store.json
```

点击 **加载**。列表应出现 83 项。普通“加载”由手机/电脑浏览器请求索引；如果浏览器不能访问该地址，但 U30 可以访问，可尝试 **加载 (proxy)**，由 U30 代理请求索引。proxy 按钮不负责修复插件内部的依赖下载地址，也不保证后续插件下载链路可用。

这份源是截至原仓库提交 `2b31582a8a075032ac13b51565c1a2dafb04e38d`（2025-08-09）的备份，包含 83 个插件/说明文件和 12 个配套资源，不代表停服前商店的最新全集。

## 使用范围

- 列表索引和插件原文件从 GitHub 读取，不依赖原商店的列表接口。
- 部分插件内部仍然使用 `pan.kanokano.cn` 下载二进制；加载列表成功不代表这些插件能完成安装。
- 当前备份中没有 `kano_sm.tar.gz`、`mihomo.zip`、`openlist-android-arm64.tar.gz`、`qinglong.tar.gz`，不能据此声称完整离线安装。
- 保留原作者和第三方组件归属。本 Fork 新增索引不改变原文件的权利或许可。

## 更新索引

安装 Python 3，将所需插件文件提交到 Git 后，执行：

```sh
python scripts/build-store.py
```

生成器按 Git 内已提交的原始字节计算 MD5/SHA256，以提交 SHA 固定下载地址，避免 Windows 换行转换影响校验。确认列表后提交 `store.json`。
