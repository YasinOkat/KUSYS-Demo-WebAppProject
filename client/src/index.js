import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { BrowserRouter, Route } from "react-router-dom";
import App from './App';
import Students from './components/StudentsList/Students';
import reportWebVitals from './reportWebVitals';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Route path="/" component={App} exact />
      <Route path="/students" component={Students} /> 
    </BrowserRouter>
  </React.StrictMode>,
);

reportWebVitals();