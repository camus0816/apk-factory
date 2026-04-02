# APK Factory

AI驱动的APK自动构建工厂。

## 工作流

1. 告诉我你的APP需求
2. AI生成Flutter代码推送到 `apps/<app-name>/`
3. 触发 GitHub Actions 构建 APK
4. 返回下载链接

## 使用方法

### 方式一：直接告诉我需求（推荐）
发送 "帮我做一个[需求描述]的APP"，AI自动完成。

### 方式二：手动构建
1. 克隆仓库
2. 在 `apps/` 下创建项目
3. 推送后访问 GitHub Actions 触发构建

## 项目结构
```
apps/         # APP 源码
workflows/   # GitHub Actions 工作流
```

## 仓库状态
✅ 初始化完成，等待第一个APP需求
