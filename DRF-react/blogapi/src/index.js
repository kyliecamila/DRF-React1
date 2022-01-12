import React from 'react';
import ReactDOM from 'react-dom';
// import * as serviceWorker from './serviceWorker';
import './index.css';
import { Route, BrowserRouter, Routes } from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';

const routing = (
  <BrowserRouter>
    <Header />
    <Routes>
      <Route exact path="/" element={<App/>}></Route> 
    </Routes>
    <Footer />
  </BrowserRouter>

);

ReactDOM.render(routing, document.getElementById('root'));

// serviceWorker.unregister();