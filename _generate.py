#!/usr/bin/env python3
"""
APK Factory - 接收参数自动生成 Flutter APP 并触发构建
用法: python3 _generate.py <app_name> <description>
"""
import sys, json, base64, urllib.request

TOKEN = "YOUR_TOKEN"  # 替换为你的 GitHub Token
REPO = "camus0816/apk-factory"

if len(sys.argv) < 3:
    print("用法: python3 _generate.py <app_name> <description>")
    sys.exit(1)

app_name = sys.argv[1]
description = " ".join(sys.argv[2:])

# Flutter 项目模板
template = {
    "pubspec.yaml": f"""name: {app_name}
description: {description}
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.6

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
""",
    "lib/main.dart": f"""import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {{
  const MyApp({{super.key}});
  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: '{description}',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(title: Text('{description}')),
        body: const Center(child: Text('Hello!')),
      ),
    );
  }}
}}
"""
}

# 创建项目文件
for path, content in template.items():
    full_path = f"apps/{app_name}/{path}"
    encoded = base64.b64encode(content.encode()).decode()
    data = json.dumps({
        "message": f"feat: 生成 {app_name}",
        "content": encoded
    }).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{{full_path}}",
        data=data,
        headers={{"Authorization": f"token {{TOKEN}}", "Content-Type": "application/json"}},
        method="PUT"
    )
    try:
        urllib.request.urlopen(req)
        print(f"  + {{path}}")
    except Exception as e:
        print(f"  ! {{path}}: {{e}}")

print(f"\n✅ {{app_name}} 创建完成!")
print(f"触发构建: https://github.com/{{REPO}}/actions/workflows/build-apk.yml")
