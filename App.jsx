/**
 * @file App.jsx
 * @description 应用程序入口，展示设计系统预览。
 */

import React from 'react';
import DesignSystemPreview from './design-system/DesignSystemPreview';

const App = () => {
  return (
    <div className="app">
      <DesignSystemPreview />
    </div>
  );
};

export default App;
