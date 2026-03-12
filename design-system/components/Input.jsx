/**
 * @file Input.jsx
 * @description 输入框组件，遵循 Apple 的极简设计。
 */

import React, { useState } from 'react';
import { colors, spacing, typography, effects, animations } from '../tokens';

const Input = ({ 
  placeholder, 
  value, 
  onChange, 
  type = 'text',
  disabled = false,
  style,
  ...props 
}) => {
  const [isFocused, setIsFocused] = useState(false);

  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    gap: spacing[2],
    width: '100%',
    ...style,
  };

  const inputStyle = {
    width: '100%',
    padding: `${spacing[3]} ${spacing[4]}`,
    borderRadius: effects.radius.md,
    backgroundColor: colors.bg.secondary,
    border: `1px solid ${isFocused ? colors.brand.blue : colors.gray[200]}`,
    fontFamily: typography.family.base,
    fontSize: typography.size.base,
    color: colors.text.primary,
    outline: 'none',
    transition: `border-color ${animations.duration.fast} ${animations.ease.inOut}`,
    boxSizing: 'border-box',
    opacity: disabled ? 0.42 : 1,
    cursor: disabled ? 'not-allowed' : 'text',
  };

  return (
    <div style={containerStyle}>
      <input
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        disabled={disabled}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        style={inputStyle}
        {...props}
      />
    </div>
  );
};

export default Input;
