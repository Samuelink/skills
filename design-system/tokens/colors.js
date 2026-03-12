/**
 * @file colors.js
 * @description 颜色设计 Token，基于 Apple 官网设计系统。
 * 包含文字、背景、品牌色及灰度系统。
 */

export const colors = {
  // 基础颜色
  white: 'rgb(255, 255, 255)',
  black: 'rgb(0, 0, 0)',

  // 文字颜色
  text: {
    primary: 'rgb(29, 29, 31)',
    secondary: 'rgb(110, 110, 115)',
    tertiary: 'rgb(134, 134, 139)',
    quaternary: 'rgb(66, 66, 69)',
  },

  // 背景颜色
  bg: {
    primary: 'rgb(255, 255, 255)',
    secondary: 'rgb(250, 250, 252)',
    tertiary: 'rgb(245, 245, 247)',
    quaternary: 'rgb(232, 232, 237)',
  },

  // 品牌色
  brand: {
    blue: 'rgb(0, 113, 227)',
    blueLight: 'rgb(0, 102, 204)',
    orange: 'rgb(245, 99, 0)',
    green: 'rgb(3, 161, 14)',
    red: 'rgb(227, 0, 0)',
    yellow: 'rgb(255, 224, 69)',
  },

  // 灰度系统
  gray: {
    50: 'rgb(250, 250, 252)',
    100: 'rgb(245, 245, 247)',
    200: 'rgb(232, 232, 237)',
    300: 'rgb(210, 210, 215)',
    400: 'rgb(134, 134, 139)',
    500: 'rgb(110, 110, 115)',
    600: 'rgb(66, 66, 69)',
    700: 'rgb(29, 29, 31)',
    800: 'rgb(22, 22, 23)',
    900: 'rgb(0, 0, 0)',
  },

  // Alpha 颜色
  alpha: {
    black8: 'rgba(0, 0, 0, 0.08)',
    black16: 'rgba(0, 0, 0, 0.16)',
    black48: 'rgba(0, 0, 0, 0.48)',
    black56: 'rgba(0, 0, 0, 0.56)',
    black72: 'rgba(0, 0, 0, 0.72)',
    black80: 'rgba(0, 0, 0, 0.8)',
    black88: 'rgba(0, 0, 0, 0.88)',
    white80: 'rgba(255, 255, 255, 0.8)',
    white92: 'rgba(250, 250, 252, 0.92)',
  },
};
