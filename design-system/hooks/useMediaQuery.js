/**
 * @file useMediaQuery.js
 * @description 媒体查询 Hook，用于响应式设计。
 */

import { useState, useEffect } from 'react';

/**
 * 监听媒体查询状态
 * @param {string} query 媒体查询字符串
 * @returns {boolean} 是否匹配
 */
export const useMediaQuery = (query) => {
  const [matches, setMatches] = useState(false);

  useEffect(() => {
    const media = window.matchMedia(query);
    if (media.matches !== matches) {
      setMatches(media.matches);
    }
    const listener = () => setMatches(media.matches);
    media.addEventListener('change', listener);
    return () => media.removeEventListener('change', listener);
  }, [matches, query]);

  return matches;
};
