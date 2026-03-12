# Apple 官网设计系统深度分析

> 基于 2026 年 3 月 5 日对 https://www.apple.com/ 的详细分析

---

## 1. 调色盘（Color Palette）

### 1.1 主色调（Primary Colors）

#### 文字颜色
```css
/* 主文字颜色 - 深灰黑 */
--sk-body-text-color: rgb(29, 29, 31);
--sk-headline-text-color: rgb(29, 29, 31);

/* 次要文字颜色 */
--sk-glyph-gray-secondary: rgb(110, 110, 115);
--sk-glyph-gray-secondary-alpha: rgba(0, 0, 0, 0.56);

/* 三级文字颜色 */
--sk-glyph-gray-tertiary: rgb(134, 134, 139);
--sk-glyph-gray-tertiary-alpha: rgba(0, 0, 0, 0.48);

/* 次要文字颜色（替代） */
--sk-glyph-gray-secondary-alt: rgb(66, 66, 69);
--sk-glyph-gray-secondary-alt-alpha: rgba(0, 0, 0, 0.72);
```

#### 背景颜色
```css
/* 主背景色 - 纯白 */
--sk-body-background-color: rgb(255, 255, 255);
--sk-fill: rgb(255, 255, 255);

/* 次要背景色 */
--sk-fill-secondary: rgb(250, 250, 252);

/* 三级背景色 */
--sk-fill-tertiary: rgb(245, 245, 247);

/* 四级背景色 */
--sk-fill-gray-quaternary: rgb(232, 232, 237);
--sk-fill-gray-quaternary-alpha: rgba(0, 0, 0, 0.08);
```

#### 品牌色与强调色
```css
/* Apple 蓝 - 主要交互色 */
--sk-body-link-color: rgb(0, 102, 204);
--sk-glyph-blue: rgb(0, 102, 204);
--sk-fill-blue: rgb(0, 113, 227);
--sk-focus-color: #0071e3;

/* Apple 橙 */
--sk-glyph-orange: rgb(182, 68, 0);
--sk-fill-orange: rgb(245, 99, 0);
--sk-fill-orange-secondary: rgb(255, 249, 244);

/* Apple 绿 */
--sk-glyph-green: rgb(0, 128, 9);
--sk-fill-green: rgb(3, 161, 14);
--sk-fill-green-secondary: rgb(245, 255, 246);
--sk-enviro-green: rgb(0, 217, 89);

/* Apple 红 */
--sk-glyph-red: rgb(227, 0, 0);
--sk-fill-red: rgb(227, 0, 0);
--sk-fill-red-secondary: rgb(255, 242, 244);
--sk-productred: rgb(175, 30, 45);

/* Apple 黄 */
--sk-fill-yellow: rgb(255, 224, 69);
--sk-fill-yellow-secondary: rgb(255, 254, 242);
```

### 1.2 导航栏颜色（Navigation Colors）

```css
/* 导航栏文字 - 浅色主题 */
--r-globalnav-color: rgba(0, 0, 0, 0.8);
--r-globalnav-color-secondary: #333336;
--r-globalnav-color-hover: #000000;

/* 导航栏文字 - 深色主题 */
--r-globalnav-color: rgba(255, 255, 255, 0.8);
--r-globalnav-color-secondary: #E8E8ED;
--r-globalnav-color-hover: #FFFFFF;

/* 导航栏背景 */
--r-globalnav-background-opened: #fafafc;
--r-globalnav-background-opened-dark: #161617;
--globalnav-background: rgba(250, 250, 252, 0.92);
--globalnav-background-dark: rgba(22, 22, 23, 0.88);
```

### 1.3 灰度系统（Grayscale System）

```css
/* 填充灰度 */
--sk-fill-gray: rgb(29, 29, 31);
--sk-fill-gray-alpha: rgba(0, 0, 0, 0.88);
--sk-fill-gray-secondary: rgb(134, 134, 139);
--sk-fill-gray-secondary-alpha: rgba(0, 0, 0, 0.48);
--sk-fill-gray-tertiary: rgb(210, 210, 215);
--sk-fill-gray-tertiary-alpha: rgba(0, 0, 0, 0.16);
--sk-fill-gray-quaternary: rgb(232, 232, 237);
--sk-fill-gray-quaternary-alpha: rgba(0, 0, 0, 0.08);

/* 字形灰度 */
--sk-glyph: rgb(0, 0, 0);
--sk-glyph-gray: rgb(29, 29, 31);
--sk-glyph-gray-alpha: rgba(0, 0, 0, 0.88);
```

### 1.4 环境中性色
```css
--sk-enviro-neutral: rgb(232, 232, 237);
```

---

## 2. 间距系统（Spacing System）

### 2.1 网格系统（Grid System）

```css
/* 12 列网格 */
--sk-cssgrid-columns: 12;

/* 列间距（内部） */
--sk-cssgrid-column-gutter-inner: 24px;
--sk-cssgrid-column-gutter-inner-large: 24px;
--sk-cssgrid-column-gutter-inner-xlarge: 24px;
--sk-cssgrid-column-gutter-inner-medium: 24px;
--sk-cssgrid-column-gutter-inner-small: 24px;

/* 行间距（内部） */
--sk-cssgrid-row-gutter-inner: 24px;
--sk-cssgrid-row-gutter-inner-large: 24px;

/* 列间距（外部） */
--sk-cssgrid-column-gutter-outer: 24px;
--sk-cssgrid-column-gutter-outer-large: 24px;

/* 行间距（外部） */
--sk-cssgrid-row-gutter-outer: 0;
```

### 2.2 堆叠间距（Stacked Margins）

```css
/* 默认堆叠间距 */
--sk-default-stacked-margin: 0.4em;

/* 段落 + 元素间距 */
--sk-paragraph-plus-element-margin: 0.8em;

/* 标题 + 首个元素间距 */
--sk-headline-plus-first-element-margin: 0.8em;

/* 标题 + 标题间距 */
--sk-headline-plus-headline-margin: 0.4em;

/* 段落 + 标题间距 */
--sk-paragraph-plus-headline-margin: 1.6em;
```

### 2.3 按钮间距（Button Spacing）

```css
/* 按钮水平外边距 */
--sk-button-margin-horizontal: 14px;

/* 按钮垂直外边距 */
--sk-button-margin-vertical: 14px;

/* 按钮水平内边距 */
--sk-button-padding-horizontal: 16px;

/* 按钮最小宽度基准 */
--sk-button-min-width-basis: 60px;
```

### 2.4 导航栏间距

```css
/* 导航栏高度 */
--r-globalnav-height: 44px;
--r-globalnav-height-with-flyout: 48px;

/* 导航栏浮层间距 */
--r-globalnav-flyout-spacing: 88px;
```

---

## 3. 字体排版（Typography）

### 3.1 字体族（Font Family）

```css
/* 主字体栈 - SF Pro Text */
font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 阿拉伯语 */
font-family: "SF Pro AR", "SF Pro AR Text", "SF Pro Text", "SF Pro Gulf", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 日语 */
font-family: "SF Pro JP", "SF Pro Text", "SF Pro Icons", "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", "メイリオ", "Meiryo", "ＭＳ Ｐゴシック", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 韩语 */
font-family: "SF Pro KR", "SF Pro Text", "SF Pro Icons", "Apple Gothic", "HY Gulim", "MalgunGothic", "HY Dotum", "Lexi Gulim", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 简体中文 */
font-family: "SF Pro SC", "SF Pro Text", "SF Pro Icons", "PingFang SC", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 繁体中文（香港） */
font-family: "SF Pro HK", "SF Pro Text", "SF Pro Icons", "PingFang HK", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 繁体中文（台湾） */
font-family: "SF Pro TC", "SF Pro Text", "SF Pro Icons", "PingFang TC", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 泰语 */
font-family: "SF Pro TH", "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;

/* 图标字体 */
font-family: "SF Pro Icons";
```

### 3.2 字号阶梯（Font Size Scale）

```css
/* 基础字号 */
html {
  font-size: 106.25%; /* 17px */
}

/* 字号阶梯 */
font-size: 12px;  /* 小号文本 */
font-size: 14px;  /* 次要文本、按钮 */
font-size: 17px;  /* 正文、导航 */
```

### 3.3 行高（Line Height）

```css
/* 正文行高 */
line-height: 1.4705882353;  /* 约 1.47 - 17px 字号 */
line-height: 1.3529611765;  /* 约 1.35 - 阿拉伯语 */
line-height: 1.5882352941;  /* 约 1.59 - 日语 */

/* 按钮行高 */
line-height: 1.2857742857;  /* 约 1.29 - 14px 字号 */

/* 标题行高 */
line-height: 1.1764805882;  /* 约 1.18 - 17px 字号 */

/* 小号文本行高 */
line-height: 1.3333733333;  /* 约 1.33 - 12px 字号 */
line-height: 1.4285914286;  /* 约 1.43 - 14px 字号 */

/* 继承行高 */
line-height: inherit;
line-height: 1;  /* 图标 */
```

### 3.4 字重（Font Weight）

```css
/* 常规 */
font-weight: 400;

/* 半粗体 */
font-weight: 600;

/* 继承 */
font-weight: normal;
font-weight: inherit;
```

### 3.5 上标/下标

```css
/* 脚注字号 */
--sk-footnote-font-size: 0.6em;

/* 脚注偏移 */
--sk-footnote-offset-top: -0.5em;
```

---

## 4. 组件特征（Component Features）

### 4.1 圆角半径（Border Radius）

```css
/* 按钮圆角 - 胶囊形 */
--sk-button-border-radius: 980px;
border-radius: 980px;
border-radius: 999px;  /* 完全圆形 */

/* 卡片圆角 */
border-radius: 5px;   /* 小圆角 */
border-radius: 8px;   /* 中圆角 */
border-radius: 10px;  /* 标准圆角 */
border-radius: 12px;  /* 大圆角 */

/* 无圆角 */
border-radius: 0px;
```

**Token 建议：**
```css
--radius-none: 0px;
--radius-sm: 5px;
--radius-md: 8px;
--radius-lg: 10px;
--radius-xl: 12px;
--radius-pill: 980px;
--radius-full: 999px;
```

### 4.2 阴影（Box Shadow）

```css
/* 标准阴影 */
box-shadow: 3px 5px 30px rgba(0, 0, 0, 0.22);
```

**Token 建议：**
```css
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12);
--shadow-md: 3px 5px 30px rgba(0, 0, 0, 0.22);
--shadow-lg: 0 10px 40px rgba(0, 0, 0, 0.25);
```

### 4.3 毛玻璃效果（Backdrop Filter）

```css
/* 导航栏毛玻璃 */
--globalnav-backdrop-filter: saturate(180%) blur(20px);
backdrop-filter: saturate(180%) blur(20px);

/* 按钮毛玻璃 */
--sk-button-backdrop-filter: none;
backdrop-filter: blur(20px);

/* 点导航毛玻璃 */
--sk-dotnav-scrim-backdrop-filter: saturate(180%) blur(20px);

/* 无毛玻璃 */
backdrop-filter: none;
```

**Token 建议：**
```css
--backdrop-none: none;
--backdrop-blur-sm: blur(10px);
--backdrop-blur-md: blur(20px);
--backdrop-blur-lg: blur(30px);
--backdrop-saturate: saturate(180%) blur(20px);
```

### 4.4 过渡动画（Transitions & Animations）

#### 过渡时长
```css
/* 快速过渡 */
--r-globalnav-flyout-close-delay: 0.12s;
--r-globalnav-duration-medium: 0.24s;

/* 标准过渡 */
transition: 160ms ease-in-out;
transition: 250ms linear;
transition: 320ms ease-in-out;

/* 慢速过渡 */
--r-globalnav-flyout-link-opacity-duration: 0.5s;
```

#### 过渡属性
```css
/* 宽度/高度过渡 */
transition: width var(--sk-dotnav-variable-duration) ease-in-out;
transition: height var(--sk-dotnav-hover-animation-duration) linear;

/* 背景色过渡 */
transition: background-color var(--sk-dotnav-hover-animation-duration) linear;

/* 变换过渡 */
transition: transform var(--sk-dotnav-hover-animation-duration) ease-in-out;
transition: transform 320ms ease-in-out 60ms;

/* 透明度过渡 */
transition: opacity 160ms ease-in-out;
transition: opacity 160ms ease-in-out 80ms;

/* 组合过渡 */
transition: opacity 160ms ease-in-out, transform 160ms ease-in-out;
transition: width var(--sk-dotnav-variable-duration) ease-in-out,
            height var(--sk-dotnav-variable-duration) ease-in-out,
            left var(--sk-dotnav-variable-duration) ease-in-out,
            opacity var(--sk-dotnav-variable-duration) ease-in-out,
            background-color var(--sk-dotnav-variable-duration) ease-in-out,
            scale var(--sk-dotnav-variable-duration) ease-in-out,
            transform var(--sk-dotnav-variable-duration) ease-in-out;
```

#### 动画
```css
/* 淡入淡出动画 */
animation: dotnav-become-visible var(--sk-dotnav-fade-in-out-duration) ease-in-out both;
animation: dotnav-become-invisible var(--sk-dotnav-fade-in-out-duration) ease-in-out both;

/* 位移动画 */
animation: dotnav-shift-start-1 var(--sk-dotnav-variable-duration) ease-in-out both;
animation: dotnav-shift-end-1 var(--sk-dotnav-variable-duration) ease-in-out both;

/* 搜索输入动画 */
animation: globalnav-search-input-intro 0.24s cubic-bezier(0.4, 0, 0.6, 1) 0.2s both;
animation: globalnav-search-input-outro 0.24s cubic-bezier(0.4, 0, 0.6, 1) 0ms both;

/* 禁用动画 */
animation: none !important;
transition: none !important;
```

**Token 建议：**
```css
/* 时长 */
--duration-fast: 120ms;
--duration-normal: 160ms;
--duration-medium: 240ms;
--duration-slow: 320ms;
--duration-slower: 500ms;

/* 缓动函数 */
--ease-linear: linear;
--ease-in-out: ease-in-out;
--ease-custom: cubic-bezier(0.4, 0, 0.6, 1);

/* 延迟 */
--delay-none: 0ms;
--delay-short: 60ms;
--delay-medium: 80ms;
--delay-long: 120ms;
--delay-longer: 200ms;
```

### 4.5 焦点样式（Focus Styles）

```css
/* 焦点轮廓 */
outline: 2px solid var(--sk-focus-color, #0071e3);
outline-offset: var(--sk-focus-offset, 1px);

/* 焦点颜色 */
--sk-focus-color: #0071e3;
--sk-focus-color-alt: rgb(0, 0, 0);

/* 焦点偏移 */
--sk-focus-offset: 1px;
--sk-focus-offset-container: 3px;
--sk-focus-offset: -7px;  /* 负偏移 */
```

### 4.6 禁用状态

```css
/* 禁用透明度 */
--sk-link-disabled-opacity: 0.42;
--sk-button-disabled-opacity: var(--sk-link-disabled-opacity, 0.42);
```

---

## 5. 响应式断点（Responsive Breakpoints）

### 5.1 断点定义

```css
/* Small - 移动设备 */
@media (max-width: 734px) { }

/* Medium - 平板 */
@media (max-width: 1068px) { }

/* Large - 桌面（默认） */
/* 无需媒体查询，默认样式 */

/* XLarge - 大屏桌面 */
@media (min-width: 1441px) { }

/* 高度断点 - 针对高屏幕 */
@media (min-width: 1441px) and (min-height: 776px) { }  /* xlargetall */
@media (min-width: 1070px) and (max-width: 1440px) and (min-height: 776px) { }  /* largetall */
@media (min-width: 736px) and (max-width: 1069px) and (min-height: 734px) { }  /* mediumtall */
```

### 5.2 断点范围总结

| 断点名称 | 宽度范围 | 高度范围 | 设备类型 |
|---------|---------|---------|---------|
| **small** | ≤ 734px | - | 手机 |
| **medium** | 735px - 1068px | - | 平板 |
| **large** | 1069px - 1440px | - | 桌面 |
| **xlarge** | ≥ 1441px | - | 大屏桌面 |
| **mediumtall** | 736px - 1069px | ≥ 734px | 高屏平板 |
| **largetall** | 1070px - 1440px | ≥ 776px | 高屏桌面 |
| **xlargetall** | ≥ 1441px | ≥ 776px | 高屏大桌面 |

### 5.3 特殊媒体查询

```css
/* 反色模式 */
@media (inverted-colors) { }

/* 最小桌面宽度 */
@media only screen and (min-width: 834px) { }

/* 最大平板宽度 */
@media only screen and (max-width: 833px) { }

/* 支持 backdrop-filter */
@supports ((-webkit-backdrop-filter: initial) or (backdrop-filter: initial)) { }
```

**Token 建议：**
```css
/* 断点变量 */
--breakpoint-sm: 734px;
--breakpoint-md: 1068px;
--breakpoint-lg: 1440px;
--breakpoint-xl: 1441px;

/* 高度断点 */
--breakpoint-tall-sm: 734px;
--breakpoint-tall-md: 776px;
```

---

## 6. 设计系统 Token 完整建议

### 6.1 颜色 Tokens

```css
:root {
  /* === 基础颜色 === */
  --color-white: rgb(255, 255, 255);
  --color-black: rgb(0, 0, 0);
  
  /* === 文字颜色 === */
  --color-text-primary: rgb(29, 29, 31);
  --color-text-secondary: rgb(110, 110, 115);
  --color-text-tertiary: rgb(134, 134, 139);
  --color-text-quaternary: rgb(66, 66, 69);
  
  /* === 背景颜色 === */
  --color-bg-primary: rgb(255, 255, 255);
  --color-bg-secondary: rgb(250, 250, 252);
  --color-bg-tertiary: rgb(245, 245, 247);
  --color-bg-quaternary: rgb(232, 232, 237);
  
  /* === 品牌色 === */
  --color-brand-blue: rgb(0, 113, 227);
  --color-brand-blue-light: rgb(0, 102, 204);
  --color-brand-orange: rgb(245, 99, 0);
  --color-brand-green: rgb(3, 161, 14);
  --color-brand-red: rgb(227, 0, 0);
  --color-brand-yellow: rgb(255, 224, 69);
  
  /* === 灰度 === */
  --color-gray-50: rgb(250, 250, 252);
  --color-gray-100: rgb(245, 245, 247);
  --color-gray-200: rgb(232, 232, 237);
  --color-gray-300: rgb(210, 210, 215);
  --color-gray-400: rgb(134, 134, 139);
  --color-gray-500: rgb(110, 110, 115);
  --color-gray-600: rgb(66, 66, 69);
  --color-gray-700: rgb(29, 29, 31);
  --color-gray-800: rgb(22, 22, 23);
  --color-gray-900: rgb(0, 0, 0);
  
  /* === Alpha 颜色 === */
  --color-alpha-black-8: rgba(0, 0, 0, 0.08);
  --color-alpha-black-16: rgba(0, 0, 0, 0.16);
  --color-alpha-black-48: rgba(0, 0, 0, 0.48);
  --color-alpha-black-56: rgba(0, 0, 0, 0.56);
  --color-alpha-black-72: rgba(0, 0, 0, 0.72);
  --color-alpha-black-80: rgba(0, 0, 0, 0.8);
  --color-alpha-black-88: rgba(0, 0, 0, 0.88);
  --color-alpha-white-80: rgba(255, 255, 255, 0.8);
  --color-alpha-white-92: rgba(250, 250, 252, 0.92);
}
```

### 6.2 间距 Tokens

```css
:root {
  /* === 基础间距 === */
  --spacing-0: 0;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-7: 28px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
  --spacing-16: 64px;
  --spacing-20: 80px;
  --spacing-22: 88px;
  
  /* === 网格间距 === */
  --grid-gutter-inner: 24px;
  --grid-gutter-outer: 24px;
  --grid-columns: 12;
  
  /* === 组件间距 === */
  --spacing-button-h: 16px;
  --spacing-button-v: 14px;
}
```

### 6.3 字体 Tokens

```css
:root {
  /* === 字体族 === */
  --font-family-base: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  --font-family-icon: "SF Pro Icons";
  
  /* === 字号 === */
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 17px;
  --font-size-lg: 20px;
  --font-size-xl: 24px;
  
  /* === 行高 === */
  --line-height-tight: 1.18;
  --line-height-snug: 1.29;
  --line-height-normal: 1.47;
  --line-height-relaxed: 1.59;
  
  /* === 字重 === */
  --font-weight-normal: 400;
  --font-weight-semibold: 600;
}
```

### 6.4 圆角 Tokens

```css
:root {
  --radius-none: 0;
  --radius-sm: 5px;
  --radius-md: 8px;
  --radius-lg: 10px;
  --radius-xl: 12px;
  --radius-pill: 980px;
  --radius-full: 999px;
}
```

### 6.5 阴影 Tokens

```css
:root {
  --shadow-none: none;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12);
  --shadow-md: 3px 5px 30px rgba(0, 0, 0, 0.22);
  --shadow-lg: 0 10px 40px rgba(0, 0, 0, 0.25);
}
```

### 6.6 毛玻璃 Tokens

```css
:root {
  --backdrop-none: none;
  --backdrop-blur-sm: blur(10px);
  --backdrop-blur-md: blur(20px);
  --backdrop-blur-lg: blur(30px);
  --backdrop-saturate: saturate(180%) blur(20px);
}
```

### 6.7 动画 Tokens

```css
:root {
  /* === 时长 === */
  --duration-instant: 0ms;
  --duration-fast: 120ms;
  --duration-normal: 160ms;
  --duration-medium: 240ms;
  --duration-slow: 320ms;
  --duration-slower: 500ms;
  
  /* === 缓动 === */
  --ease-linear: linear;
  --ease-in-out: ease-in-out;
  --ease-custom: cubic-bezier(0.4, 0, 0.6, 1);
  
  /* === 延迟 === */
  --delay-none: 0ms;
  --delay-short: 60ms;
  --delay-medium: 80ms;
  --delay-long: 120ms;
  --delay-longer: 200ms;
}
```

### 6.8 断点 Tokens

```css
:root {
  --breakpoint-sm: 734px;
  --breakpoint-md: 1068px;
  --breakpoint-lg: 1440px;
  --breakpoint-xl: 1441px;
  --breakpoint-tall-sm: 734px;
  --breakpoint-tall-md: 776px;
}
```

### 6.9 其他 Tokens

```css
:root {
  /* === 透明度 === */
  --opacity-disabled: 0.42;
  
  /* === 焦点 === */
  --focus-color: #0071e3;
  --focus-width: 2px;
  --focus-offset: 1px;
  --focus-offset-container: 3px;
  
  /* === 导航栏 === */
  --nav-height: 44px;
  --nav-height-expanded: 48px;
}
```

---

## 7. 设计特点总结

### 7.1 核心设计原则

1. **极简主义**：大量留白，简洁的配色方案
2. **层次分明**：通过字重、颜色、间距建立清晰的视觉层次
3. **一致性**：统一的圆角、间距、动画时长
4. **响应式优先**：完善的断点系统，适配各种设备
5. **性能优化**：使用 CSS 变量，便于主题切换和维护

### 7.2 独特设计元素

1. **毛玻璃效果**：`saturate(180%) blur(20px)` 创造深度感
2. **胶囊按钮**：`border-radius: 980px` 的圆角按钮
3. **微妙动画**：120-320ms 的快速过渡，提升交互体验
4. **SF Pro 字体**：Apple 自家字体，多语言支持
5. **12 列网格**：24px 间距的网格系统

### 7.3 颜色使用策略

1. **主色调**：以黑白灰为主，品牌色点缀
2. **Alpha 通道**：大量使用半透明色，增加层次
3. **深色模式**：完整的深色主题支持
4. **语义化颜色**：蓝色（链接）、绿色（成功）、红色（警告）

### 7.4 间距策略

1. **8px 基准**：大部分间距是 8 的倍数
2. **24px 网格**：列间距统一为 24px
3. **em 单位**：文本间距使用 em，保持比例
4. **安全区域**：使用 `env(safe-area-inset-*)` 适配刘海屏

---

## 8. 实施建议

### 8.1 CSS 变量组织

```css
/* 推荐的文件结构 */
/src/design-system/
  ├── tokens/
  │   ├── colors.css
  │   ├── spacing.css
  │   ├── typography.css
  │   ├── effects.css
  │   └── animations.css
  ├── components/
  │   ├── button.css
  │   ├── card.css
  │   └── navigation.css
  └── index.css
```

### 8.2 命名约定

```css
/* 推荐的命名格式 */
--{category}-{property}-{variant}

/* 示例 */
--color-text-primary
--spacing-button-h
--radius-lg
--duration-medium
--shadow-md
```

### 8.3 使用示例

```css
/* 按钮组件 */
.button {
  padding: var(--spacing-button-v) var(--spacing-button-h);
  border-radius: var(--radius-pill);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  background-color: var(--color-brand-blue);
  color: var(--color-white);
  transition: all var(--duration-normal) var(--ease-in-out);
}

.button:hover {
  background-color: var(--color-brand-blue-light);
  transform: scale(1.02);
}

/* 卡片组件 */
.card {
  padding: var(--spacing-6);
  border-radius: var(--radius-xl);
  background-color: var(--color-bg-secondary);
  box-shadow: var(--shadow-md);
  backdrop-filter: var(--backdrop-saturate);
}

/* 导航栏 */
.navigation {
  height: var(--nav-height);
  background-color: var(--color-alpha-white-92);
  backdrop-filter: var(--backdrop-saturate);
  border-bottom: 1px solid var(--color-gray-200);
}
```

---

## 9. 参考资源

- **官网**：https://www.apple.com/
- **分析日期**：2026 年 3 月 5 日
- **主要 CSS 文件**：
  - `globalheader.css` - 导航栏样式
  - `home-gallery.built.css` - 主页画廊样式
  - `ac-globalfooter.built.css` - 页脚样式

---

## 10. 附录：完整 CSS 变量列表

### 颜色变量（完整）

```css
:root {
  /* 文字 */
  --sk-body-text-color: rgb(29, 29, 31);
  --sk-headline-text-color: rgb(29, 29, 31);
  --sk-glyph: rgb(0, 0, 0);
  --sk-glyph-gray: rgb(29, 29, 31);
  --sk-glyph-gray-alpha: rgba(0, 0, 0, 0.88);
  --sk-glyph-gray-secondary: rgb(110, 110, 115);
  --sk-glyph-gray-secondary-alpha: rgba(0, 0, 0, 0.56);
  --sk-glyph-gray-secondary-alt: rgb(66, 66, 69);
  --sk-glyph-gray-secondary-alt-alpha: rgba(0, 0, 0, 0.72);
  --sk-glyph-gray-tertiary: rgb(134, 134, 139);
  --sk-glyph-gray-tertiary-alpha: rgba(0, 0, 0, 0.48);
  
  /* 背景 */
  --sk-body-background-color: rgb(255, 255, 255);
  --sk-fill: rgb(255, 255, 255);
  --sk-fill-secondary: rgb(250, 250, 252);
  --sk-fill-tertiary: rgb(245, 245, 247);
  --sk-fill-gray: rgb(29, 29, 31);
  --sk-fill-gray-alpha: rgba(0, 0, 0, 0.88);
  --sk-fill-gray-secondary: rgb(134, 134, 139);
  --sk-fill-gray-secondary-alpha: rgba(0, 0, 0, 0.48);
  --sk-fill-gray-tertiary: rgb(210, 210, 215);
  --sk-fill-gray-tertiary-alpha: rgba(0, 0, 0, 0.16);
  --sk-fill-gray-quaternary: rgb(232, 232, 237);
  --sk-fill-gray-quaternary-alpha: rgba(0, 0, 0, 0.08);
  
  /* 品牌色 */
  --sk-body-link-color: rgb(0, 102, 204);
  --sk-glyph-blue: rgb(0, 102, 204);
  --sk-fill-blue: rgb(0, 113, 227);
  --sk-glyph-orange: rgb(182, 68, 0);
  --sk-fill-orange: rgb(245, 99, 0);
  --sk-fill-orange-secondary: rgb(255, 249, 244);
  --sk-glyph-green: rgb(0, 128, 9);
  --sk-fill-green: rgb(3, 161, 14);
  --sk-fill-green-secondary: rgb(245, 255, 246);
  --sk-glyph-red: rgb(227, 0, 0);
  --sk-fill-red: rgb(227, 0, 0);
  --sk-fill-red-secondary: rgb(255, 242, 244);
  --sk-fill-yellow: rgb(255, 224, 69);
  --sk-fill-yellow-secondary: rgb(255, 254, 242);
  --sk-productred: rgb(175, 30, 45);
  --sk-enviro-green: rgb(0, 217, 89);
  --sk-enviro-neutral: rgb(232, 232, 237);
  
  /* 焦点 */
  --sk-focus-color: #0071e3;
  --sk-focus-color-alt: rgb(0, 0, 0);
}
```

---

**文档版本**：v1.0  
**最后更新**：2026-03-05  
**分析工具**：浏览器开发者工具 + CSS 文件分析  
**作者**：AI 设计系统分析
