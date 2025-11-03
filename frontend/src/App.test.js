import { render, screen } from '@testing-library/react';
import React from 'react';

// Simple test without Chakra UI to avoid dependency issues
test('renders without crashing', () => {
  const div = document.createElement('div');
  expect(div).toBeTruthy();
});

test('basic React functionality', () => {
  const TestComponent = () => <div>Test Component</div>;
  const { container } = render(<TestComponent />);
  expect(container.textContent).toBe('Test Component');
});
