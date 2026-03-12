/**
 * @file DesignSystemPreview.jsx
 * @description 设计系统预览页面。
 */

import React, { useState } from 'react';
import { 
  Button, 
  Input, 
  Card, 
  colors, 
  spacing, 
  typography, 
  effects 
} from './index';

const Section = ({ title, children }) => (
  <section style={{ marginBottom: spacing[12] }}>
    <h2 style={{ 
      fontSize: typography.size.xl, 
      fontWeight: typography.weight.semibold,
      marginBottom: spacing[6],
      borderBottom: `1px solid ${colors.gray[200]}`,
      paddingBottom: spacing[2]
    }}>
      {title}
    </h2>
    <div style={{ display: 'flex', gap: spacing[4], flexWrap: 'wrap', alignItems: 'center' }}>
      {children}
    </div>
  </section>
);

const DesignSystemPreview = () => {
  const [inputValue, setInputValue] = useState('');

  return (
    <div style={{ 
      padding: spacing[12], 
      maxWidth: '1200px', 
      margin: '0 auto',
      fontFamily: typography.family.base,
      backgroundColor: colors.bg.primary,
      color: colors.text.primary
    }}>
      <header style={{ marginBottom: spacing[16] }}>
        <h1 style={{ fontSize: typography.size.xxxl, fontWeight: typography.weight.semibold }}>
          Apple Design System
        </h1>
        <p style={{ fontSize: typography.size.lg, color: colors.text.secondary }}>
          基于 Apple 官网设计细节的可复用 UI 组件库
        </p>
      </header>

      <Section title="Buttons">
        <Button variant="primary">Primary Button</Button>
        <Button variant="secondary">Secondary</Button>
        <Button variant="outline">Outline</Button>
        <Button variant="ghost">Ghost</Button>
        <Button variant="primary" disabled>Disabled</Button>
        <Button variant="primary" size="sm">Small</Button>
        <Button variant="primary" size="lg">Large</Button>
      </Section>

      <Section title="Inputs">
        <div style={{ width: '300px' }}>
          <Input 
            placeholder="Enter something..." 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)} 
          />
        </div>
        <div style={{ width: '300px' }}>
          <Input 
            placeholder="Disabled input" 
            disabled 
          />
        </div>
      </Section>

      <Section title="Cards">
        <Card style={{ width: '300px' }}>
          <h3 style={{ fontSize: typography.size.lg, marginBottom: spacing[2] }}>Standard Card</h3>
          <p style={{ color: colors.text.secondary }}>This is a basic card with default shadow and padding.</p>
        </Card>
        
        <div style={{ 
          backgroundImage: 'linear-gradient(45deg, #0071e3, #5ac8fa)', 
          padding: spacing[8], 
          borderRadius: effects.radius.xl 
        }}>
          <Card glass style={{ width: '300px' }}>
            <h3 style={{ fontSize: typography.size.lg, marginBottom: spacing[2] }}>Glass Card</h3>
            <p style={{ color: colors.text.secondary }}>Card with backdrop blur and saturation effects.</p>
          </Card>
        </div>
      </Section>

      <Section title="Colors">
        {Object.entries(colors.brand).map(([name, value]) => (
          <div key={name} style={{ textAlign: 'center' }}>
            <div style={{ 
              width: '60px', 
              height: '60px', 
              backgroundColor: value, 
              borderRadius: effects.radius.md,
              marginBottom: spacing[1],
              boxShadow: effects.shadow.sm
            }} />
            <span style={{ fontSize: typography.size.xs }}>{name}</span>
          </div>
        ))}
      </Section>
    </div>
  );
};

export default DesignSystemPreview;
