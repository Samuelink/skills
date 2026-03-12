/**
 * @file typography.js
 * @description 字体排版设计 Token，基于 Apple 官网设计系统。
 * 包含字体族、字号、行高及字重。
 */

export const typography = {
  // 字体族
  family: {
    base: '"SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif',
    icon: '"SF Pro Icons"',
  },

  // 字号
  size: {
    xs: '12px',
    sm: '14px',
    base: '17px',
    lg: '20px',
    xl: '24px',
    xxl: '32px',
    xxxl: '48px',
  },

  // 行高
  lineHeight: {
    tight: 1.18,
    snug: 1.29,
    normal: 1.47,
    relaxed: 1.59,
  },

  // 字重
  weight: {
    normal: 400,
    semibold: 600,
    bold: 700,
  },
};
