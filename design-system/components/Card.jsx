/**
 * @file Card.jsx
 * @description 卡片组件，支持毛玻璃效果和阴影。
 */

import React from 'react';
import { colors, spacing, effects, animations } from '../tokens';

const Card = ({ 
  children, 
  glass = false, 
  shadow = 'md', 
  padding = 6,
  style,
  ...props 
}) => {
  const cardStyle = {
    borderRadius: effects.radius.xl,
    padding: spacing[padding] || spacing[6],
    backgroundColor: glass ? colors.alpha.white92 : colors.bg.primary,
    boxShadow: effects.shadow[shadow],
    backdropFilter: glass ? effects.backdrop.saturate : effects.backdrop.none,
    transition: `transform ${animations.duration.medium} ${animations.ease.inOut}`,
    overflow: 'hidden',
    ...style,
  };

  return (
    <div style={cardStyle} {...props}>
      {children}
    </div>
  );
};

export default Card;
