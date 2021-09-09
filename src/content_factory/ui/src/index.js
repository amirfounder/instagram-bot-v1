import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'
import { ContentContainer } from './components/ContentContainer';

ReactDOM.render(
  <React.StrictMode>
    <div>
      <ContentContainer />
    </div>
  </React.StrictMode>,
  document.getElementById('root')
)