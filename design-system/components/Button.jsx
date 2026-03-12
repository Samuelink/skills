/**
 * @file Button.jsx
 * @description 按钮组件，支持多种变体和尺寸。
 */

import React from 'react';
import { colors, spacing, typography, effects, animations } from '../tokens';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  disabled = false, 
  onClick,
  style,
  ...props 
}) => {
  const baseStyle = {
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: effects.radius.pill,
    fontFamily: typography.family.base,
    fontWeight: typography.weight.normal,
    cursor: disabled ? 'not-allowed' : 'pointer',
    transition: `all ${animations.duration.normal} ${animations.ease.inOut}`,
    border: 'none',
    outline: 'none',
    textDecoration: 'none',
    opacity: disabled ? 0.42 : 1,
    ...style,
  };

  const variants = {
    primary: {
      backgroundColor: colors.brand.blue,
      color: colors.white,
    },
    secondary: {
      backgroundColor: colors.bg.quaternary,
      color: colors.text.primary,
    },
    outline: {
      backgroundColor: 'transparent',
      border: `1px solid ${colors.brand.blue}`,
      color: colors.brand.blue,
    },
    ghost: {
      backgroundColor: 'transparent',
      color: colors.brand.blue,
    },
  };

  const sizes = {
    sm: {
      padding: `${spacing[1]} ${spacing[3]}`,
      fontSize: typography.size.xs,
    },
    md: {
      padding: `${spacing.button.v} ${spacing.button.h}`,
      fontSize: typography.size.sm,
    },
    lg: {
      padding: `${spacing[4]} ${spacing[6]}`,
      fontSize: typography.size.base,
    },
  };

  const combinedStyle = {
    ...baseStyle,
    ...variants[variant],
    ...sizes[size],
  };

  return (
    <button 
      style={combinedStyle} 
      onClick={!disabled ? onClick : undefined}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
