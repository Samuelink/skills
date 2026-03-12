/**
 * @file index.js
 * @description 统一导出所有设计 Token。
 */

import { colors } from './colors';
import { spacing } from './spacing';
import { typography } from './typography';

// 其他效果 Token
export const effects = {
  radius: {
    none: '0',
    sm: '5px',
    md: '8px',
    lg: '10px',
    xl: '12px',
    pill: '980px',
    full: '999px',
  },
  shadow: {
    none: 'none',
    sm: '0 1px 3px rgba(0, 0, 0, 0.12)',
    md: '3px 5px 30px rgba(0, 0, 0, 0.22)',
    lg: '0 10px 40px rgba(0, 0, 0, 0.25)',
  },
  backdrop: {
    none: 'none',
    blurSm: 'blur(10px)',
    blurMd: 'blur(20px)',
    blurLg: 'blur(30px)',
    saturate: 'saturate(180%) blur(20px)',
  },
};

// 动画 Token
export const animations = {
  duration: {
    instant: '0ms',
    fast: '120ms',
    normal: '160ms',
    medium: '240ms',
    slow: '320ms',
    slower: '500ms',
  },
  ease: {
    linear: 'linear',
    inOut: 'ease-in-out',
    custom: 'cubic-bezier(0.4, 0, 0.6, 1)',
  },
};

export { colors, spacing, typography };
