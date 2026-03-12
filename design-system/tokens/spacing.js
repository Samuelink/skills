/**
 * @file spacing.js
 * @description 间距设计 Token，基于 Apple 官网设计系统。
 * 包含基础间距、网格间距及组件特定间距。
 */

export const spacing = {
  // 基础间距 (8px 基准)
  0: '0px',
  1: '4px',
  2: '8px',
  3: '12px',
  4: '16px',
  5: '20px',
  6: '24px',
  7: '28px',
  8: '32px',
  10: '40px',
  12: '48px',
  16: '64px',
  20: '80px',
  22: '88px',

  // 网格系统
  grid: {
    gutterInner: '24px',
    gutterOuter: '24px',
    columns: 12,
  },

  // 组件间距
  button: {
    h: '16px',
    v: '14px',
  },

  // 导航栏
  nav: {
    height: '44px',
    heightExpanded: '48px',
  },
};
