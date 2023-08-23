import React from 'react';
import ReactDOM from 'react-dom'; // Update the import
import './index.css';
import { BrowserRouter, Route } from "react-router-dom";
import App from './App';
import Students from './components/StudentsList/Students'; // Import the component for the new route
import reportWebVitals from './reportWebVitals';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Route path="/" component={App} exact /> {/* Define your existing route */}
      <Route path="/students" component={Students} /> {/* Add the new route for students */}
    </BrowserRouter>
  </React.StrictMode>,
);

reportWebVitals();